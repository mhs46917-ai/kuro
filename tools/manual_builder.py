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
                                PageBreak, PageTemplate, Paragraph, Spacer, Table,
                                TableStyle)

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


def _build_markdown_sheet(manual):
    """表裏1枚もの（sheet レイアウト）の Markdown。"""
    slug = manual["slug"]
    out = [f'# {manual["title"]}', ""]
    if manual.get("meta"):
        out += ["| 項目 | 内容 |", "| --- | --- |"]
        out += [f"| {k} | {v} |" for k, v in manual["meta"]]
        out.append("")
    out += [f'> 印刷用PDF：[{manual["title"]}.pdf]({manual["title"]}.pdf)（A4 両面1枚）', ""]

    for page in manual["pages"]:
        out += ["---", "", f'## {page["side"]}　{page["title"]}', ""]
        if page.get("highlight"):
            out += [f'> ⏰ **{_plain(page["highlight"])}**', ""]
        if page.get("lead"):
            out += [_plain(page["lead"]), ""]
        for i, step in enumerate(page["steps"], start=1):
            out += [f'{i}. {_plain(step["text"])}']
            if step.get("image"):
                out += ["", f'![{page["title"]}{i}](images/{slug}/{step["image"]})', ""]
        out.append("")
        if page.get("image"):
            out += [f'![{page["title"]}](images/{slug}/{page["image"]})', ""]
        for note in page.get("notes", []):
            out += [f'> ⚠️ {_plain(note)}', ""]

    path = os.path.join(DOCS, f'{manual["title"]}.md')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return path


def build_markdown(manual):
    if manual.get("layout") == "sheet":
        return _build_markdown_sheet(manual)
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


def _page_footer(manual, font):
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
    return on_page


def _render(manual, story, font):
    """story を A4 の PDF に書き出してパスを返す。"""
    path = os.path.join(DOCS, f'{manual["title"]}.pdf')
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=18 * mm,
                          title=manual["title"], author=manual.get("author", ""))
    frame = Frame(MARGIN, 18 * mm, FRAME_W, PH - MARGIN - 18 * mm, id="n",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame],
                                       onPage=_page_footer(manual, font))])
    doc.build(story)
    return path


def _note_box(text, style, color=ACCENT, bg="#fdf0ee"):
    t = Table([[Paragraph(text, style)]], colWidths=[FRAME_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)),
        ("BOX", (0, 0), (-1, -1), 0.8, color),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    return t


def build_pdf_sheet(manual):
    """表裏1枚もの。1ページ＝1面で、写真を大きく載せる。"""
    font = register_japanese_font()
    st = _styles(font)
    bold = font + "-Bold"
    imgdir = image_dir(manual)

    st_side = ParagraphStyle("side", fontName=bold, fontSize=10, leading=13,
                             textColor=colors.white, alignment=1)
    st_ptitle = ParagraphStyle("pt", fontName=bold, fontSize=19, leading=24, textColor=NAVY)
    st_lead = ParagraphStyle("ld", fontName=font, fontSize=11, leading=17,
                             textColor=colors.HexColor("#1a1a1a"))
    st_hi = ParagraphStyle("hi", fontName=bold, fontSize=12.5, leading=18, textColor=NAVY)
    st_num = ParagraphStyle("nm", fontName=bold, fontSize=15, leading=20,
                            textColor=colors.white, alignment=1)
    st_step = ParagraphStyle("sp", fontName=font, fontSize=12.5, leading=19,
                             textColor=colors.HexColor("#1a1a1a"))
    st_warn = ParagraphStyle("wn", fontName=font, fontSize=10.5, leading=16,
                             textColor=colors.HexColor("#8a1c12"))

    story = []
    for pi, page in enumerate(manual["pages"]):
        if pi:
            story.append(PageBreak())

        head = Table([[Paragraph(page["side"], st_side), Paragraph(page["title"], st_ptitle)]],
                     colWidths=[20 * mm, FRAME_W - 20 * mm])
        head.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), NAVY),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (1, 0), (1, 0), 4 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ]))
        story.append(head)
        hr = Table([[""]], colWidths=[FRAME_W], rowHeights=[1.2])
        hr.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY)]))
        story += [hr, Spacer(1, 4 * mm)]

        if page.get("highlight"):
            story += [_note_box(page["highlight"], st_hi, NAVY, "#eef2f7"), Spacer(1, 4 * mm)]
        if page.get("lead"):
            story += [Paragraph(page["lead"], st_lead), Spacer(1, 4 * mm)]

        img_h = page.get("image_height_mm", 78) * mm
        for i, step in enumerate(page["steps"], start=1):
            badge = Table([[Paragraph(str(i), st_num)]], colWidths=[9 * mm], rowHeights=[9 * mm])
            badge.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            row = Table([[badge, Paragraph(step["text"], st_step)]],
                        colWidths=[9 * mm, FRAME_W - 9 * mm])
            row.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (1, 0), (1, 0), 4 * mm),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            block = [row]
            if step.get("image"):
                photo = _fit_image(os.path.join(imgdir, step["image"]), FRAME_W * 0.52, img_h)
                holder = Table([[photo]], colWidths=[FRAME_W])
                holder.setStyle(TableStyle([
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]))
                block.append(holder)
            block.append(Spacer(1, 5 * mm))
            story.append(KeepTogether(block))

        if page.get("image"):
            photo = _fit_image(os.path.join(imgdir, page["image"]), FRAME_W * 0.62, img_h)
            holder = Table([[photo]], colWidths=[FRAME_W])
            holder.setStyle(TableStyle([
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
            ]))
            story += [holder, Spacer(1, 5 * mm)]

        for note in page.get("notes", []):
            story += [_note_box("※ " + note, st_warn), Spacer(1, 3 * mm)]

    return _render(manual, story, font)


def build_pdf(manual):
    if manual.get("layout") == "sheet":
        return build_pdf_sheet(manual)
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

    return _render(manual, story, font)


def validate(manual):
    """画像の不足・未使用をチェックして警告リストを返す。"""
    warnings = []
    imgdir = image_dir(manual)
    used = set()
    if manual.get("layout") == "sheet":
        targets = []
        for page in manual["pages"]:
            if page.get("image"):
                targets.append((page["side"], page["image"]))
            for i, step in enumerate(page["steps"], start=1):
                if step.get("image"):
                    targets.append((f'{page["side"]}手順{i}', step["image"]))
    else:
        targets = [(f"手順{step_number(i)}", step["image"])
                   for i, step in enumerate(manual["steps"])]
    for label, name in targets:
        used.add(name)
        p = os.path.join(imgdir, name)
        if not os.path.exists(p):
            warnings.append(f"{label}: 画像がありません -> {p}")
    if os.path.isdir(imgdir):
        for f in sorted(os.listdir(imgdir)):
            if f.lower().endswith((".jpg", ".jpeg", ".png")) and f not in used:
                warnings.append(f"未使用の画像: {f}")
    else:
        warnings.append(f"画像フォルダがありません -> {imgdir}")
    return warnings
