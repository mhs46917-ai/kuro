# -*- coding: utf-8 -*-
"""マニュアル定義（manuals/<slug>.py の MANUAL）から Markdown と PDF を生成する。

レイアウト・配色はすべてここに集約しているので、マニュアルを増やすときは
manuals/ にデータを1ファイル足すだけでよい。
"""
import os
import re

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

from jp_font import register_japanese_font

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(REPO, "docs")
IMAGES_ROOT = os.path.join(DOCS, "images")

CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"

NAVY = colors.HexColor("#1f3a5f")
ACCENT = colors.HexColor("#c0392b")
LIGHT = colors.HexColor("#eef2f7")
LINE = colors.HexColor("#c8d2de")
GREY = colors.HexColor("#666666")

MARGIN = 16 * mm
PW, PH = A4
FRAME_W = PW - 2 * MARGIN


def step_number(i):
    return CIRCLED[i] if i < len(CIRCLED) else f"({i + 1})"


def image_dir(manual):
    return os.path.join(IMAGES_ROOT, manual["slug"])


# --------------------------------------------------------------------------
# Markdown
# --------------------------------------------------------------------------

def _plain(text):
    return re.sub(r"</?b>", "**", text)


def build_markdown(manual):
    slug = manual["slug"]
    out = [f'# {manual["title"]}', ""]

    if manual.get("meta"):
        out += ["| 項目 | 内容 |", "| --- | --- |"]
        out += [f"| {k} | {v} |" for k, v in manual["meta"]]
        out.append("")

    out += [f'> 印刷用PDF：[{manual["title"]}.pdf]({manual["title"]}.pdf)', "", "---", ""]

    n = 0
    if manual.get("purpose"):
        n += 1
        out += [f"## {n}. 目的", "", manual["purpose"], ""]

    freq = manual.get("frequency")
    if freq:
        n += 1
        out += [f"## {n}. 清掃頻度", "",
                "| " + " | ".join(freq["columns"]) + " |",
                "| " + " | ".join("---" for _ in freq["columns"]) + " |"]
        for row in freq["rows"]:
            out.append("| " + " | ".join(c.replace("\n", "<br>") for c in row) + " |")
        out.append("")

    if manual.get("preparation"):
        n += 1
        out += [f"## {n}. 事前準備", ""] + [f"- {x}" for x in manual["preparation"]] + [""]

    if manual.get("safety"):
        n += 1
        out += [f"## {n}. 安全上の注意", ""]
        for i, x in enumerate(manual["safety"]):
            if i:
                out.append(">")
            out.append(f"> ⚠️ {_plain(x)}")
        out += ["", "---", ""]

    n += 1
    out += [f"## {n}. 作業手順", ""]
    for i, step in enumerate(manual["steps"]):
        num = step_number(i)
        out += [f'### 手順{num} {step["title"]}', ""]
        out += [_plain(l) for l in step["lines"]]
        out += ["", f'![{step["title"]}](images/{slug}/{step["image"]})', "", "---", ""]

    if manual.get("checklist"):
        n += 1
        out += [f"## {n}. 作業完了後の確認", ""]
        out += [f"- [ ] {x}" for x in manual["checklist"]] + [""]

    cols = manual.get("record_columns")
    if cols:
        n += 1
        out += [f"## {n}. 実施記録", "",
                "| " + " | ".join(cols) + " |",
                "| " + " | ".join("---" for _ in cols) + " |",
                "| " + " | ".join("" for _ in cols) + " |", ""]

    path = os.path.join(DOCS, f'{manual["title"]}.md')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return path


# --------------------------------------------------------------------------
# PDF
# --------------------------------------------------------------------------

def _styles(font):
    bold = font + "-Bold"
    return {
        "title": ParagraphStyle("t", fontName=bold, fontSize=20, leading=26, textColor=NAVY),
        "sub": ParagraphStyle("s", fontName=font, fontSize=10, leading=14, textColor=GREY),
        "h2": ParagraphStyle("h2", fontName=font, fontSize=12, leading=16,
                             textColor=colors.white, leftIndent=3 * mm),
        "steph": ParagraphStyle("sh", fontName=font, fontSize=11.5, leading=15,
                                textColor=colors.white, leftIndent=2.5 * mm),
        "body": ParagraphStyle("b", fontName=font, fontSize=9.6, leading=15, alignment=TA_LEFT,
                               textColor=colors.HexColor("#1a1a1a"), spaceAfter=1.2 * mm),
        "cell": ParagraphStyle("c", fontName=font, fontSize=9.5, leading=14),
        "cellh": ParagraphStyle("ch", fontName=font, fontSize=9.5, leading=14,
                                textColor=colors.white),
        "note": ParagraphStyle("n", fontName=font, fontSize=9, leading=14,
                               textColor=colors.HexColor("#8a1c12")),
    }


