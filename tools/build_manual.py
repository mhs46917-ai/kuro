#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""マニュアルのMarkdownとPDFを生成する。

    python3 tools/build_manual.py pool-hair-catcher   # 1件
    python3 tools/build_manual.py --all               # manuals/ 配下すべて
"""
import argparse
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import manual_builder  # noqa: E402

REPO = manual_builder.REPO
MANUALS_DIR = os.path.join(REPO, "manuals")


def load(slug):
    path = os.path.join(MANUALS_DIR, slug.replace("-", "_") + ".py")
    if not os.path.exists(path):
        sys.exit(f"定義ファイルがありません: {path}")
    spec = importlib.util.spec_from_file_location("manual_def", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.MANUAL


def all_slugs():
    return sorted(f[:-3].replace("_", "-") for f in os.listdir(MANUALS_DIR)
                  if f.endswith(".py") and not f.startswith("_"))


def build(slug, skip_pdf=False):
    manual = load(slug)
    for w in manual_builder.validate(manual):
        print(f"  [警告] {w}")
    md = manual_builder.build_markdown(manual)
    print(f"  Markdown: {os.path.relpath(md, REPO)}")
    if not skip_pdf:
        pdf = manual_builder.build_pdf(manual)
        size = os.path.getsize(pdf) // 1024
        print(f"  PDF     : {os.path.relpath(pdf, REPO)} ({size} KB)")


def main():
    ap = argparse.ArgumentParser(description="マニュアルのMD/PDFを生成する")
    ap.add_argument("slug", nargs="?", help="manuals/<slug>.py のスラッグ")
    ap.add_argument("--all", action="store_true", help="すべてのマニュアルを生成")
    ap.add_argument("--list", action="store_true", help="マニュアル一覧を表示")
    ap.add_argument("--no-pdf", action="store_true", help="Markdownのみ生成")
    args = ap.parse_args()

    if args.list:
        for s in all_slugs():
            print(s)
        return
    targets = all_slugs() if args.all else ([args.slug] if args.slug else [])
    if not targets:
        ap.error("スラッグを指定するか --all を付けてください（一覧は --list）")
    for slug in targets:
        print(f"● {slug}")
        build(slug, args.no_pdf)


if __name__ == "__main__":
    main()
