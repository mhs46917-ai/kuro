#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新しいマニュアルの定義ファイルを雛形から作る。

    python3 tools/new_manual.py ろ過器逆洗 --slug backwash --steps 12
"""
import argparse
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE = '''# -*- coding: utf-8 -*-
"""{title} マニュアル定義。

画像は docs/images/{slug}/ に置く（tools/prepare_images.py で縮小・連番化できる）。
ビルド: python3 tools/build_manual.py {slug}
"""

MANUAL = {{
    "slug": "{slug}",
    "title": "{title}",
    "subtitle": "",
    "author": "株式会社ウェルアップ",
    "meta": [
        ["作業名", "{title}"],
        ["対象設備", ""],
        ["作業区分", ""],
        ["想定作業人数", "1〜2名"],
        ["改訂日", "{today}"],
    ],
    "purpose": "",

    # 頻度表が不要なマニュアルでは "frequency" ごと削除してよい
    "frequency": {{
        "columns": ["区分", "頻度", "実施日"],
        "widths": [0.20, 0.16, 0.64],
        "rows": [
            ["通常", "", ""],
        ],
    }},

    "preparation": [
        "保護具：",
        "工具・用具：",
    ],
    "safety": [
        "",
    ],

    # 手順。番号（①②③…）は並び順から自動で付く
    "steps": [
{steps}    ],

    "checklist": [
        "",
    ],
    "record_columns": ["実施日", "実施者", "状態", "特記事項"],
    "record_rows": 5,
}}
'''

STEP = '''        {{
            "title": "",
            "lines": [
                "",
            ],
            "image": "{image}",
        }},
'''


def main():
    ap = argparse.ArgumentParser(description="マニュアル定義の雛形を作る")
    ap.add_argument("title", help="マニュアルのタイトル（日本語可）")
    ap.add_argument("--slug", required=True, help="英数字のスラッグ 例: backwash")
    ap.add_argument("--steps", type=int, default=10, help="手順数（既定10）")
    args = ap.parse_args()

    from datetime import date
    path = os.path.join(REPO, "manuals", args.slug.replace("-", "_") + ".py")
    if os.path.exists(path):
        sys.exit(f"すでに存在します: {path}")

    steps = "".join(STEP.format(image=f"{i:02d}.jpg") for i in range(1, args.steps + 1))
    body = TEMPLATE.format(title=args.title, slug=args.slug,
                           today=date.today().isoformat(), steps=steps)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    os.makedirs(os.path.join(REPO, "docs", "images", args.slug), exist_ok=True)

    print(f"作成しました: {os.path.relpath(path, REPO)}")
    print(f"写真置き場  : docs/images/{args.slug}/")
    print("次の手順:")
    print(f"  1. python3 tools/prepare_images.py {args.slug} <写真フォルダ>")
    print(f"  2. {os.path.relpath(path, REPO)} に手順の文章を書く")
    print(f"  3. python3 tools/build_manual.py {args.slug}")


if __name__ == "__main__":
    main()
