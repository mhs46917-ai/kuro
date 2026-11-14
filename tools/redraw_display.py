# -*- coding: utf-8 -*-
"""温調器など7セグメント表示の数値を、マニュアル記載値に描き直す。

実機の表示をそのまま載せると記載値と食い違うため、表示例として数値を差し替える。
使用例（冬季熱交換器操作の制御盤写真）:

    import sys; sys.path.insert(0, "tools")
    from PIL import Image
    import redraw_display as rd

    im = Image.open("docs/images/winter-heat-exchanger/04-controller.jpg").convert("RGB")
    rd.put_number(im, (190, 211, 325, 280), 330, "30.5", w=29, h=54, t=7.5, gap=5,
                  color=(126, 240, 44))          # 緑（pv）＝現在水温
    rd.put_number(im, (205, 288, 322, 347), 330, "30.4", w=25, h=46, t=6.5, gap=4,
                  color=(246, 150, 26))          # オレンジ（sp）＝設定値
    im.save("docs/images/winter-heat-exchanger/04-controller.jpg", quality=92)

box は塗りつぶす範囲、sample_x は背景色を拾う列（表示窓内の数字が無い位置）。
"""
from PIL import Image, ImageDraw, ImageFilter

SEGMENTS = {
    "0": "abcdef", "1": "bc", "2": "abged", "3": "abgcd", "4": "fgbc",
    "5": "afgcd", "6": "afgedc", "7": "abc", "8": "abcdefg", "9": "abcdfg",
}


def _polys(x, y, w, h, t, g):
    hm = y + h / 2.0
    return {
        "a": [(x + g, y), (x + w - g, y), (x + w - g - t, y + t), (x + g + t, y + t)],
        "g": [(x + g + t * 0.5, hm - t / 2), (x + w - g - t * 0.5, hm - t / 2),
              (x + w - g - t * 0.5, hm + t / 2), (x + g + t * 0.5, hm + t / 2)],
        "d": [(x + g + t, y + h - t), (x + w - g - t, y + h - t),
              (x + w - g, y + h), (x + g, y + h)],
        "f": [(x, y + g), (x + t, y + g + t), (x + t, hm - t / 2 - g), (x, hm - g)],
        "b": [(x + w, y + g), (x + w, hm - g), (x + w - t, hm - t / 2 - g),
              (x + w - t, y + g + t)],
        "e": [(x, hm + g), (x + t, hm + t / 2 + g), (x + t, y + h - t - g), (x, y + h - g)],
        "c": [(x + w, hm + g), (x + w, y + h - g), (x + w - t, y + h - t - g),
              (x + w - t, hm + t / 2 + g)],
    }


def _skew(pts, y_base, slant):
    return [(px + (y_base - py) * slant, py) for px, py in pts]


def _draw(draw, text, x, y, w, h, t, gap, fill, slant):
    cx = float(x)
    for ch in text:
        if ch == ".":
            s = t * 0.95
            draw.rectangle([cx, y + h - s, cx + s, y + h], fill=fill)
            cx += s + gap
            continue
        for seg in SEGMENTS[ch]:
            draw.polygon(_skew(_polys(cx, y, w, h, t, t * 0.28)[seg], y + h, slant), fill=fill)
        cx += w + gap


def flatten_background(img, box, sample_x):
    """表示窓の同じ行から背景色を拾い、box をその色で塗って数字を消す。"""
    x0, y0, x1, y1 = box
    px = img.load()
    for yy in range(y0, y1):
        r = g = b = 0
        for sx in range(sample_x, sample_x + 6):
            c = px[sx, yy]
            r, g, b = r + c[0], g + c[1], b + c[2]
        col = (r // 6, g // 6, b // 6)
        for xx in range(x0, x1):
            px[xx, yy] = col


def put_number(img, box, sample_x, text, w, h, t, gap, color, slant=0.05):
    x0, y0, x1, y1 = box
    flatten_background(img, box, sample_x)
    mask = Image.new("L", img.size, 0)
    _draw(ImageDraw.Draw(mask), text, x0, y0, w, h, t, gap, 255, slant)
    glow = mask.filter(ImageFilter.GaussianBlur(4)).point(lambda v: v // 7)
    img.paste(Image.new("RGB", img.size, color), (0, 0), glow)
    img.paste(Image.new("RGB", img.size, color), (0, 0), mask)
