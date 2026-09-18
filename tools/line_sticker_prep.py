#!/usr/bin/env python3
"""
LINEスタンプ提出用データへの一括変換ツール。

生成AI(Gemini等)が出した画像を、LINE Creators Market の提出規定に合わせて
まとめて整形する。3x3などのグリッド画像も、個別画像も入力にできる。

やること:
  1. 背景の除去（縁から連結した背景色を塗り分けて透過）
  2. 文字や飛び散った効果線などの孤立パーツを除去（最大の連結成分だけ残す）
  3. 白背景で輪郭が飛ぶ問題への対処（外側の縁取り + 距離0のソフトシャドウ）
  4. 余白10pxを確保して 370x320 に収める
  5. 01.png 〜 40.png / main.png(240x240) / tab.png(96x74) を書き出し

使い方:
  # 3x3グリッド1枚から9個を切り出す
  python3 tools/line_sticker_prep.py grid.png -o out --grid 3x3

  # 個別画像をまとめて処理する
  python3 tools/line_sticker_prep.py imgs/*.png -o out

  # 縁取りを濃くしたい / 外したい
  python3 tools/line_sticker_prep.py grid.png -o out --grid 3x3 --outline-width 4
  python3 tools/line_sticker_prep.py grid.png -o out --grid 3x3 --no-outline
"""

import argparse
import glob
import os
import sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

# LINE Creators Market の提出規定
STICKER_W, STICKER_H = 370, 320
MAIN_SIZE = (240, 240)
TAB_SIZE = (96, 74)
MARGIN = 10  # 推奨される安全余白

# 白背景でキャラクターが沈まないようにする輪郭処理の既定値
OUTLINE_RGB = (154, 167, 176)   # #9AA7B0
OUTLINE_ALPHA = 153             # 60%
GLOW_RGB = (143, 165, 181)      # #8FA5B5
GLOW_ALPHA = 64                 # 25%
GLOW_BLUR = 8


def split_grid(img, cols, rows):
    w, h = img.size
    cw, ch = w / cols, h / rows
    for r in range(rows):
        for c in range(cols):
            yield img.crop((int(c * cw), int(r * ch), int((c + 1) * cw), int((r + 1) * ch)))


