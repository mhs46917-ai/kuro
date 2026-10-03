# -*- coding: utf-8 -*-
"""日本語フォントをOSごとに自動検出して ReportLab に登録する。

環境変数 MANUAL_FONT に TTF/TTC のパスを指定すると、それを最優先で使用する。
"""
import os
import sys

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_NAME = "ManualJP"
FONT_NAME_BOLD = "ManualJP-Bold"

# (パス, TTCのサブフォント番号) を優先順に並べる
CANDIDATES = {
    "win32": [
        (r"C:\Windows\Fonts\meiryo.ttc", 0, r"C:\Windows\Fonts\meiryob.ttc", 0),
        (r"C:\Windows\Fonts\YuGothM.ttc", 0, r"C:\Windows\Fonts\YuGothB.ttc", 0),
        (r"C:\Windows\Fonts\YuGothR.ttc", 0, r"C:\Windows\Fonts\YuGothB.ttc", 0),
        (r"C:\Windows\Fonts\msgothic.ttc", 0, None, 0),
    ],
    "darwin": [
        ("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc", 0,
         "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc", 0),
        ("/System/Library/Fonts/Hiragino Sans GB.ttc", 0, None, 0),
        ("/Library/Fonts/Arial Unicode.ttf", 0, None, 0),
    ],
    "linux": [
        ("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf", 0,
         "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf", 0),
        ("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", 0, None, 0),
        ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 0,
         "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 0),
        ("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", 0, None, 0),
    ],
}


def _platform_key():
    if sys.platform.startswith("win"):
        return "win32"
    if sys.platform == "darwin":
        return "darwin"
    return "linux"


def _register(path, index, bold_path, bold_index):
    pdfmetrics.registerFont(TTFont(FONT_NAME, path, subfontIndex=index))
    if bold_path and os.path.exists(bold_path):
        pdfmetrics.registerFont(TTFont(FONT_NAME_BOLD, bold_path, subfontIndex=bold_index))
    else:
        pdfmetrics.registerFont(TTFont(FONT_NAME_BOLD, path, subfontIndex=index))
    pdfmetrics.registerFontFamily(
        FONT_NAME, normal=FONT_NAME, bold=FONT_NAME_BOLD,
        italic=FONT_NAME, boldItalic=FONT_NAME_BOLD)
    return FONT_NAME


def register_japanese_font():
    """登録したフォント名（通常体）を返す。見つからない場合は例外。"""
    override = os.environ.get("MANUAL_FONT")
    if override:
        if not os.path.exists(override):
            raise FileNotFoundError(f"MANUAL_FONT が見つかりません: {override}")
        return _register(override, int(os.environ.get("MANUAL_FONT_INDEX", "0")), None, 0)

    for path, index, bold_path, bold_index in CANDIDATES[_platform_key()]:
        if os.path.exists(path):
            return _register(path, index, bold_path, bold_index)

    # 最後の手段：ReportLab 内蔵のCIDフォント（埋め込みなし。多くのビューアで表示可）
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
    pdfmetrics.registerFontFamily("HeiseiKakuGo-W5", normal="HeiseiKakuGo-W5",
                                  bold="HeiseiKakuGo-W5", italic="HeiseiKakuGo-W5",
                                  boldItalic="HeiseiKakuGo-W5")
    print("[警告] 日本語TTFが見つからないため内蔵CIDフォントを使用します（埋め込みなし）。")
    return "HeiseiKakuGo-W5"
