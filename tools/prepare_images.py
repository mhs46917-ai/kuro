#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""現場写真を縮小・圧縮して docs/images/<slug>/ に連番で配置する。

    python3 tools/prepare_images.py pool-hair-catcher ~/Desktop/写真フォルダ

スマホ写真はそのままだと1枚10MB超になるため、幅1400px・JPEG品質82に変換する。
並び順は既定でファイル名順。--by-time を付けると撮影日時（EXIF）順になる。
出力は 01.jpg, 02.jpg ... で、定義ファイルに貼れる steps の雛形も表示する。
"""
import argparse
import os
import sys

from PIL import Image, ImageOps

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTS = (".jpg", ".jpeg", ".png", ".heic", ".webp")


def shot_time(path):
    try:
        exif = Image.open(path).getexif()
        return exif.get(36867) or exif.get(306) or ""
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser(description="写真を縮小して docs/images/<slug>/ に配置")
    ap.add_argument("slug")
    ap.add_argument("sources", nargs="+", help="写真フォルダ、または写真ファイル")
    ap.add_argument("--width", type=int, default=1400, help="最大幅px（既定1400）")
    ap.add_argument("--quality", type=int, default=82, help="JPEG品質（既定82）")
    ap.add_argument("--by-time", action="store_true", help="撮影日時順に並べる")
    ap.add_argument("--start", type=int, default=1, help="連番の開始（既定1）")
    args = ap.parse_args()

    files = []
    for src in args.sources:
        if os.path.isdir(src):
            files += [os.path.join(src, f) for f in os.listdir(src)
                      if f.lower().endswith(EXTS)]
        elif os.path.isfile(src):
            files.append(src)
        else:
            sys.exit(f"見つかりません: {src}")
    if not files:
        sys.exit("対象の画像がありません")

    files.sort(key=shot_time if args.by_time else (lambda p: os.path.basename(p).lower()))

    outdir = os.path.join(REPO, "docs", "images", args.slug)
    os.makedirs(outdir, exist_ok=True)

    names = []
    for i, src in enumerate(files, start=args.start):
        try:
            im = Image.open(src)
        except Exception as e:
            print(f"  [スキップ] {os.path.basename(src)}: {e}")
            continue
        im = ImageOps.exif_transpose(im).convert("RGB")  # 縦横の向きを正す
        w, h = im.size
        if w > args.width:
            im = im.resize((args.width, round(h * args.width / w)), Image.LANCZOS)
        name = f"{i:02d}.jpg"
        dst = os.path.join(outdir, name)
        im.save(dst, "JPEG", quality=args.quality, optimize=True)
        names.append(name)
        print(f"  {os.path.basename(src)} -> docs/images/{args.slug}/{name} "
              f"({os.path.getsize(dst) // 1024} KB)")

    print(f"\n{len(names)}枚を配置しました。定義ファイルの steps 雛形:\n")
    for name in names:
        print('        {')
        print('            "title": "",')
        print('            "lines": [')
        print('                "",')
        print('            ],')
        print(f'            "image": "{name}",')
        print('        },')


if __name__ == "__main__":
    main()
