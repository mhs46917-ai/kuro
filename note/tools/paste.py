"""note貼り付け用テキストを作る。使い方: python3 note/tools/paste.py 記事.md [記事.md ...]"""
import re
import sys
from pathlib import Path

for arg in sys.argv[1:]:
    src = Path(arg)
    s = src.read_text(encoding="utf-8")
    s = re.sub(r"\A---\n.*?\n---\n", "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"^#\s*本文\s*$", "", s, flags=re.M)
    s = re.sub(r"^#+\s+", "", s, flags=re.M)
    s = re.sub(r"^---$", "", s, flags=re.M)
    s = re.sub(r"\n{3,}", "\n\n", s).strip() + "\n"
    out = src.with_name(src.stem + "-paste.txt")
    out.write_text(s, encoding="utf-8")
    print(f"{out}  {len(s.replace(chr(10), ''))}字")
