#!/usr/bin/env python3
"""prompts/prompts.json から Gemini に貼り付けるプロンプト集(Markdown)を生成する。

    python3 scripts/gen_prompts.py                # 3x3グリッド（既定）
    python3 scripts/gen_prompts.py --grid 2x2     # 1枚あたり4コマ（画質重視）
    python3 scripts/gen_prompts.py --grid 4x4     # 1セット＝1枚（16コマ）
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "prompts" / "prompts.json"

BG_JA = "淡いミントグリーンの単色"
BG_EN = "a flat pale mint green"

# ------------------------------------------------------------------ 同一性ロック
IDENTITY_JA = """添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）"""

IDENTITY_EN = """Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)"""


def rules_ja(cols: int, rows: int, n: int, blanks: int) -> str:
    lines = [
        f"・{n}個を{cols}×{rows}のグリッド一覧画像にし、左上から右下へこの順で配置する",
        "・必ず全身を描く。体の一部がコマの外で切れないようにする",
        "・コマとコマの間に枠線・区切り線・番号を描かない",
        "・背景に物や風景を描かない（切り抜いて使うため）",
        "・影・地面・グラデーション・模様を描かない",
        "・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない",
        "・小物（湯のみ・カバン・財布など）は淡い色で小さく、キャラクターの顔に重ならないように描く",
    ]
    if blanks:
        lines.insert(1, f"・右下の{blanks}コマは何も描かず、背景色のまま空けておく")
    return "\n".join(lines)


def rules_en(cols: int, rows: int, n: int, blanks: int) -> str:
    lines = [
        f"- Lay out {n} illustrations as a {cols} x {rows} grid sheet, in this order from top-left to bottom-right",
        "- Always draw the full body; never let any part be cut off by the edge of its cell",
        "- No panel borders, dividing lines or numbers between the cells",
        "- No objects and no scenery in the background (the art will be cut out later)",
        "- No shadows, no ground, no gradients, no patterns",
        "- No text and no numbers anywhere. Do not write any of the words used below",
        "- Keep props small and pale so they never cover the character",
    ]
    if blanks:
        lines.insert(1, f"- Leave the last {blanks} cells at the bottom right empty, background color only")
    return "\n".join(lines)


def grid_prompt_ja(items, cols, rows, first, last) -> str:
    n = len(items)
    blanks = cols * rows - n
    poses = "\n".join(f"・「{it['text']}」… {it['pose']}" for it in items)
    return (
        f"{IDENTITY_JA}\n\n"
        f"【必ず守ること】\n{rules_ja(cols, rows, n, blanks)}\n\n"
        f"【ポーズ】\n{poses}\n\n"
        f"背景は{BG_JA}。正方形。できるだけ高解像度で出力してください。"
    )


def grid_prompt_en(items, cols, rows) -> str:
    n = len(items)
    blanks = cols * rows - n
    poses = "\n".join(f"- \"{it['text']}\" ... {it['pose_en']}" for it in items)
    return (
        f"{IDENTITY_EN}\n\n"
        f"MUST FOLLOW:\n{rules_en(cols, rows, n, blanks)}\n\n"
        f"POSES:\n{poses}\n\n"
        f"Background: {BG_EN}, flat. Square canvas. Output at the highest resolution available."
    )


def single_prompt_ja(item) -> str:
    return (
        f"{IDENTITY_JA}\n\n"
        "【必ず守ること】\n"
        "・キャラクターは1体だけ。グリッドや複数バリエーションにしない\n"
        "・必ず全身を描く。体の一部が画面の外で切れないようにする\n"
        "・背景に物や風景を描かない（切り抜いて使うため）\n"
        "・影・地面・グラデーション・模様を描かない\n"
        "・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない\n\n"
        f"【ポーズ】\n{item['pose']}\n\n"
        f"背景は{BG_JA}。正方形。キャラクターは中央に、四辺に余白をあけて描く。"
    )


def single_prompt_en(item) -> str:
    return (
        f"{IDENTITY_EN}\n\n"
        "MUST FOLLOW:\n"
        "- Exactly one character. Not a grid, not multiple variations\n"
        "- Always draw the full body, never cut off by the edge of the canvas\n"
        "- No objects and no scenery in the background (the art will be cut out later)\n"
        "- No shadows, no ground, no gradients, no patterns\n"
        "- No text and no numbers anywhere\n\n"
        f"POSE: {item['pose_en']}\n\n"
        f"Background: {BG_EN}, flat. Square canvas, character centered with margins on all sides."
    )


def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", default="3x3", help="1枚あたりのコマ数（既定 3x3）")
    args = ap.parse_args()
    cols, rows = (int(v) for v in args.grid.lower().split("x"))
    per = cols * rows

    data = json.loads(DATA.read_text(encoding="utf-8"))
    out_dir = ROOT / "prompts"
    index = [
        "# Gemini プロンプト集",
        "",
        f"各セットを **{cols}×{rows}のグリッド一覧画像**でまとめて生成するプロンプトです。",
        "Gemini に **参考画像 `reference/character.png` を毎回添付**してください。",
        "",
    ]

    for s in data["sets"]:
        items = s["items"]
        sheets = list(chunks(items, per))
        lines = [
            f"# セット{s['id']}：{s['title']}（{s['slug']}）",
            "",
            s["concept"],
            "",
            "## 作り方",
            "",
            "1. Gemini に `reference/character.png` を添付する",
            f"2. 下の「シート1」のプロンプトを貼って{cols}×{rows}の一覧画像を出す",
            f"3. できた画像を `work/sheets/{s['id']}-sheet1.png` として保存する",
            "4. 一覧画像を1コマずつに切り分ける",
            "",
            "```bash",
            f"python3 scripts/stickerkit.py split --sheet work/sheets/{s['id']}-sheet1.png \\",
            f"    --set {s['id']} --grid {cols}x{rows} --start 1",
            "```",
            "",
            "5. 残りのシートも同じように（`--start` の数字を変える）",
            "6. 崩れたコマだけ、下の「1枚ずつ描き直す用」で描き直して "
            f"`work/raw/{s['id']}-xx.png` を上書きする",
            f"7. `cutout --set {s['id']}` → `text --set {s['id']}` → `package --set {s['id']}`",
            "",
            "---",
            "",
        ]

        start = 1
        for si, sheet in enumerate(sheets, start=1):
            first, last = start, start + len(sheet) - 1
            blanks = per - len(sheet)
            lines += [
                f"## シート{si}（{s['id']}-{first:02d} 〜 {s['id']}-{last:02d}／{len(sheet)}コマ）",
                "",
                f"- 保存先: `work/sheets/{s['id']}-sheet{si}.png`",
                f"- 切り分け: `python3 scripts/stickerkit.py split "
                f"--sheet work/sheets/{s['id']}-sheet{si}.png --set {s['id']} "
                f"--grid {cols}x{rows} --start {first}`",
            ]
            if blanks:
                lines.append(f"- このシートは{len(sheet)}コマだけで、右下の{blanks}コマは空にします")
            lines += [
                "",
                "```text",
                grid_prompt_ja(sheet, cols, rows, first, last),
                "```",
                "",
                "<details><summary>English version</summary>",
                "",
                "```text",
                grid_prompt_en(sheet, cols, rows),
                "```",
                "",
                "</details>",
                "",
                "| コマ | セリフ | ファイル名 |",
                "|---|---|---|",
            ]
            for i, it in enumerate(sheet):
                lines.append(f"| {i+1} | {it['text']} | `{s['id']}-{start+i:02d}.png` |")
            lines += ["", "---", ""]
            start = last + 1

        lines += ["## 1枚ずつ描き直す用", "",
                  "グリッドで崩れたコマだけ、これで単体生成して差し替えてください。", ""]
        for it in items:
            fid = f"{s['id']}-{it['no']:02d}"
            lines += [
                f"<details><summary><b>{fid}「{it['text']}」</b> … {it['pose']}</summary>",
                "",
                "```text",
                single_prompt_ja(it),
                "```",
                "",
                "```text",
                single_prompt_en(it),
                "```",
                "",
                "</details>",
                "",
            ]

        path = out_dir / f"set-{s['id'].lower()}_{s['slug']}.md"
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}  （シート{len(sheets)}枚）")
        index.append(
            f"- [セット{s['id']}：{s['title']}]({path.name})"
            f" — {len(items)}個／シート{len(sheets)}枚　{s['concept']}"
        )

    index += [
        "",
        "## グリッドか、1枚ずつか",
        "",
        f"- **グリッド（{cols}×{rows}）**… 絵柄が揃いやすく、生成回数が少なくて済みます。まずこちらで。",
        "  1コマあたりの解像度が下がるので、Geminiの出力は**いちばん大きいサイズ**を選んでください。",
        "- **1枚ずつ**… 解像度と細部が安定します。グリッドで崩れたコマの描き直しに。",
        "",
        "```bash",
        "python3 scripts/gen_prompts.py --grid 2x2   # 1枚4コマ（画質重視・4シート）",
        "python3 scripts/gen_prompts.py --grid 4x4   # 1セット1枚（16コマ・手間重視）",
        "```",
        "",
        "## 文字（セリフ）について",
        "",
        "画像生成AIは日本語を崩しがちなので、**絵は文字なしで作り、",
        "セリフは後から `stickerkit.py text` で合成する**設計にしています。",
        "プロンプトにも「文字を一切描かない」と明記済みです。",
    ]
    (out_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print("wrote prompts/README.md")


if __name__ == "__main__":
    main()
