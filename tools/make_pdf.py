# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from steps import TITLE, SUBTITLE, FREQ, STEPS
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, KeepTogether)

FONT = 'IPAGothic'
pdfmetrics.registerFont(TTFont(FONT, '/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf'))
pdfmetrics.registerFont(TTFont(FONT + '-B', '/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf'))
pdfmetrics.registerFontFamily(FONT, normal=FONT, bold=FONT + '-B', italic=FONT, boldItalic=FONT + '-B')

IMGDIR = '/home/user/kuro/docs/images/pool-hair-catcher'
OUT = '/home/user/kuro/docs/プールヘアキャッチャー清掃.pdf'

NAVY = colors.HexColor('#1f3a5f')
ACCENT = colors.HexColor('#c0392b')
LIGHT = colors.HexColor('#eef2f7')
GREY = colors.HexColor('#666666')

MARGIN = 16 * mm
PW, PH = A4
FRAME_W = PW - 2 * MARGIN

st_title = ParagraphStyle('t', fontName=FONT, fontSize=20, leading=26, textColor=NAVY)
st_sub = ParagraphStyle('s', fontName=FONT, fontSize=10, leading=14, textColor=GREY)
st_h2 = ParagraphStyle('h2', fontName=FONT, fontSize=12, leading=16, textColor=colors.white,
                       leftIndent=3*mm, spaceBefore=1*mm)
st_steph = ParagraphStyle('sh', fontName=FONT, fontSize=11.5, leading=15, textColor=colors.white,
                          leftIndent=2.5*mm)
st_body = ParagraphStyle('b', fontName=FONT, fontSize=9.6, leading=15, alignment=TA_LEFT,
                         textColor=colors.HexColor('#1a1a1a'), spaceAfter=1.2*mm)
st_cell = ParagraphStyle('c', fontName=FONT, fontSize=9.5, leading=14)
st_cellh = ParagraphStyle('ch', fontName=FONT, fontSize=9.5, leading=14, textColor=colors.white)
st_note = ParagraphStyle('n', fontName=FONT, fontSize=9, leading=14,
                         textColor=colors.HexColor('#8a1c12'))
st_foot = ParagraphStyle('f', fontName=FONT, fontSize=7.5, leading=10, textColor=GREY)


def bar(text, color=NAVY, style=None):
    t = Table([[Paragraph(text, style or st_h2)]], colWidths=[FRAME_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t


def sized_image(path, max_w, max_h):
    w, h = PILImage.open(path).size
    scale = min(max_w / w, max_h / h)
    return Image(path, width=w * scale, height=h * scale)


story = []

# --- header ---
story.append(Paragraph(TITLE, st_title))
story.append(Spacer(1, 1.5*mm))
story.append(Paragraph(SUBTITLE, st_sub))
story.append(Spacer(1, 1*mm))
hr = Table([['']], colWidths=[FRAME_W], rowHeights=[1.2])
hr.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), NAVY)]))
story.append(hr)
story.append(Spacer(1, 5*mm))

# --- 清掃頻度 ---
story.append(bar('清掃頻度'))
story.append(Spacer(1, 2.5*mm))
rows = [[Paragraph(c, st_cellh if i == 0 else st_cell) for c in row.copy()]
        for i, row in enumerate([[c.replace('\n', '<br/>') for c in r] for r in FREQ])]
ft = Table(rows, colWidths=[FRAME_W*0.20, FRAME_W*0.16, FRAME_W*0.64])
ft.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT]),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#b9c4d2')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 2.2*mm),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2*mm),
    ('LEFTPADDING', (0, 0), (-1, -1), 3*mm),
]))
story.append(ft)
story.append(Spacer(1, 5*mm))

# --- 安全上の注意 ---
story.append(bar('安全上の注意', ACCENT))
story.append(Spacer(1, 2.5*mm))
warn = Table([[Paragraph(
    '・必ずろ過器を停止し、前後バルブを閉じてからフタを開けること。通水状態でフタを開けると内圧により水が噴出する恐れがある。<br/>'
    '・作業時は手袋・長靴を着用し、床面の水濡れによる転倒に注意する。<br/>'
    '・「常時開」の表示札が付いたバルブは、作業終了後に必ず全開へ戻すこと。', st_note)]],
    colWidths=[FRAME_W])