def _bar(text, style, color=NAVY):
    t = Table([[Paragraph(text, style)]], colWidths=[FRAME_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def _fit_image(path, max_w, max_h):
    w, h = PILImage.open(path).size
    scale = min(max_w / w, max_h / h)
    return Image(path, width=w * scale, height=h * scale)


def build_pdf(manual):
    font = register_japanese_font()
    st = _styles(font)
    imgdir = image_dir(manual)
    story = []

    story.append(Paragraph(manual["title"], st["title"]))
    if manual.get("subtitle"):
        story += [Spacer(1, 1.5 * mm), Paragraph(manual["subtitle"], st["sub"])]
    story.append(Spacer(1, 1 * mm))
    hr = Table([[""]], colWidths=[FRAME_W], rowHeights=[1.2])
    hr.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY)]))
    story += [hr, Spacer(1, 5 * mm)]

    freq = manual.get("frequency")
    if freq:
        story += [_bar("清掃頻度", st["h2"]), Spacer(1, 2.5 * mm)]
        rows = [[Paragraph(c, st["cellh"]) for c in freq["columns"]]]
        rows += [[Paragraph(c.replace("\n", "<br/>"), st["cell"]) for c in r] for r in freq["rows"]]
        widths = freq.get("widths", [1.0 / len(freq["columns"])] * len(freq["columns"]))
        t = Table(rows, colWidths=[FRAME_W * w for w in widths])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#b9c4d2")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 2.2 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2 * mm),
            ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
        ]))
        story += [t, Spacer(1, 5 * mm)]

    if manual.get("safety"):
        story += [_bar("安全上の注意", st["h2"], ACCENT), Spacer(1, 2.5 * mm)]
        body = "<br/>".join("・" + x for x in manual["safety"])
        warn = Table([[Paragraph(body, st["note"])]], colWidths=[FRAME_W])
        warn.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fdf0ee")),
            ("BOX", (0, 0), (-1, -1), 0.6, ACCENT),
            ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ]))
        story += [warn, Spacer(1, 5 * mm)]

    story += [_bar("作業手順", st["h2"]), Spacer(1, 3 * mm)]

    img_w = FRAME_W * manual.get("image_column_ratio", 0.38)
    txt_w = FRAME_W - img_w
    img_h = manual.get("image_max_height_mm", 62) * mm
    for i, step in enumerate(manual["steps"]):
        head = _bar(f'{step_number(i)}　{step["title"]}', st["steph"])
        text = [Paragraph(l, st["body"]) for l in step["lines"]]
        photo = _fit_image(os.path.join(imgdir, step["image"]), img_w - 4 * mm, img_h)
        inner = Table([[text, photo]], colWidths=[txt_w, img_w])
        inner.setStyle(TableStyle([
            ("VALIGN", (0, 0), (0, 0), "TOP"),
            ("VALIGN", (1, 0), (1, 0), "MIDDLE"),
            ("ALIGN", (1, 0), (1, 0), "CENTER"),
            ("LEFTPADDING", (0, 0), (0, 0), 2 * mm),
            ("RIGHTPADDING", (0, 0), (0, 0), 3 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE),
            ("LINEBEFORE", (1, 0), (1, 0), 0.5, LINE),
        ]))
        story.append(KeepTogether([head, inner, Spacer(1, 4 * mm)]))

    if manual.get("checklist"):
        ct = Table([[Paragraph("□", st["cell"]), Paragraph(c, st["cell"])]
                    for c in manual["checklist"]],
                   colWidths=[8 * mm, FRAME_W - 8 * mm])
        ct.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#b9c4d2")),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, LIGHT]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 1.8 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8 * mm),
            ("LEFTPADDING", (1, 0), (1, -1), 3 * mm),
        ]))
        story.append(KeepTogether([Spacer(1, 1 * mm), _bar("作業完了後の確認", st["h2"]),
                                   Spacer(1, 2.5 * mm), ct, Spacer(1, 5 * mm)]))

    cols = manual.get("record_columns")
    if cols:
        nrows = manual.get("record_rows", 5)
        rec = [[Paragraph(c, st["cellh"]) for c in cols]]
        rec += [[Paragraph("", st["cell"]) for _ in cols] for _ in range(nrows)]
        widths = manual.get("record_widths", [1.0 / len(cols)] * len(cols))
        rt = Table(rec, colWidths=[FRAME_W * w for w in widths],
                   rowHeights=[8 * mm] + [9 * mm] * nrows, repeatRows=1)
        rt.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#b9c4d2")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("LEFTPADDING", (0, 0), (-1, -1), 2 * mm),
        ]))
        story.append(KeepTogether([_bar("実施記録", st["h2"]), Spacer(1, 2.5 * mm), rt]))

    def on_page(canv, doc):
        canv.saveState()
        canv.setFont(font, 7.5)
        canv.setFillColor(GREY)
        canv.drawString(MARGIN, 10 * mm, manual["title"])
        canv.drawRightString(PW - MARGIN, 10 * mm, f"- {canv.getPageNumber()} -")
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.4)
        canv.line(MARGIN, 13 * mm, PW - MARGIN, 13 * mm)
        canv.restoreState()

    path = os.path.join(DOCS, f'{manual["title"]}.pdf')
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=18 * mm,
                          title=manual["title"], author=manual.get("author", ""))
    frame = Frame(MARGIN, 18 * mm, FRAME_W, PH - MARGIN - 18 * mm, id="n",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=on_page)])
    doc.build(story)
    return path


def validate(manual):
    """画像の不足・未使用をチェックして警告リストを返す。"""
    warnings = []
    imgdir = image_dir(manual)
    used = set()
    for i, step in enumerate(manual["steps"]):
        p = os.path.join(imgdir, step["image"])
        used.add(step["image"])
        if not os.path.exists(p):
            warnings.append(f'手順{step_number(i)}: 画像がありません -> {p}')
    if os.path.isdir(imgdir):
        for f in sorted(os.listdir(imgdir)):
            if f.lower().endswith((".jpg", ".jpeg", ".png")) and f not in used:
                warnings.append(f"未使用の画像: {f}")
    else:
        warnings.append(f"画像フォルダがありません -> {imgdir}")
    return warnings
