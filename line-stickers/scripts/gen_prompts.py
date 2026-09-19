#!/usr/bin/env python3
"""prompts/prompts.json から Gemini に貼り付けるプロンプト集(Markdown)を生成する。

使い方:
    python3 scripts/gen_prompts.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "prompts" / "prompts.json"

STYLE_JA = """添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない"""

STYLE_EN = """Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark."""


def build_prompt(pose: str, text: str) -> str:
    return (
        f"{STYLE_JA}\n\n"
        f"【今回のポーズ・表情】\n{pose}\n\n"
        f"（※このスタンプに乗せる予定のセリフは「{text}」です。"
        f"セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）"
    )


def build_prompt_en(pose_en: str, text: str) -> str:
    return (
        f"{STYLE_EN}\n\n"
        f"Pose and expression: {pose_en}.\n"
        f"(This sticker will later carry the Japanese caption \"{text}\" added in post - "
        f"match the mood, but do not draw any text.)"
    )


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    out_dir = ROOT / "prompts"

    index = ["# Gemini プロンプト集", "", "各ファイルの本文をそのまま Gemini に貼り付け、", 
             "**参考画像 `reference/character.png` を毎回添付**してください。", ""]

    for s in data["sets"]:
        lines = [
            f"# セット{s['id']}：{s['title']}（{s['slug']}）",
            "",
            s["concept"],
            "",
            "## 使い方",
            "",
            "1. Gemini に `reference/character.png` を添付する",
            "2. 下の各プロンプトを1つずつ貼って生成する（1枚ずつ作るのが一番ブレません）",
            f"3. 気に入った画像を `work/raw/{s['id']}-01.png` 〜 "
            f"`work/raw/{s['id']}-{len(s['items']):02d}.png` の名前で保存する（番号が並び順になります）",
            f"4. `python3 scripts/stickerkit.py cutout --set {s['id']}` → "
            f"`text --set {s['id']}` → `package --set {s['id']}` でZIPまで作る",
            "",
            "## 共通スタイル（各プロンプトに含まれています）",
            "",
            "```text",
            STYLE_JA,
            "```",
            "",
            "---",
            "",
        ]

        for it in s["items"]:
            fid = f"{s['id']}-{it['no']:02d}"
            lines += [
                f"## {fid}　「{it['text']}」",
                "",
                f"- ポーズ: {it['pose']}",
                f"- 保存ファイル名: `work/raw/{fid}.png`",
                "",
                "<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>",
                "",
                "```text",
                build_prompt(it["pose"], it["text"]),
                "```",
                "",
                "</details>",
                "",
                "<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>",
                "",
                "```text",
                build_prompt_en(it["pose_en"], it["text"]),
                "```",
                "",
                "</details>",
                "",
            ]

        path = out_dir / f"set-{s['id'].lower()}_{s['slug']}.md"
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
        index.append(f"- [セット{s['id']}：{s['title']}]({path.name}) — {s['concept']}")

    index += [
        "",
        "## 文字（セリフ）について",
        "",
        "画像生成AIは日本語の文字を崩しがちなので、**絵は文字なしで作り、",
        "セリフは後から `stickerkit.py text` で合成する**のがおすすめです。",
        "",
        "```bash",
        "python3 scripts/stickerkit.py text --set A          # work/cutout の画像にセリフを焼き込む",
        "```",
        "",
        "Gemini に文字ごと描かせたい場合は、各プロンプトの最後の行を",
        "`画像の下部に丸ゴシック体で「〇〇」と大きく書いてください。` に差し替えてください",
        "（崩れやすいので、出来上がりは必ず目視チェックを）。",
    ]
    (out_dir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print("wrote prompts/README.md")


if __name__ == "__main__":
    main()
