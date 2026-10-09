#!/usr/bin/env python3
"""ちび系キャラのREADME（編集用テンプレート＋36個の表）から、
Geminiにそのまま貼れる1枚ずつのプロンプトを組み立てる。

出力:
  docs/<キャラ>/prompts.md  … 36個ぶんのコピペ用プロンプト
  --json PATH を付けると、全キャラ分をJSONでも書き出す（コピー用ページの元データ）
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHARACTERS = [
    ("chibi-hamster", "hamster"),
    ("chibi-kobuta", "kobuta"),
    ("chibi-shirobunchou", "bunchou"),
    ("chibi-nikuman", "nikuman"),
    ("onigiri-zeki", "onigiri"),
]

# 体にかぶせる・巻く小物は「キャラクターに重ねない」と矛盾するので注記を外す
WRAP_WORDS = re.compile(r"かける|かぶ|巻く|入れる|帽|くるま|つもる|突起")


def read_template(text):
    m = re.search(r"## 編集用テンプレート.*?```\n(.*?)```", text, re.S)
    return m.group(1).rstrip("\n")


def read_pack(text):
    title = re.search(r"^## パック1：(.+?)（", text, re.M).group(1)
    rows = []
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0].isdigit():
            rows.append(dict(zip(("no", "word", "face", "arm", "extra"), cells)))
    rows.sort(key=lambda r: int(r["no"]))
    return title, rows


def fill(template, row):
    out = []
    for line in template.splitlines():
        if "(表情)" in line:
            if row["face"] == "変えない":
                line = line.split(":")[0] + ":変えない"
            else:
                line = line.replace("(表情)", row["face"])
        elif "(腕)" in line:
            if row["arm"] == "変えない":
                line = line.split(":")[0] + ":変えない"
            else:
                line = line.replace("(腕)", row["arm"])
        elif "(追加)" in line:
            if row["extra"] == "なし":
                line = line.split(":")[0] + ":なし"
            elif WRAP_WORDS.search(row["extra"]):
                line = line.split(":")[0] + ":" + row["extra"]
            else:
                line = line.replace("(追加)", row["extra"])
        line = line.replace("(言葉)", row["word"])
        out.append(line)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="全キャラ分のJSONの書き出し先")
    args = ap.parse_args()

    data = []
    for folder, key in CHARACTERS:
        readme = (ROOT / "docs" / folder / "README.md").read_text(encoding="utf-8")
        name = re.match(r"# (.+?)（", readme).group(1)
        template = read_template(readme)
        pack, rows = read_pack(readme)
        assert rows, folder
        ref = next(p.name for p in sorted((ROOT / "docs" / folder).glob("ref_edit_base.*")))
        items = [
            {**r, "file": f"{key}_{int(r['no']):02d}.jpg", "prompt": fill(template, r)}
            for r in rows
        ]
        data.append({"key": key, "folder": folder, "name": name, "pack": pack, "ref": ref, "items": items})

        md = [
            f"# {name}【{pack}】 Gemini用プロンプト（1枚ずつ）",
            "",
            "`tools/build_chibi_prompts.py` でREADMEから自動生成。表を直したら再生成する。",
            "",
            f"- 毎回新しいチャットに `docs/{folder}/{ref}` だけを添付し、1つ貼る",
            "- 保存名は各見出しの右のファイル名にそろえると、後処理で番号順に並べやすい",
            "",
        ]
        for it in items:
            md += [f"## {it['no']}. {it['word']}　→ `{it['file']}`", "", "```", it["prompt"], "```", ""]
        (ROOT / "docs" / folder / "prompts.md").write_text("\n".join(md), encoding="utf-8")

    if args.json:
        Path(args.json).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
