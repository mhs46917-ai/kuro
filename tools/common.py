"""業務データ処理の共通ユーティリティ。

Excel 分析・画像データ化の双方から利用する。日本の業務データにありがちな
表記ゆれ（全角数字、通貨記号、和暦、「―」による空欄表現など）を吸収する。
"""

from __future__ import annotations

import datetime as _dt
import re
import unicodedata
from typing import Any

# 空欄として扱う文字列（半角化・strip 後に比較する）
NULL_TOKENS = {
    "", "-", "--", "---", "ー", "―", "‐", "–", "—",
    "なし", "無し", "N/A", "n/a", "NA", "null", "NULL", "None", "該当なし", "#N/A",
}

_CURRENCY_CHARS = "¥￥$＄円"
_NUM_NOISE = re.compile(r"[,\s，、" + _CURRENCY_CHARS + r"]")
_PAREN_NEGATIVE = re.compile(r"^\((.+)\)$|^（(.+)）$")

# 和暦の元号と開始日（改元日）
_ERAS = {
    "令和": (2018, _dt.date(2019, 5, 1)),   # 令和N年 = 2018 + N
    "R": (2018, _dt.date(2019, 5, 1)),
    "平成": (1988, _dt.date(1989, 1, 8)),
    "H": (1988, _dt.date(1989, 1, 8)),
    "昭和": (1925, _dt.date(1926, 12, 25)),
    "S": (1925, _dt.date(1926, 12, 25)),
}
_WAREKI = re.compile(
    r"^(令和|平成|昭和|R|H|S)\s*(元|\d{1,2})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日?$"
)
_YMD = re.compile(r"^(\d{4})\s*[-/年.]\s*(\d{1,2})\s*[-/月.]\s*(\d{1,2})\s*日?$")
_YM = re.compile(r"^(\d{4})\s*[-/年.]\s*(\d{1,2})\s*月?$")


def to_hankaku(value: Any) -> Any:
    """全角英数記号を半角へ正規化する（日本語かなカナはそのまま）。"""
    if not isinstance(value, str):
        return value
    # NFKC はカタカナ半角も全角化してくれるため、表記統一に都合が良い
    return unicodedata.normalize("NFKC", value)


def clean_text(value: Any) -> Any:
    """文字列の前後空白・連続空白・改行を整理する。"""
    if not isinstance(value, str):
        return value
    text = to_hankaku(value).replace("　", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_blank(value: Any) -> bool:
    """空欄とみなせる値か判定する。"""
    if value is None:
        return True
    if isinstance(value, float) and value != value:  # NaN
        return True
    if isinstance(value, str):
        return clean_text(value) in NULL_TOKENS
    return False


def parse_number(value: Any) -> float | None:
    """「1,234円」「▲500」「(1,200)」「１２３」などを数値へ変換する。

    変換できない場合は None を返す（例外は投げない）。
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return None if (isinstance(value, float) and value != value) else float(value)
    if not isinstance(value, str):
        return None

    text = clean_text(value)
    if text in NULL_TOKENS:
        return None

    negative = False
    matched = _PAREN_NEGATIVE.match(text)
    if matched:
        negative = True
        text = matched.group(1) or matched.group(2) or ""
    for mark in ("▲", "△", "−", "－"):
        if text.startswith(mark):
            negative = True
            text = text[len(mark):]

    percent = text.endswith("%")
    if percent:
        text = text[:-1]

    text = _NUM_NOISE.sub("", text)
    if text in ("", "-", "+", "."):
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if percent:
        number /= 100.0
    return -number if negative else number


def parse_date(value: Any) -> _dt.date | None:
    """西暦・和暦・日付風文字列を date へ変換する。失敗時は None。"""
    if value is None:
        return None
    if isinstance(value, _dt.datetime):
        return value.date()
    if isinstance(value, _dt.date):
        return value
    if isinstance(value, (int, float)):
        # Excel シリアル値（1900 日付システム）とみなす
        try:
            serial = int(value)
        except (ValueError, OverflowError):
            return None
        if 1 <= serial <= 60000:
            base = _dt.date(1899, 12, 30)
            return base + _dt.timedelta(days=serial)
        return None
    if not isinstance(value, str):
        return None

    text = clean_text(value)
    if text in NULL_TOKENS:
        return None

    matched = _WAREKI.match(text)
    if matched:
        era, year_text, month, day = matched.groups()
        offset, era_start = _ERAS[era]
        year = offset + (1 if year_text == "元" else int(year_text))
        try:
            parsed = _dt.date(year, int(month), int(day))
        except ValueError:
            return None
        return parsed if parsed >= era_start else None

    matched = _YMD.match(text)
    if matched:
        year, month, day = (int(g) for g in matched.groups())
        try:
            return _dt.date(year, month, day)
        except ValueError:
            return None

    matched = _YM.match(text)
    if matched:
        year, month = (int(g) for g in matched.groups())
        try:
            return _dt.date(year, month, 1)
        except ValueError:
            return None
    return None


def format_number(value: Any, digits: int = 2) -> str:
    """レポート表示用に数値を整形する（整数は小数点を出さない）。"""
    if value is None:
        return ""
    if isinstance(value, float) and value != value:
        return ""
    if isinstance(value, (int, float)):
        if float(value).is_integer() and abs(value) < 1e15:
            return f"{int(value):,}"
        return f"{value:,.{digits}f}"
    return str(value)
