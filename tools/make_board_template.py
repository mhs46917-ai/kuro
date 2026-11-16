#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ホワイトボード用の記入レイアウトを生成する。

プール水温と熱交換器バルブの操作を1日分記録するための枠。
用紙サイズは --size で変える（既定 A3縦）。実寸のボードに合わせたいときは
--width / --height に mm を指定する。

    python3 tools/make_board_template.py
    python3 tools/make_board_template.py --width 450 --height 600 --rows 8
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A3
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from jp_font import register_japanese_font

NAVY = colors.HexColor("#1f3a5f")
RED = colors.HexColor("#c0392b")
LIGHT = colors.HexColor("#eef2f7")
PINK = colors.HexColor("#fdf0ee")
LINE = colors.HexColor("#9aa7b8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def centered(c, text, font, size, x, y, w, h, color=colors.black):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawCentredString(x + w / 2, y + h / 2 - size * 0.36, text)


def build(path, W, H, rows, margin=12 * mm):
    font = register_japanese_font()
    bold = font + "-Bold"
    c = canvas.Canvas(path, pagesize=(W, H))
    fw = W - 2 * margin
    x0 = margin
    y = H - margin

    # ── タイトル帯 ─────────────────────────────
    th = 20 * mm
    y -= th
    c.setFillColor(NAVY)
    c.rect(x0, y, fw, th, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont(bold, 19)
    c.drawString(x0 + 6 * mm, y + th / 2 - 7, "プール水温・熱交換器バルブ 記録")
    # 日付記入枠
    dw = 76 * mm
    c.setFillColor(colors.white)
    c.rect(x0 + fw - dw - 4 * mm, y + 3 * mm, dw, th - 6 * mm, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.setFont(bold, 14)
    c.drawString(x0 + fw - dw + 2 * mm, y + th / 2 - 5, "日付　　　/　　　（　　）")

    # ── 目標値の帯（消さない） ─────────────────
    y -= 4 * mm
    bh = 24 * mm
    y -= bh
    c.setFillColor(LIGHT)
    c.rect(x0, y, fw, bh, stroke=0, fill=1)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.2)
    c.rect(x0, y, fw, bh, stroke=1, fill=0)
    c.setFillColor(NAVY)
    c.setFont(bold, 15)
    c.drawString(x0 + 6 * mm, y + bh - 10 * mm, "理想 30.5℃　／　管理範囲 30.3〜30.8℃")
    c.setFont(font, 13.5)
    c.drawString(x0 + 6 * mm, y + 5 * mm,
                 "30.8℃以上 → バルブ①② を【閉】　　30.3℃以下 → バルブ①② を【開】")

    # ── 記録表 ────────────────────────────────
    y -= 5 * mm
    cols = [("時　刻", 0.19), ("水　温 ℃（緑の数値）", 0.21), ("バルブ 開", 0.145),
            ("バルブ 閉", 0.145), ("担　当", 0.31)]
    hh = 13 * mm
    rh = (y - margin - 78 * mm - 5 * mm) / rows
    rh = min(rh, 30 * mm)

    # 見出し行
    y -= hh
    cx = x0
    for name, ratio in cols:
        w = fw * ratio
        c.setFillColor(NAVY)
        c.rect(cx, y, w, hh, stroke=0, fill=1)
        centered(c, name, bold, 13, cx, y, w, hh, colors.white)
        cx += w
    # 本体の行
    for i in range(rows):
        y -= rh
        cx = x0
        for j, (_, ratio) in enumerate(cols):
            w = fw * ratio
            c.setFillColor(colors.white if i % 2 == 0 else LIGHT)
            c.rect(cx, y, w, rh, stroke=0, fill=1)
            c.setStrokeColor(LINE)
            c.setLineWidth(0.9)
            c.rect(cx, y, w, rh, stroke=1, fill=0)
            cx += w
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.6)
    c.rect(x0, y, fw, hh + rh * rows, stroke=1, fill=0)

    # ── 締め時確認（必須） ─────────────────────
    y -= 6 * mm
    sh = 72 * mm
    y -= sh
    c.setFillColor(PINK)
    c.rect(x0, y, fw, sh, stroke=0, fill=1)
    c.setStrokeColor(RED)
    c.setLineWidth(2)
    c.rect(x0, y, fw, sh, stroke=1, fill=0)

    bar = 13 * mm
    c.setFillColor(RED)
    c.rect(x0, y + sh - bar, fw, bar, stroke=0, fill=1)
    centered(c, "締め時確認（必須）　バルブを【閉】のまま終業は絶対NG",
             bold, 14, x0, y + sh - bar, fw, bar, colors.white)

    scols = [("時　刻", 0.19), ("オレンジ 30.3〜30.5", 0.26), ("バルブ① 開", 0.17),
             ("バルブ② 開", 0.17), ("担　当", 0.21)]
    shh, srh = 12 * mm, 24 * mm
    sy = y + sh - bar - 4 * mm - shh
    cx = x0 + 4 * mm
    iw = fw - 8 * mm
    for name, ratio in scols:
        w = iw * ratio
        c.setFillColor(NAVY)
        c.rect(cx, sy, w, shh, stroke=0, fill=1)
        centered(c, name, bold, 11.5, cx, sy, w, shh, colors.white)
        cx += w
    cx = x0 + 4 * mm
    for name, ratio in scols:
        w = iw * ratio
        c.setFillColor(colors.white)
        c.rect(cx, sy - srh, w, srh, stroke=0, fill=1)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.9)
        c.rect(cx, sy - srh, w, srh, stroke=1, fill=0)
        cx += w

    c.setFillColor(RED)
    c.setFont(font, 11.5)
    c.drawString(x0 + 5 * mm, y + 5 * mm,
                 "※閉のまま終業すると翌日の水温回復に朝〜夕方までかかり、ガスを通常以上に使用する。")

    # ── 記入方法（最下部） ─────────────────────
    c.setFillColor(colors.HexColor("#555555"))
    c.setFont(font, 10.5)
    c.drawString(x0, margin + 6 * mm,
                 "記入方法：時刻と水温を書き、バルブを操作した方の欄に○。")
    c.drawString(x0, margin,
                 "操作しなかった確認だけの回も、時刻・水温・担当を記入する。")

    c.showPage()
    c.save()
    return path


def main():
    ap = argparse.ArgumentParser(description="ホワイトボード記入レイアウトを作る")
    ap.add_argument("--width", type=float, help="横 mm（既定 A3縦の297）")
    ap.add_argument("--height", type=float, help="縦 mm（既定 A3縦の420）")
    ap.add_argument("--rows", type=int, default=8, help="記録行数（既定8）")
    ap.add_argument("--out", default=None, help="出力先PDF")
    args = ap.parse_args()

    W = args.width * mm if args.width else A3[0]
    H = args.height * mm if args.height else A3[1]
    out = args.out or os.path.join(REPO, "docs", "ホワイトボード記入レイアウト.pdf")
    build(out, W, H, args.rows)
    print(f"{os.path.relpath(out, REPO)}  {W/mm:.0f}×{H/mm:.0f}mm  {args.rows}行")


if __name__ == "__main__":
    main()
