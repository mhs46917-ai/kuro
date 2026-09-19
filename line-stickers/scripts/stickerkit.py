#!/usr/bin/env python3
"""LINEスタンプ用ツールキット：背景の切り抜き → セリフ合成 → 提出用ZIP作成。

    python3 scripts/stickerkit.py split --sheet work/sheets/A-sheet1.png --set A --grid 3x3 --start 1
    python3 scripts/stickerkit.py cutout  --set A        # work/raw → work/cutout
    python3 scripts/stickerkit.py text    --set A        # セリフを焼き込む（任意）
    python3 scripts/stickerkit.py package --set A        # dist/ にZIPを作る
    python3 scripts/stickerkit.py check   dist/kuro-A.zip

LINE Creators Market の規定（静止スタンプ）:
    スタンプ画像 : 最大 W370 x H320 px / PNG / 透過 / 1ファイル1MB以下 / 8,16,24,32,40個
    メイン画像   : W240 x H240 px
    タブ画像     : W96  x H74  px
    ※ 各辺は偶数、まわりに10pxほど余白を空けるのが推奨。
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import zipfile
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts" / "prompts.json"

STICKER_SIZE = (370, 320)
MAIN_SIZE = (240, 240)
TAB_SIZE = (96, 74)
MAX_BYTES = 1024 * 1024
VALID_COUNTS = (8, 16, 24, 32, 40)
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJKjp-Bold.otf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf",
    "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc",
    "C:/Windows/Fonts/meiryob.ttc",
]

NAME_RE = re.compile(r"^(?P<set>[A-Za-z])[-_]?(?P<no>\d{1,2})")


# --------------------------------------------------------------------------- utils
def find_font(explicit: str | None = None) -> str:
    if explicit:
        if not Path(explicit).exists():
            sys.exit(f"フォントが見つかりません: {explicit}")
        return explicit
    for p in FONT_CANDIDATES:
        if Path(p).exists():
            return p
    sys.exit("日本語フォントが見つかりません。--font でパスを指定してください。")


def load_items(set_id: str) -> dict[int, str]:
    """セットIDから {番号: セリフ} を返す。"""
    data = json.loads(PROMPTS.read_text(encoding="utf-8"))
    for s in data["sets"]:
        if s["id"].upper() == set_id.upper():
            return {it["no"]: it["text"] for it in s["items"]}
    sys.exit(f"セット {set_id} が prompts.json にありません。")


def parse_no(path: Path) -> int | None:
    m = NAME_RE.match(path.stem)
    return int(m.group("no")) if m else None


def collect(in_dir: Path, set_id: str | None) -> list[Path]:
    files = [p for p in sorted(in_dir.iterdir()) if p.suffix.lower() in IMAGE_EXTS]
    if set_id:
        files = [p for p in files if p.stem[:1].upper() == set_id.upper()]
    return files


# ------------------------------------------------------------------- cutout core
def _border_components(bg_mask: np.ndarray) -> np.ndarray:
    """背景候補のうち、画像の外周とつながっている領域だけを True で返す。"""
    try:
        from scipy import ndimage  # type: ignore

        lab, n = ndimage.label(bg_mask)
        if n == 0:
            return np.zeros_like(bg_mask)
        border = np.concatenate([lab[0, :], lab[-1, :], lab[:, 0], lab[:, -1]])
        keep = np.unique(border[border > 0])
        return np.isin(lab, keep)
    except ImportError:  # scipy 無しでも動くフォールバック（少し遅い）
        h, w = bg_mask.shape
        seen = np.zeros((h, w), dtype=bool)
        q: deque[tuple[int, int]] = deque()
        for x in range(w):
            for y in (0, h - 1):
                if bg_mask[y, x] and not seen[y, x]:
                    seen[y, x] = True
                    q.append((y, x))
        for y in range(h):
            for x in (0, w - 1):
                if bg_mask[y, x] and not seen[y, x]:
                    seen[y, x] = True
                    q.append((y, x))
        while q:
            y, x = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and bg_mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    q.append((ny, nx))
        return seen


def _drop_specks(alpha: np.ndarray, min_area: int) -> np.ndarray:
    """ゴミのような小さい点を消す。"""
    if min_area <= 0:
        return alpha
    try:
        from scipy import ndimage  # type: ignore
    except ImportError:
        return alpha
    lab, n = ndimage.label(alpha > 8)
    if n <= 1:
        return alpha
    sizes = ndimage.sum(np.ones_like(lab), lab, index=range(1, n + 1))
    small = {i + 1 for i, sz in enumerate(sizes) if sz < min_area}
    if small:
        alpha = alpha.copy()
        alpha[np.isin(lab, list(small))] = 0
    return alpha


def remove_background(img: Image.Image, tol: float = 34.0, min_area: int = 64) -> Image.Image:
    """単色背景（白）を透過にする。すでに透過済みならそのまま返す。"""
    img = img.convert("RGBA")
    arr = np.asarray(img).astype(np.float32)
    rgb, a = arr[..., :3], arr[..., 3]

    # すでに切り抜き済み（外周の多くが透明）ならそのまま使う
    border_a = np.concatenate([a[0, :], a[-1, :], a[:, 0], a[:, -1]])
    if (border_a < 16).mean() > 0.9:
        return img

    # 外周のピクセルから背景色を推定
    border_rgb = np.concatenate([rgb[0, :], rgb[-1, :], rgb[:, 0], rgb[:, -1]], axis=0)
    bg = np.median(border_rgb, axis=0)

    dist = np.sqrt(((rgb - bg) ** 2).sum(axis=2))
    t_in, t_out = tol * 0.55, tol * 1.6
    soft = np.clip((dist - t_in) / max(t_out - t_in, 1e-6), 0.0, 1.0)  # 0=背景 1=キャラ

    outside = _border_components(dist < t_out)
    new_a = np.where(outside, soft * 255.0, 255.0)
    new_a = np.minimum(new_a, a if a.max() > 0 else 255.0)
    new_a = _drop_specks(new_a, min_area)

    # 半透明の縁に残る背景色（白フチ）を取り除く
    af = (new_a / 255.0)[..., None]
    clean = np.where(af > 0.02, (rgb - bg * (1.0 - af)) / np.maximum(af, 1e-6), rgb)
    out = np.concatenate([np.clip(clean, 0, 255), new_a[..., None]], axis=2)
    return Image.fromarray(out.astype(np.uint8), "RGBA")


def trim(img: Image.Image, threshold: int = 8) -> Image.Image:
    a = np.asarray(img.split()[3])
    ys, xs = np.where(a > threshold)
    if len(xs) == 0:
        return img
    return img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))


def fit_canvas(
    img: Image.Image,
    size: tuple[int, int],
    margin: int = 10,
    box: tuple[int, int, int, int] | None = None,
) -> Image.Image:
    """透明キャンバスの中央に、余白を残して収める。box=(l,t,r,b) で配置領域を限定。"""
    W, H = size
    l, t, r, b = box or (margin, margin, W - margin, H - margin)
    aw, ah = max(r - l, 1), max(b - t, 1)
    scale = min(aw / img.width, ah / img.height)
    new = img.resize((max(int(img.width * scale), 1), max(int(img.height * scale), 1)), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas.paste(new, (l + (aw - new.width) // 2, t + (ah - new.height) // 2), new)
    return canvas


def save_png(img: Image.Image, path: Path, max_bytes: int = MAX_BYTES) -> int:
    img.save(path, "PNG", optimize=True)
    if path.stat().st_size > max_bytes:  # 減色して1MB以下に収める
        for colors in (255, 192, 128, 96):
            img.quantize(colors=colors, method=Image.FASTOCTREE).save(path, "PNG", optimize=True)
            if path.stat().st_size <= max_bytes:
                break
    return path.stat().st_size


# ------------------------------------------------------------------ text overlay
def draw_caption(
    canvas: Image.Image,
    text: str,
    font_path: str,
    band: tuple[int, int, int, int],
    fill=(74, 48, 34, 255),
    stroke=(255, 255, 255, 255),
) -> None:
    l, t, r, b = band
    max_w, max_h = r - l, b - t
    size = max_h
    while size > 8:
        font = ImageFont.truetype(font_path, size)
        bbox = font.getbbox(text, stroke_width=max(size // 8, 2))
        if bbox[2] - bbox[0] <= max_w and bbox[3] - bbox[1] <= max_h:
            break
        size -= 2
    font = ImageFont.truetype(font_path, size)
    sw = max(size // 8, 2)
    d = ImageDraw.Draw(canvas)
    bbox = d.textbbox((0, 0), text, font=font, stroke_width=sw)
    x = l + (max_w - (bbox[2] - bbox[0])) // 2 - bbox[0]
    y = t + (max_h - (bbox[3] - bbox[1])) // 2 - bbox[1]
    d.text((x, y), text, font=font, fill=fill, stroke_width=sw, stroke_fill=stroke)


# ------------------------------------------------------------------- grid split
def parse_grid(spec: str) -> tuple[int, int]:
    try:
        cols, rows = (int(v) for v in spec.lower().split("x"))
        if cols < 1 or rows < 1:
            raise ValueError
    except ValueError:
        sys.exit(f"--grid は 3x3 のように指定してください（今: {spec}）")
    return cols, rows


def is_blank(cell: Image.Image) -> bool:
    """ほぼ単色（＝何も描かれていない）コマかどうか。"""
    small = cell.convert("RGB").resize((32, 32), Image.BILINEAR)
    # チャンネルごとの「面内の」ばらつきを見る（全体のstdだと色味の差を拾ってしまう）
    spread = np.asarray(small, dtype=np.float32).std(axis=(0, 1)).max()
    return float(spread) < 4.0


def cmd_split(args: argparse.Namespace) -> None:
    sheet = Image.open(args.sheet).convert("RGBA")
    cols, rows = parse_grid(args.grid)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    count = args.count or cols * rows
    cw, ch = sheet.width / cols, sheet.height / rows
    inset_x, inset_y = int(cw * args.inset), int(ch * args.inset)

    saved = 0
    for i in range(count):
        r, c = divmod(i, cols)
        if r >= rows:
            break
        box = (round(c * cw) + inset_x, round(r * ch) + inset_y,
               round((c + 1) * cw) - inset_x, round((r + 1) * ch) - inset_y)
        cell = sheet.crop(box)
        no = args.start + i
        name = f"{args.set.upper()}-{no:02d}.png"
        if is_blank(cell):
            print(f"  {r+1}段{c+1}列 → {name}  空のコマのようなので飛ばしました")
            continue
        cell.save(out_dir / name, "PNG")
        print(f"  {r+1}段{c+1}列 → {name}  {cell.width}x{cell.height}")
        saved += 1
    small = [n for n in (cw - 2 * inset_x, ch - 2 * inset_y) if n < 320]
    if small:
        print("  ※ 1コマが小さめです。Geminiの出力解像度を上げるか --grid を粗くしてください。")
    print(f"✓ {saved}枚を {out_dir} に切り出しました。")


# ------------------------------------------------------------------- subcommands
def cmd_cutout(args: argparse.Namespace) -> None:
    in_dir, out_dir = Path(args.input), Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    files = collect(in_dir, args.set)
    if not files:
        sys.exit(f"{in_dir} に画像がありません（--set {args.set} で絞り込み中）" if args.set
                 else f"{in_dir} に画像がありません。")
    for p in files:
        img = remove_background(Image.open(p), tol=args.tol, min_area=args.min_area)
        img = trim(img)
        if not args.no_resize:
            img = fit_canvas(img, STICKER_SIZE, margin=args.margin)
        dst = out_dir / f"{p.stem}.png"
        size = save_png(img, dst)
        print(f"  {p.name} → {dst.name}  {img.width}x{img.height}  {size/1024:.0f}KB")
    print(f"✓ {len(files)}枚を {out_dir} に出力しました。")


def cmd_text(args: argparse.Namespace) -> None:
    in_dir, out_dir = Path(args.input), Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    font_path = find_font(args.font)
    files = collect(in_dir, args.set)
    if not files:
        sys.exit(f"{in_dir} に画像がありません。")
    texts = load_items(args.set) if args.set else {}
    W, H = STICKER_SIZE
    band_h = int(H * args.band)
    done = 0
    for p in files:
        no = parse_no(p)
        text = args.text or texts.get(no or -1)
        if not text:
            print(f"  skip {p.name}（セリフが特定できません）")
            continue
        img = trim(Image.open(p).convert("RGBA"))
        if args.position == "top":
            box = (args.margin, args.margin + band_h, W - args.margin, H - args.margin)
            band = (args.margin, args.margin, W - args.margin, args.margin + band_h)
        else:
            box = (args.margin, args.margin, W - args.margin, H - args.margin - band_h)
            band = (args.margin, H - args.margin - band_h, W - args.margin, H - args.margin)
        canvas = fit_canvas(img, STICKER_SIZE, margin=args.margin, box=box)
        draw_caption(canvas, text, font_path, band)
        size = save_png(canvas, out_dir / f"{p.stem}.png")
        print(f"  {p.name} 「{text}」  {size/1024:.0f}KB")
        done += 1
    print(f"✓ {done}枚にセリフを合成しました → {out_dir}")


def _make_aux(src: Path, size: tuple[int, int], dst: Path, margin: int) -> int:
    img = trim(remove_background(Image.open(src)))
    return save_png(fit_canvas(img, size, margin=margin), dst)


def default_package_input(set_id: str) -> Path:
    """セリフ合成済み(work/final)があればそちらを、無ければ work/cutout を使う。"""
    final = ROOT / "work/final"
    if final.is_dir() and collect(final, set_id):
        return final
    return ROOT / "work/cutout"


def cmd_package(args: argparse.Namespace) -> None:
    in_dir = Path(args.input) if args.input else default_package_input(args.set)
    out_dir = Path(args.output)
    print(f"入力: {in_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)
    files = collect(in_dir, args.set)
    numbered = sorted(((parse_no(p) or 0, p) for p in files), key=lambda t: t[0])
    if not numbered:
        sys.exit(f"{in_dir} にセット {args.set} の画像がありません。")
    if len(numbered) not in VALID_COUNTS and not args.force:
        sys.exit(f"スタンプは {VALID_COUNTS} 個のいずれかにしてください（今: {len(numbered)}個）。"
                 " どうしても通すなら --force。")

    stage = out_dir / f"_stage_{args.set.upper()}"
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)

    total = 0
    for idx, (_, p) in enumerate(numbered, start=1):
        img = Image.open(p).convert("RGBA")
        if img.size != STICKER_SIZE:
            img = fit_canvas(trim(img), STICKER_SIZE, margin=args.margin)
        total += save_png(img, stage / f"{idx:02d}.png")

    # メイン/タブ画像は、文字が乗っていない切り抜き版があればそちらを優先する
    first = numbered[0][1]
    plain = ROOT / "work/cutout" / first.name
    main_src = Path(args.main) if args.main else (plain if plain.exists() else first)
    tab_src = Path(args.tab) if args.tab else main_src
    total += _make_aux(main_src, MAIN_SIZE, stage / "main.png", args.margin)
    total += _make_aux(tab_src, TAB_SIZE, stage / "tab.png", max(args.margin // 2, 2))

    zip_path = out_dir / (args.name or f"kuro-stickers-{args.set.upper()}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(stage.iterdir()):
            z.write(f, f.name)  # ZIP直下に置くこと（LINEの一括アップロード仕様）
    if not args.keep_stage:
        shutil.rmtree(stage)
    print(f"✓ {zip_path}  スタンプ{len(numbered)}枚 + main + tab  合計{total/1024/1024:.2f}MB")
    _report(validate_zip(zip_path))


def validate_zip(zip_path: Path) -> list[str]:
    errs: list[str] = []
    with zipfile.ZipFile(zip_path) as z:
        names = z.namelist()
        if any("/" in n for n in names):
            errs.append("ZIPの中にフォルダがあります。画像はZIP直下に置いてください。")
        stickers = sorted(n for n in names if re.fullmatch(r"\d{2}\.png", n))
        if len(stickers) not in VALID_COUNTS:
            errs.append(f"スタンプ枚数が {len(stickers)} 個です（{VALID_COUNTS} のいずれかに）。")
        for need in ("main.png", "tab.png"):
            if need not in names:
                errs.append(f"{need} がありません。")
        for n in names:
            if not n.lower().endswith(".png"):
                errs.append(f"{n}: PNG以外のファイルが入っています。")
                continue
            info = z.getinfo(n)
            with z.open(n) as fh:
                img = Image.open(fh).convert("RGBA")
                w, h, alpha_min = img.width, img.height, img.split()[3].getextrema()[0]
            if info.file_size > MAX_BYTES:
                errs.append(f"{n}: {info.file_size/1024:.0f}KB（1MB超）")
            if n == "main.png" and (w, h) != MAIN_SIZE:
                errs.append(f"{n}: {w}x{h}（{MAIN_SIZE[0]}x{MAIN_SIZE[1]} である必要あり）")
            elif n == "tab.png" and (w, h) != TAB_SIZE:
                errs.append(f"{n}: {w}x{h}（{TAB_SIZE[0]}x{TAB_SIZE[1]} である必要あり）")
            elif n in stickers:
                if w > STICKER_SIZE[0] or h > STICKER_SIZE[1]:
                    errs.append(f"{n}: {w}x{h}（最大370x320）")
                if w % 2 or h % 2:
                    errs.append(f"{n}: {w}x{h}（各辺を偶数に）")
            if alpha_min == 255:
                errs.append(f"{n}: 背景が透過していません。")
    return errs


def _report(errs: list[str]) -> None:
    if errs:
        print("✗ 要修正:")
        for e in errs:
            print(f"   - {e}")
    else:
        print("✓ LINEの規定チェック：問題なし")


def cmd_check(args: argparse.Namespace) -> None:
    errs = validate_zip(Path(args.zip))
    _report(errs)
    sys.exit(1 if errs else 0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("split", help="グリッド一覧画像を1コマずつに切り分ける")
    sp.add_argument("--sheet", required=True, help="Geminiが出した一覧画像")
    sp.add_argument("--set", required=True, help="A/B/C")
    sp.add_argument("--grid", default="3x3", help="列x行（既定 3x3）")
    sp.add_argument("--start", type=int, default=1, help="左上のコマの番号")
    sp.add_argument("--count", type=int, help="実際に描かれているコマ数（既定: 全部）")
    sp.add_argument("--inset", type=float, default=0.0, help="各コマの外周を削る割合（例 0.02）")
    sp.add_argument("--output", default=str(ROOT / "work/raw"))
    sp.set_defaults(func=cmd_split)

    c = sub.add_parser("cutout", help="背景を透過にして370x320に整える")
    c.add_argument("--input", default=str(ROOT / "work/raw"))
    c.add_argument("--output", default=str(ROOT / "work/cutout"))
    c.add_argument("--set", help="A/B/C/D（ファイル名の先頭で絞り込み）")
    c.add_argument("--tol", type=float, default=34.0, help="背景とみなす色の許容差（既定34）")
    c.add_argument("--min-area", type=int, default=64, help="これ以下の点ノイズを消す")
    c.add_argument("--margin", type=int, default=10)
    c.add_argument("--no-resize", action="store_true", help="切り抜くだけでリサイズしない")
    c.set_defaults(func=cmd_cutout)

    t = sub.add_parser("text", help="セリフを画像に合成する")
    t.add_argument("--input", default=str(ROOT / "work/cutout"))
    t.add_argument("--output", default=str(ROOT / "work/final"))
    t.add_argument("--set", help="A/B/C/D（prompts.json のセリフを使う）")
    t.add_argument("--text", help="全部に同じ文字を入れる場合")
    t.add_argument("--font", help="日本語フォントのパス")
    t.add_argument("--position", choices=("bottom", "top"), default="bottom")
    t.add_argument("--band", type=float, default=0.22, help="文字帯の高さ（画像比）")
    t.add_argument("--margin", type=int, default=10)
    t.set_defaults(func=cmd_text)

    p = sub.add_parser("package", help="連番にリネームして提出用ZIPを作る")
    p.add_argument("--input", default=None, help="既定: work/final があればそれ、無ければ work/cutout")
    p.add_argument("--output", default=str(ROOT / "dist"))
    p.add_argument("--set", required=True, help="A/B/C/D")
    p.add_argument("--main", help="メイン画像の元ファイル（既定: 1番目のスタンプ）")
    p.add_argument("--tab", help="タブ画像の元ファイル（既定: メインと同じ）")
    p.add_argument("--name", help="ZIPのファイル名")
    p.add_argument("--margin", type=int, default=10)
    p.add_argument("--force", action="store_true", help="枚数チェックを無視する")
    p.add_argument("--keep-stage", action="store_true", help="ZIP前の画像フォルダを残す")
    p.set_defaults(func=cmd_package)

    k = sub.add_parser("check", help="ZIPがLINEの規定を満たすか確認する")
    k.add_argument("zip")
    k.set_defaults(func=cmd_check)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
