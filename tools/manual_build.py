#!/usr/bin/env python3
"""業務マニュアルの定義ファイル(YAML)から、配布用マニュアルを生成する。

使い方の例:
    python3 tools/manual_build.py --new manuals/受注処理.yaml   # ひな形を作る
    python3 tools/manual_build.py manuals/受注処理.yaml          # HTML を生成
    python3 tools/manual_build.py manuals/受注処理.yaml --format md

生成した HTML はブラウザで開き「印刷 → PDF に保存」で A4 の PDF になる。
画像は base64 で埋め込むため、HTML 1 ファイルだけで配布できる。
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import mimetypes
import sys
from pathlib import Path

import yaml

TEMPLATE = """\
# 業務マニュアル定義ファイル
# 必要な項目だけ残して自由に編集してください。空欄の項目は出力されません。

title: {title}
document_no: MN-001
version: "1.0"
department: 
author: 
effective_date: {today}

purpose: |
  この手順書の目的を書きます（何のための業務か、何が達成できれば完了か）。

scope: |
  対象者・対象業務の範囲を書きます。

terms:
  - term: 用語
    definition: 用語の説明

revisions:
  - version: "1.0"
    date: {today}
    author: 
    summary: 初版作成

sections:
  - title: 事前準備
    description: この章で行うことの概要。
    steps:
      - title: 必要なものを揃える
        detail: |
          具体的な操作を書きます。箇条書きにしたい場合は
          - のように行頭にハイフンを置きます。
        role: 担当者
        system: 対象システム名
        note: 補足事項があれば書きます。
        warning: 特に注意すべき点があれば書きます。
        checks:
          - 完了判定の条件を書きます

  - title: 本手続き
    steps:
      - title: 手順のタイトル
        detail: 手順の内容。
        # image: images/screen01.png   # 画像を載せる場合

faq:
  - q: よくある質問
    a: その回答

contacts:
  - name: 担当部署 / 担当者
    role: 問い合わせ内容
    contact: 内線・メールなど
