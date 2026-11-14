# -*- coding: utf-8 -*-
"""写真に番号マーカーと凡例を焼き込む。

全体図に「ここが何か」を書き込むためのもの。マニュアル生成時ではなく
画像の準備段階で使う（docs/images/<slug>/ の写真を直接書き換える）。

使用例:
    import sys; sys.path.insert(0, "tools")
    import annotate_image as ann
    ann.annotate(
        "docs/images/winter-heat-exchanger/01-overview.jpg",
        marks=[
            {"n": "1", "target": (1090, 670), "label_at": (1180, 430), "color": "red"},
        ],
        legend=["① …", "② …"],
    )
"""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
COLORS = {
    "red": (217, 48, 37),
    "blue": (26, 115, 232),
    "navy": (31, 58, 95),
}


def _font(size):
    return ImageFont.truetype(FONT, size)


def annotate(path, marks, legend, out=None, badge_r=46, ring_r=78,
             legend_size=44, dash=False):
    im = Image.open(path).convert("RGB")
    W, H = im.size
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)

    for m in marks:
        c = COLORS[m.get("color", "red")] + (255,)
        tx, ty = m["target"]
        lx, ly = m.get("label_at", (tx, ty - 160))
        r = m.get("ring_r", ring_r)
        # 対象を囲む円（点線指定なら破線で描く）
        if m.get("dashed"):
            for a in range(0, 360, 18):
                d.arc([tx - r, ty - r, tx + r, ty + r], a, a + 10, fill=c, width=9)
        else:
            d.ellipse([tx - r, ty - r, tx + r, ty + r], outline=c, width=9)
        # バッジへの引き出し線
        d.line([(lx, ly), (tx, ty)], fill=c, width=7)
        # 番号バッジ
        d.ellipse([lx - badge_r, ly - badge_r, lx + badge_r, ly + badge_r],
                  fill=c, outline=(255, 255, 255, 255), width=6)
        f = _font(int(badge_r * 1.4))
        t = m["n"]
        bb = d.textbbox((0, 0), t, font=f)
        d.text((lx - (bb[2] - bb[0]) / 2 - bb[0], ly - (bb[3] - bb[1]) / 2 - bb[1]),
               t, font=f, fill=(255, 255, 255, 255))

    # 下部の凡例
    if legend:
        f = _font(legend_size)
        pad, gap = 26, 16
        line_h = legend_size + gap
        box_h = line_h * len(legend) + pad * 2 - gap
        y0 = H - box_h
        d.rectangle([0, y0, W, H], fill=(16, 24, 38, 232))
        for i, line in enumerate(legend):
            d.text((pad, y0 + pad + i * line_h), line, font=f, fill=(255, 255, 255, 255))

    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    im.save(out or path, "JPEG", quality=88, optimize=True)
    return out or path