def remove_background(panel, tol):
    """縁から連結している背景色の領域だけを透過する。

    単純な色指定での塗り分けと違い、キャラクターの内側にある背景と同系色のパーツ
    （例: 水色のナイトキャップ）を巻き込まない。
    """
    a = np.asarray(panel.convert("RGB")).astype(np.int16)
    h, w = a.shape[:2]

    # 四隅のサンプルの中央値を背景色とみなす
    k = max(2, min(h, w) // 40)
    corners = np.concatenate([
        a[:k, :k].reshape(-1, 3), a[:k, -k:].reshape(-1, 3),
        a[-k:, :k].reshape(-1, 3), a[-k:, -k:].reshape(-1, 3),
    ])
    bg_color = np.median(corners, axis=0)

    dist = np.sqrt(((a - bg_color) ** 2).sum(axis=2))
    bg_like = dist < tol

    # 背景色に近い画素のうち、画像の縁につながっているものだけを背景と判定する
    lab, n = ndimage.label(bg_like)
    border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    border.discard(0)
    background = np.isin(lab, list(border)) if border else np.zeros_like(bg_like)

    return ~background


def drop_blue(panel, mask, threshold):
    """青が突出した画素をマスクから外す。

    生成画像には足元の接地影や背景のはみ出しが青いまま残りやすく、透過すると
    青い染みになる。逆に、意図して青いパーツ（ナイトキャップ等）を持つ絵では
    --drop-blue 0 で無効にすること。
    """
    a = np.asarray(panel.convert("RGB")).astype(np.int16)
    blueness = a[:, :, 2] - a[:, :, 0]
    return mask & (blueness <= threshold)


def keep_largest_blob(mask, min_ratio=0.02):
    """最大の連結成分だけを残す。焼き込まれた文字や離れた効果線がこれで落ちる。"""
    lab, n = ndimage.label(mask)
    if n == 0:
        return mask
    sizes = ndimage.sum(mask, lab, range(1, n + 1))
    keep = int(np.argmax(sizes)) + 1
    if sizes[keep - 1] < mask.size * min_ratio:
        return mask  # 主役が見つからないときは触らない
    return lab == keep


def add_outline(rgba, width, outline_rgb, outline_alpha, glow_rgb, glow_alpha, glow_blur):
    """外側の縁取りと距離0のソフトシャドウを敷いて、白背景でも輪郭が立つようにする。

    硬いベクター線を足すと手描きのタッチと喧嘩するため、縁取りは不透明度を落とし、
    その外側にぼかしたシャドウを重ねて「浮かせる」。
    """
    pad = width + glow_blur * 3
    w, h = rgba.size
    canvas = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    canvas.paste(rgba, (pad, pad))

    alpha = canvas.split()[3]
    layers = []

    if glow_alpha > 0:
        blurred = alpha.filter(ImageFilter.GaussianBlur(glow_blur))
        g = np.asarray(blurred).astype(np.uint16) * glow_alpha // 255
        glow = Image.new("RGBA", canvas.size, glow_rgb + (0,))
        glow.putalpha(Image.fromarray(g.astype(np.uint8)))
        layers.append(glow)

    if width > 0:
        grown = alpha.filter(ImageFilter.MaxFilter(width * 2 + 1))
        o = np.asarray(grown).astype(np.uint16) * outline_alpha // 255
        outline = Image.new("RGBA", canvas.size, outline_rgb + (0,))
        outline.putalpha(Image.fromarray(o.astype(np.uint8)))
        layers.append(outline)

    out = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    for layer in layers:
        out = Image.alpha_composite(out, layer)
    return Image.alpha_composite(out, canvas)


def fit_canvas(rgba, size, margin):
    """内容を切り詰めて、余白を確保したうえで規定サイズの中央に置く。"""
    bbox = rgba.split()[3].getbbox()
    if bbox:
        rgba = rgba.crop(bbox)
    tw, th = size[0] - margin * 2, size[1] - margin * 2
    scale = min(tw / rgba.width, th / rgba.height)
    new = rgba.resize((max(1, round(rgba.width * scale)),
                       max(1, round(rgba.height * scale))), Image.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    canvas.paste(new, ((size[0] - new.width) // 2, (size[1] - new.height) // 2), new)
    return canvas


def process(panel, args):
    mask = remove_background(panel, args.tolerance)
    if args.drop_blue > 0:
        mask = drop_blue(panel, mask, args.drop_blue)
    if not args.keep_all:
        mask = keep_largest_blob(mask)

    rgba = panel.convert("RGBA")
    alpha = Image.fromarray((mask * 255).astype(np.uint8))
    # 1pxだけぼかして、切り抜き境界のギザつきを抑える
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))
    rgba.putalpha(alpha)

    if args.outline_width > 0 or args.glow_alpha > 0:
        rgba = add_outline(rgba, args.outline_width, OUTLINE_RGB, args.outline_alpha,
                           GLOW_RGB, args.glow_alpha, args.glow_blur)
    return fit_canvas(rgba, (STICKER_W, STICKER_H), args.margin)


def main():
    p = argparse.ArgumentParser(description="生成画像をLINEスタンプ提出用データに一括変換する")
    p.add_argument("inputs", nargs="+", help="入力画像（グリッド1枚でも個別複数枚でも可）")
    p.add_argument("-o", "--outdir", default="line_out", help="出力先ディレクトリ")
    p.add_argument("--grid", help="入力がグリッド画像のときの分割数（例: 3x3）")
    p.add_argument("--tolerance", type=float, default=40.0,
                   help="背景色とみなす色距離。背景が残るなら上げ、キャラが欠けるなら下げる")
    p.add_argument("--margin", type=int, default=MARGIN, help="確保する安全余白(px)")
    p.add_argument("--drop-blue", type=int, default=18,
                   help="青が突出した画素を落とす閾値(B-R)。接地影の除去用。"
                        "意図して青いパーツがある絵では 0 にする")
    p.add_argument("--outline-width", type=int, default=3, help="縁取りの太さ(px)。0で無効")
    p.add_argument("--outline-alpha", type=int, default=OUTLINE_ALPHA, help="縁取りの不透明度(0-255)")
    p.add_argument("--glow-alpha", type=int, default=GLOW_ALPHA, help="ソフトシャドウの不透明度(0-255)")
    p.add_argument("--glow-blur", type=int, default=GLOW_BLUR, help="ソフトシャドウのぼかし量(px)")
    p.add_argument("--no-outline", action="store_true", help="縁取りとシャドウを一切足さない")
    p.add_argument("--keep-all", action="store_true",
                   help="孤立パーツを消さない（効果線を残したいときに使う）")
    args = p.parse_args()

    if args.no_outline:
        args.outline_width, args.glow_alpha = 0, 0

    paths = []
    for pattern in args.inputs:
        paths.extend(sorted(glob.glob(pattern)) or [pattern])

    panels = []
    for path in paths:
        if not os.path.exists(path):
            sys.exit(f"見つかりません: {path}")
        img = Image.open(path)
        if args.grid:
            cols, rows = (int(v) for v in args.grid.lower().split("x"))
            panels.extend(split_grid(img, cols, rows))
        else:
            panels.append(img)

    os.makedirs(args.outdir, exist_ok=True)
    results = []
    for i, panel in enumerate(panels, 1):
        out = process(panel, args)
        name = os.path.join(args.outdir, f"{i:02d}.png")
        out.save(name)
        results.append(out)
        print(f"  {name}  {out.size[0]}x{out.size[1]}")

    if results:
        fit_canvas(results[0], MAIN_SIZE, 6).save(os.path.join(args.outdir, "main.png"))
        fit_canvas(results[0], TAB_SIZE, 4).save(os.path.join(args.outdir, "tab.png"))
        print(f"  {args.outdir}/main.png  240x240")
        print(f"  {args.outdir}/tab.png   96x74")

    n = len(results)
    if n not in (8, 16, 24, 32, 40):
        print(f"\n注意: {n}個です。LINEの提出は 8/16/24/32/40 個のいずれかである必要があります。")


if __name__ == "__main__":
    main()