"""

CSS = """
:root { --ink:#1c1c1c; --muted:#5f6b7a; --line:#d9dee5; --accent:#1f4e79;
        --warn-bg:#fff4f2; --warn-line:#d1453b; --note-bg:#f1f6fb; --note-line:#1f4e79; }
* { box-sizing: border-box; }
body { margin:0; color:var(--ink); background:#f4f5f7;
       font-family:"Hiragino Kaku Gothic ProN","Yu Gothic","Meiryo",system-ui,sans-serif;
       line-height:1.75; font-size:15px; }
.sheet { max-width:900px; margin:0 auto; background:#fff; padding:48px 56px;
         box-shadow:0 1px 3px rgba(0,0,0,.08); }
h1 { font-size:26px; margin:0 0 8px; letter-spacing:.02em; }
h2 { font-size:19px; margin:40px 0 12px; padding:8px 12px; background:var(--accent);
     color:#fff; border-radius:3px; }
h3 { font-size:16px; margin:24px 0 8px; }
p { margin:.5em 0; }
.meta { display:flex; flex-wrap:wrap; gap:6px 24px; color:var(--muted); font-size:13px;
        border-bottom:2px solid var(--accent); padding-bottom:16px; margin-bottom:8px; }
.meta b { color:var(--ink); font-weight:600; }
.block { margin:28px 0; }
.block > .label { font-weight:600; font-size:14px; color:var(--accent); margin-bottom:4px; }
table { border-collapse:collapse; width:100%; font-size:14px; margin:8px 0 4px; }
th, td { border:1px solid var(--line); padding:7px 10px; text-align:left; vertical-align:top; }
th { background:#eef2f6; font-weight:600; white-space:nowrap; }
ol.toc { columns:2; font-size:14px; padding-left:1.4em; }
ol.toc a { color:var(--ink); text-decoration:none; }
ol.toc a:hover { text-decoration:underline; }
.step { border:1px solid var(--line); border-radius:4px; padding:14px 16px; margin:12px 0;
        page-break-inside:avoid; }
.step-head { display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; }
.step-no { background:var(--accent); color:#fff; font-size:13px; font-weight:700;
           border-radius:3px; padding:2px 9px; white-space:nowrap; }
.step-title { font-weight:600; font-size:16px; }
.tags { margin-left:auto; display:flex; gap:6px; flex-wrap:wrap; }
.tag { font-size:12px; color:var(--muted); border:1px solid var(--line);
       border-radius:10px; padding:1px 9px; background:#fafbfc; }
.detail { margin:8px 0 0; }
.detail ul { margin:.3em 0; padding-left:1.3em; }
.callout { border-left:4px solid; padding:8px 12px; margin:10px 0; font-size:14px;
           border-radius:0 3px 3px 0; }
.callout.note { background:var(--note-bg); border-color:var(--note-line); }
.callout.warn { background:var(--warn-bg); border-color:var(--warn-line); }
.callout .label { font-weight:600; margin-right:.4em; }
.checks { margin:10px 0 0; padding:0; list-style:none; font-size:14px; }
.checks li { padding-left:1.6em; position:relative; }
.checks li::before { content:"☐"; position:absolute; left:.2em; color:var(--accent); }
figure { margin:12px 0 0; }
figure img { max-width:100%; border:1px solid var(--line); border-radius:3px; }
figcaption { font-size:12px; color:var(--muted); margin-top:4px; }
footer { margin-top:48px; padding-top:14px; border-top:1px solid var(--line);
         font-size:12px; color:var(--muted); }
@media print {
  body { background:#fff; font-size:11pt; }
  .sheet { box-shadow:none; max-width:none; padding:0; }
  h2 { page-break-after:avoid; }
  @page { size:A4; margin:18mm 15mm; }
}
@media (max-width:640px) { .sheet { padding:24px 18px; } ol.toc { columns:1; } }
"""


# ---------------------------------------------------------------- 変換ヘルパー

def esc(value) -> str:
    return html.escape("" if value is None else str(value))


def rich_text(text) -> str:
    """本文テキストを段落・箇条書きの HTML に変換する。

    連続する行は 1 つの段落にまとめ、空行で段落を分ける。行頭が "- " などの
    行は箇条書きとして扱う。
    """
    if text is None:
        return ""
    blocks: list[str] = []
    bullets: list[str] = []
    paragraph: list[str] = []

    def flush() -> None:
        if bullets:
            blocks.append("<ul>" + "".join(f"<li>{esc(b)}</li>" for b in bullets) + "</ul>")
            bullets.clear()
        if paragraph:
            blocks.append(f"<p>{esc(''.join(paragraph))}</p>")
            paragraph.clear()

    for line in str(text).splitlines():
        stripped = line.strip()
        if stripped.startswith(("- ", "・", "* ")):
            if paragraph:
                flush()
            bullets.append(stripped.lstrip("-・* ").strip())
            continue
        if not stripped:
            flush()
            continue
        if bullets:
            flush()
        paragraph.append(stripped)
    flush()
    return "".join(blocks)


def embed_image(source: str, base_dir: Path) -> str | None:
    """画像を data URI にして HTML に埋め込む。見つからない場合は None。"""
    path = Path(source)
    if not path.is_absolute():
        path = base_dir / path
    if not path.exists():
        print(f"[警告] 画像が見つかりません: {path}", file=sys.stderr)
        return None
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def table_html(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>" for row in rows
    )
    return f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


# ---------------------------------------------------------------- HTML 生成

def render_html(manual: dict, base_dir: Path) -> str:
    title = manual.get("title") or "業務マニュアル"
    meta_items = [
        ("文書番号", manual.get("document_no")),
        ("版数", manual.get("version")),
        ("所管部署", manual.get("department")),
        ("作成者", manual.get("author")),
        ("適用開始日", manual.get("effective_date")),
    ]
    meta = "".join(
        f"<span><b>{esc(label)}:</b> {esc(value)}</span>"
        for label, value in meta_items if value
    )

    parts: list[str] = [f"<h1>{esc(title)}</h1>", f'<div class="meta">{meta}</div>']

    for label, key in (("目的", "purpose"), ("適用範囲", "scope")):
        if manual.get(key):
            parts.append(
                f'<div class="block"><div class="label">{label}</div>{rich_text(manual[key])}</div>'
            )

    if manual.get("terms"):
        rows = [[t.get("term", ""), t.get("definition", "")] for t in manual["terms"]]
        parts.append('<div class="block"><div class="label">用語定義</div>'
                     + table_html(["用語", "説明"], rows) + "</div>")

    if manual.get("revisions"):
        rows = [
            [r.get("version", ""), r.get("date", ""), r.get("author", ""), r.get("summary", "")]
            for r in manual["revisions"]
        ]
        parts.append('<div class="block"><div class="label">改訂履歴</div>'
                     + table_html(["版数", "改訂日", "改訂者", "内容"], rows) + "</div>")

    sections = manual.get("sections") or []
    if sections:
        toc = "".join(
            f'<li><a href="#sec{i}">{esc(s.get("title", f"第{i}章"))}</a></li>'
            for i, s in enumerate(sections, start=1)
        )
        parts.append(f'<div class="block"><div class="label">目次</div><ol class="toc">{toc}</ol></div>')

    for section_no, section in enumerate(sections, start=1):
        parts.append(f'<h2 id="sec{section_no}">{section_no}. {esc(section.get("title", ""))}</h2>')
        if section.get("description"):
            parts.append(rich_text(section["description"]))
        for step_no, step in enumerate(section.get("steps") or [], start=1):
            parts.append(render_step(f"{section_no}-{step_no}", step, base_dir))

    if manual.get("faq"):
        parts.append('<h2 id="faq">よくある質問</h2>')
        rows = [[f.get("q", ""), f.get("a", "")] for f in manual["faq"]]
        parts.append(table_html(["質問", "回答"], rows))

    if manual.get("contacts"):
        parts.append('<h2 id="contacts">問い合わせ先</h2>')
        rows = [
            [c.get("name", ""), c.get("role", ""), c.get("contact", "")]
            for c in manual["contacts"]
        ]
        parts.append(table_html(["担当", "内容", "連絡先"], rows))

    parts.append(
        f"<footer>{esc(title)}"
        + (f" / 版数 {esc(manual.get('version'))}" if manual.get("version") else "")
        + f" / 出力日 {dt.date.today():%Y-%m-%d}</footer>"
    )

    return (
        "<!doctype html>\n<html lang=\"ja\">\n<head>\n<meta charset=\"utf-8\">\n"
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{esc(title)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n"
        f'<div class="sheet">\n{"".join(parts)}\n</div>\n</body>\n</html>\n'
    )


def render_step(number: str, step: dict, base_dir: Path) -> str:
    tags = "".join(
        f'<span class="tag">{esc(label)}: {esc(step[key])}</span>'
        for label, key in (("担当", "role"), ("システム", "system"), ("所要", "duration"))
        if step.get(key)
    )
    body = [
        '<div class="step">',
        '<div class="step-head">',
        f'<span class="step-no">{esc(number)}</span>',
        f'<span class="step-title">{esc(step.get("title", ""))}</span>',
        f'<span class="tags">{tags}</span>' if tags else "",
        "</div>",
    ]
    if step.get("detail"):
        body.append(f'<div class="detail">{rich_text(step["detail"])}</div>')
    if step.get("note"):
        body.append(f'<div class="callout note"><span class="label">補足</span>{esc(step["note"])}</div>')
    if step.get("warning"):
        body.append(f'<div class="callout warn"><span class="label">注意</span>{esc(step["warning"])}</div>')
    if step.get("checks"):
        items = "".join(f"<li>{esc(c)}</li>" for c in step["checks"])
        body.append(f'<ul class="checks">{items}</ul>')
    if step.get("image"):
        uri = embed_image(step["image"], base_dir)
        if uri:
            caption = esc(step.get("caption", ""))
            body.append(
                f'<figure><img src="{uri}" alt="{esc(step.get("title", ""))}">'
                + (f"<figcaption>{caption}</figcaption>" if caption else "")
                + "</figure>"
            )
    body.append("</div>")
    return "".join(body)


# ---------------------------------------------------------------- Markdown 生成

def render_markdown(manual: dict) -> str:
    lines: list[str] = [f"# {manual.get('title', '業務マニュアル')}", ""]
    meta = [
        f"- {label}: {manual[key]}"
        for label, key in (
            ("文書番号", "document_no"), ("版数", "version"), ("所管部署", "department"),
            ("作成者", "author"), ("適用開始日", "effective_date"),
        )
        if manual.get(key)
    ]
    lines += meta + [""]

    for label, key in (("目的", "purpose"), ("適用範囲", "scope")):
        if manual.get(key):
            lines += [f"## {label}", "", str(manual[key]).strip(), ""]

    if manual.get("terms"):
        lines += ["## 用語定義", "", "| 用語 | 説明 |", "| --- | --- |"]
        lines += [f"| {t.get('term','')} | {t.get('definition','')} |" for t in manual["terms"]]
        lines.append("")

    if manual.get("revisions"):
        lines += ["## 改訂履歴", "", "| 版数 | 改訂日 | 改訂者 | 内容 |", "| --- | --- | --- | --- |"]
        lines += [
            f"| {r.get('version','')} | {r.get('date','')} | {r.get('author','')} | {r.get('summary','')} |"
            for r in manual["revisions"]
        ]
        lines.append("")

    for section_no, section in enumerate(manual.get("sections") or [], start=1):
        lines += [f"## {section_no}. {section.get('title','')}", ""]
        if section.get("description"):
            lines += [str(section["description"]).strip(), ""]
        for step_no, step in enumerate(section.get("steps") or [], start=1):
            lines.append(f"### {section_no}-{step_no}. {step.get('title','')}")
            tags = [
                f"{label}: {step[key]}"
                for label, key in (("担当", "role"), ("システム", "system"), ("所要", "duration"))
                if step.get(key)
            ]
            if tags:
                lines += ["", f"*{' / '.join(tags)}*"]
            if step.get("detail"):
                lines += ["", str(step["detail"]).strip()]
            if step.get("note"):
                lines += ["", f"> **補足**: {step['note']}"]
            if step.get("warning"):
                lines += ["", f"> **注意**: {step['warning']}"]
            for check in step.get("checks") or []:
                lines.append(f"- [ ] {check}")
            if step.get("image"):
                lines += ["", f"![{step.get('title','')}]({step['image']})"]
            lines.append("")

    if manual.get("faq"):
        lines += ["## よくある質問", ""]
        for item in manual["faq"]:
            lines += [f"**Q. {item.get('q','')}**", "", f"A. {item.get('a','')}", ""]

    if manual.get("contacts"):
        lines += ["## 問い合わせ先", "", "| 担当 | 内容 | 連絡先 |", "| --- | --- | --- |"]
        lines += [
            f"| {c.get('name','')} | {c.get('role','')} | {c.get('contact','')} |"
            for c in manual["contacts"]
        ]
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------- 検証

def validate(manual: dict) -> list[str]:
    warnings: list[str] = []
    if not manual.get("title"):
        warnings.append("title（マニュアル名）が未設定です")
    if not manual.get("sections"):
        warnings.append("sections（章）が 1 つもありません")
    for section_no, section in enumerate(manual.get("sections") or [], start=1):
        if not section.get("steps"):
            warnings.append(f"第{section_no}章「{section.get('title','')}」に手順がありません")
        for step_no, step in enumerate(section.get("steps") or [], start=1):
            if not step.get("title"):
                warnings.append(f"手順 {section_no}-{step_no} に title がありません")
            if not step.get("detail"):
                warnings.append(f"手順 {section_no}-{step_no}「{step.get('title','')}」に detail がありません")
    return warnings


# ---------------------------------------------------------------- エントリポイント

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="YAML の定義から業務マニュアルを生成する",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="マニュアル定義ファイル (.yaml)")
    parser.add_argument("--new", action="store_true", help="ひな形を作成して終了する")
    parser.add_argument("--format", choices=["html", "md", "both"], default="html",
                        help="出力形式（既定: html）")
    parser.add_argument("--out", default="output", help="出力先ディレクトリ（既定: output）")
    args = parser.parse_args(argv)

    path = Path(args.input)

    if args.new:
        if path.exists():
            raise SystemExit(f"既にファイルが存在します: {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            TEMPLATE.format(title=path.stem, today=f"{dt.date.today():%Y-%m-%d}"),
            encoding="utf-8",
        )
        print(f"[作成] ひな形: {path}")
        print("内容を編集したあと、--new なしで実行するとマニュアルが生成されます。")
        return 0

    if not path.exists():
        raise SystemExit(f"ファイルが見つかりません: {path}（--new でひな形を作成できます）")

    try:
        manual = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as error:
        raise SystemExit(
            f"YAML を読み込めません: {path}\n{error}\n"
            "ヒント: 値に「: 」や「#」を含める場合は \"二重引用符\" で囲んでください。"
        )
    if not isinstance(manual, dict):
        raise SystemExit("YAML の最上位は項目名と値の対応（マッピング）である必要があります。")

    for warning in validate(manual):
        print(f"[警告] {warning}", file=sys.stderr)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = manual.get("title") or path.stem

    if args.format in ("html", "both"):
        html_path = out_dir / f"{stem}.html"
        html_path.write_text(render_html(manual, path.parent), encoding="utf-8")
        print(f"[出力] HTML: {html_path}（ブラウザで開き 印刷→PDF保存 で配布用 PDF になります）")
    if args.format in ("md", "both"):
        md_path = out_dir / f"{stem}.md"
        md_path.write_text(render_markdown(manual), encoding="utf-8")
        print(f"[出力] Markdown: {md_path}")

    steps = sum(len(s.get("steps") or []) for s in manual.get("sections") or [])
    print(f"  - 章: {len(manual.get('sections') or [])} / 手順: {steps}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:  # head などにパイプした場合
        sys.stderr.close()
        raise SystemExit(0)