warn.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fdf0ee')),
    ('BOX', (0, 0), (-1, -1), 0.6, ACCENT),
    ('LEFTPADDING', (0, 0), (-1, -1), 3*mm),
    ('RIGHTPADDING', (0, 0), (-1, -1), 3*mm),
    ('TOPPADDING', (0, 0), (-1, -1), 2.5*mm),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5*mm),
]))
story.append(warn)
story.append(Spacer(1, 5*mm))

story.append(bar('作業手順'))
story.append(Spacer(1, 3*mm))

# --- steps ---
IMG_W = FRAME_W * 0.38
TXT_W = FRAME_W - IMG_W
for num, name, lines, img in STEPS:
    head = bar(f'{num}　{name}', NAVY, st_steph)
    body = [Paragraph(l, st_body) for l in lines]
    photo = sized_image(os.path.join(IMGDIR, img), IMG_W - 4*mm, 62*mm)
    inner = Table([[body, photo]], colWidths=[TXT_W, IMG_W])
    inner.setStyle(TableStyle([
        ('VALIGN', (0, 0), (0, 0), 'TOP'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('LEFTPADDING', (0, 0), (0, 0), 2*mm),
        ('RIGHTPADDING', (0, 0), (0, 0), 3*mm),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5*mm),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#c8d2de')),
        ('LINEBEFORE', (1, 0), (1, 0), 0.5, colors.HexColor('#c8d2de')),
    ]))
    story.append(KeepTogether([head, inner, Spacer(1, 4*mm)]))

# --- checklist ---
story.append(Spacer(1, 1*mm))
checks = [
    '前後バルブが全開（配管に対して水平）に戻っている',
    'ヘアーキャッチャー内が満水で、エア抜きネジが締まっている',
    'フタ・フランジ部・ドレン部から漏水がない',
    '制御盤の「底引 運転」スイッチが通常位置（自動）に戻っている',
    '表示灯・電流計・圧力計が通常値を示し、異常音・異常振動がない',
    '工具・ブラシを片付け、ごみ袋を所定の場所へ廃棄した',
]
ct = Table([[Paragraph('□', st_cell), Paragraph(c, st_cell)] for c in checks],
           colWidths=[8*mm, FRAME_W - 8*mm])
ct.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#b9c4d2')),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, LIGHT]),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('TOPPADDING', (0, 0), (-1, -1), 1.8*mm),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8*mm),
    ('LEFTPADDING', (1, 0), (1, -1), 3*mm),
]))
story.append(KeepTogether([bar('作業完了後の確認'), Spacer(1, 2.5*mm), ct, Spacer(1, 5*mm)]))

# --- record ---
hdr = ['実施日', '実施者', '堆積物の量・状態', '清掃前 圧力', '清掃後 圧力', '特記事項']
rec = [[Paragraph(h, st_cellh) for h in hdr]] + [[Paragraph('', st_cell) for _ in hdr] for _ in range(5)]
rt = Table(rec, colWidths=[FRAME_W*x for x in (0.13, 0.12, 0.25, 0.13, 0.13, 0.24)],
           rowHeights=[8*mm] + [9*mm]*5, repeatRows=1)
rt.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#b9c4d2')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('LEFTPADDING', (0, 0), (-1, -1), 2*mm),
]))
story.append(KeepTogether([bar('実施記録'), Spacer(1, 2.5*mm), rt]))


def on_page(canv, doc):
    canv.saveState()
    canv.setFont(FONT, 7.5)
    canv.setFillColor(GREY)
    canv.drawString(MARGIN, 10*mm, TITLE)
    canv.drawRightString(PW - MARGIN, 10*mm, f'- {canv.getPageNumber()} -')
    canv.setStrokeColor(colors.HexColor('#c8d2de'))
    canv.setLineWidth(0.4)
    canv.line(MARGIN, 13*mm, PW - MARGIN, 13*mm)
    canv.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                      topMargin=MARGIN, bottomMargin=18*mm, title=TITLE, author='株式会社ウェルアップ')
frame = Frame(MARGIN, 18*mm, FRAME_W, PH - MARGIN - 18*mm, id='n',
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='all', frames=[frame], onPage=on_page)])
doc.build(story)
print('built', OUT, os.path.getsize(OUT) // 1024, 'KB')
