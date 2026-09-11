#!/usr/bin/env python3
"""Excel / CSV の業務データを分析し、Markdown と Excel のレポートを出力する。

使い方の例:
    python3 tools/excel_analyze.py 売上.xlsx
    python3 tools/excel_analyze.py 売上.xlsx --sheet 明細 --groupby 支店 --value 金額
    python3 tools/excel_analyze.py 実績.csv --date 計上日 --out output/2026-09

指定を省略した場合は、列の内容から集計軸と日付列を自動で選ぶ。
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import clean_text, format_number, is_blank, parse_date, parse_number  # noqa: E402

CSV_ENCODINGS = ("utf-8-sig", "cp932", "utf-8", "euc_jp")
MAX_HEADER_SCAN = 20          # タイトル行を探す走査範囲
CATEGORY_MAX_UNIQUE = 30      # 集計軸として扱うカテゴリ数の上限
MISSING_WARN_RATE = 0.30      # 欠損率の警告しきい値


# ---------------------------------------------------------------- 読み込み

def read_table(path: Path, sheet: str | None, header_row: int | None) -> dict[str, pd.DataFrame]:
    """ファイルを読み込み、{シート名: DataFrame} を返す。"""
    if path.suffix.lower() in (".csv", ".tsv", ".txt"):
        sep = "\t" if path.suffix.lower() == ".tsv" else ","
        raw = _read_csv(path, sep)
        return {path.stem: _apply_header(raw, header_row)}

    book = pd.read_excel(path, sheet_name=None, header=None, dtype=object)
    if sheet is not None:
        if sheet not in book:
            raise SystemExit(
                f"シート「{sheet}」が見つかりません。存在するシート: {', '.join(book)}"
            )
        book = {sheet: book[sheet]}
    return {name: _apply_header(frame, header_row) for name, frame in book.items()}


def _read_csv(path: Path, sep: str) -> pd.DataFrame:
    last_error: Exception | None = None
    for encoding in CSV_ENCODINGS:
        try:
            return pd.read_csv(path, sep=sep, header=None, dtype=object, encoding=encoding)
        except UnicodeDecodeError as error:
            last_error = error
    raise SystemExit(f"文字コードを判定できませんでした: {path} ({last_error})")


def detect_header_row(frame: pd.DataFrame) -> int:
    """見出し行の位置を推定する（表の上にタイトル行がある場合に対応）。"""
    scan = min(MAX_HEADER_SCAN, len(frame))
    counts = [
        sum(0 if is_blank(v) else 1 for v in frame.iloc[i].tolist())
        for i in range(scan)
    ]
    if not counts or max(counts) == 0:
        return 0
    threshold = max(counts) * 0.8
    for i, count in enumerate(counts):
        if count < threshold:
            continue
        values = [v for v in frame.iloc[i].tolist() if not is_blank(v)]
        labels = [clean_text(v) for v in values if isinstance(v, str)]
        # 見出しらしさ: 文字列が主体で、重複が少ない
        if len(labels) >= len(values) * 0.7 and len(set(labels)) >= len(labels) * 0.9:
            return i
    return counts.index(max(counts))


def _apply_header(frame: pd.DataFrame, header_row: int | None) -> pd.DataFrame:
    if frame.empty:
        return frame
    row = detect_header_row(frame) if header_row is None else header_row
    header = frame.iloc[row].tolist()
    body = frame.iloc[row + 1:].reset_index(drop=True)

    names: list[str] = []
    seen: dict[str, int] = {}
    for index, value in enumerate(header):
        name = clean_text(value) if not is_blank(value) else f"列{index + 1}"
        name = str(name)
        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 0
        names.append(name)
    body.columns = names
    body.attrs["header_row"] = row
    # 全体が空の行・列を落とす
    body = body.loc[~body.map(is_blank).all(axis=1)]
    keep = [c for c in body.columns if not body[c].map(is_blank).all()]
    dropped = [c for c in body.columns if c not in keep]
    result = body[keep].reset_index(drop=True)
    result.attrs["header_row"] = row
    result.attrs["empty_columns"] = dropped
    return result


# ---------------------------------------------------------------- 型推定

class Column:
    """1 列分の推定結果と変換済みデータ。"""

    def __init__(self, name: str, raw: pd.Series):
        self.name = name
        self.raw = raw
        self.total = len(raw)
        self.blank_mask = raw.map(is_blank)
        self.filled = raw[~self.blank_mask]
        self.kind = "空"
        self.values: pd.Series = self.filled
        self.unparsed: list = []
        self._infer()

    def _infer(self) -> None:
        if self.filled.empty:
            return
        if pd.api.types.is_datetime64_any_dtype(self.raw):
            self.kind = "日付"
            self.values = self.filled.map(parse_date)
            return
        if pd.api.types.is_numeric_dtype(self.raw) and not pd.api.types.is_bool_dtype(self.raw):
            self.kind = "数値"
            self.values = self.filled.astype(float)
            return

        numbers = self.filled.map(parse_number)
        number_rate = numbers.notna().mean()
        if number_rate >= 0.9:
            self.kind = "数値"
            self.values = numbers
            self.unparsed = self.filled[numbers.isna()].tolist()
            return

        dates = self.filled.map(parse_date)
        date_rate = pd.Series([d is not None for d in dates]).mean()
        if date_rate >= 0.9:
            self.kind = "日付"
            self.values = dates
            self.unparsed = [v for v, d in zip(self.filled, dates) if d is None]
            return

        texts = self.filled.map(clean_text)
        unique = texts.nunique()
        limit = max(CATEGORY_MAX_UNIQUE, int(self.total * 0.05))
        self.kind = "カテゴリ" if unique <= limit else "テキスト"
        self.values = texts

    @property
    def missing_rate(self) -> float:
        return float(self.blank_mask.mean()) if self.total else 0.0

    def numeric_series(self) -> pd.Series:
        return pd.Series(self.values, dtype="float64")

    def date_series(self) -> pd.Series:
        return pd.to_datetime(pd.Series(list(self.values)), errors="coerce")


def profile_columns(frame: pd.DataFrame) -> list[Column]:
    return [Column(str(name), frame[name]) for name in frame.columns]


# ---------------------------------------------------------------- 品質チェック

def check_quality(frame: pd.DataFrame, columns: list[Column]) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []

    def add(level: str, target: str, detail: str, action: str) -> None:
        issues.append({"重要度": level, "対象": target, "内容": detail, "対応案": action})

    for name in frame.attrs.get("empty_columns", []):
        add("低", str(name), "全行が空欄の列", "不要であれば削除する")

    duplicated = frame.duplicated(keep=False)
    if duplicated.any():
        rows = [str(i + 2) for i in frame.index[duplicated][:10]]
        add("高", "行全体", f"全列が一致する重複行が {int(duplicated.sum())} 行",
            f"該当行(表内 {', '.join(rows)} 行目付近)を確認し重複を削除する")

    for column in columns:
        if column.missing_rate >= MISSING_WARN_RATE:
            add("中", column.name, f"欠損率 {column.missing_rate:.0%}",
                "入力必須か確認し、不要なら列を整理する")

        if column.unparsed:
            samples = ", ".join(repr(v) for v in column.unparsed[:5])
            add("高", column.name,
                f"{column.kind}列に変換できない値が {len(column.unparsed)} 件 (例: {samples})",
                "入力規則を統一する / 該当セルを修正する")

        if column.kind in ("カテゴリ", "テキスト") and not column.filled.empty:
            strings = column.filled[column.filled.map(lambda v: isinstance(v, str))]
            if not strings.empty:
                untrimmed = strings[strings.map(lambda v: v != v.strip())]
                if not untrimmed.empty:
                    add("低", column.name, f"前後に空白を含むセルが {len(untrimmed)} 件",
                        "トリム処理で統一する")
                normalized = strings.map(clean_text)
                collapsed = normalized.nunique()
                if collapsed < strings.nunique():
                    add("中", column.name,
                        f"表記ゆれの疑い: 正規化すると {strings.nunique()} 種類 → {collapsed} 種類",
                        "全角半角・空白を統一する（マスタ化を検討）")

        if column.kind == "数値" and len(column.numeric_series().dropna()) >= 8:
            series = column.numeric_series().dropna()
            q1, q3 = series.quantile(0.25), series.quantile(0.75)
            iqr = q3 - q1
            if iqr > 0:
                outliers = series[(series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)]
                if not outliers.empty:
                    add("中", column.name,
                        f"外れ値候補 {len(outliers)} 件 (最小 {format_number(outliers.min())} / "
                        f"最大 {format_number(outliers.max())})",
                        "入力ミスか実態かを確認する")

        if column.kind == "日付":
            dates = column.date_series().dropna()
            if not dates.empty:
                today = pd.Timestamp(dt.date.today())
                future = dates[dates > today]
                if not future.empty:
                    add("中", column.name, f"未来日付が {len(future)} 件 (最大 {future.max().date()})",
                        "入力ミスか予定日かを確認する")
                old = dates[dates < pd.Timestamp("1990-01-01")]
                if not old.empty:
                    add("中", column.name, f"1990年より前の日付が {len(old)} 件",
                        "書式違い（シリアル値など）の可能性を確認する")

    return issues


# ---------------------------------------------------------------- 集計

def pick_axes(columns: list[Column], groupby: list[str], values: list[str],
              date_column: str | None) -> tuple[list[str], list[str], str | None]:
    """集計軸・集計値・日付列を決める（未指定なら自動選択）。"""
    by_name = {c.name: c for c in columns}

    if groupby:
        axes = [g for g in groupby if g in by_name]
        missing = [g for g in groupby if g not in by_name]
        if missing:
            raise SystemExit(f"集計軸に指定した列が見つかりません: {', '.join(missing)}")
    else:
        candidates = [
            c for c in columns
            if c.kind == "カテゴリ" and 1 < c.values.nunique() <= CATEGORY_MAX_UNIQUE
        ]
        candidates.sort(key=lambda c: (c.missing_rate, c.values.nunique()))
        axes = [c.name for c in candidates[:3]]

    if values:
        targets = [v for v in values if v in by_name]
        missing = [v for v in values if v not in by_name]
        if missing:
            raise SystemExit(f"集計値に指定した列が見つかりません: {', '.join(missing)}")
    else:
        numeric = [c for c in columns if c.kind == "数値"]
        numeric.sort(key=lambda c: -abs(c.numeric_series().dropna().sum() or 0))
        targets = [c.name for c in numeric[:5]]

    if date_column:
        if date_column not in by_name:
            raise SystemExit(f"日付列に指定した列が見つかりません: {date_column}")
        chosen_date = date_column
    else:
        dated = [c for c in columns if c.kind == "日付"]
        dated.sort(key=lambda c: c.missing_rate)
        chosen_date = dated[0].name if dated else None

    return axes, targets, chosen_date


def build_frame(columns: list[Column]) -> pd.DataFrame:
    """推定型に沿って変換済みの DataFrame を組み立てる。"""
    data: dict[str, pd.Series] = {}
    for column in columns:
        series = pd.Series(index=column.raw.index, dtype="object")
        if column.kind == "数値":
            series = pd.Series(index=column.raw.index, dtype="float64")
            series.loc[column.values.index] = column.numeric_series().to_numpy()
        elif column.kind == "日付":
            converted = pd.to_datetime(pd.Series(list(column.values)), errors="coerce")
            series = pd.Series(index=column.raw.index, dtype="datetime64[ns]")
            series.loc[column.filled.index] = converted.to_numpy()
        else:
            series.loc[column.values.index] = column.values.to_numpy()
        data[column.name] = series
    return pd.DataFrame(data)


def aggregate(frame: pd.DataFrame, axis: str, targets: list[str], top: int,
              normalize: bool = False) -> pd.DataFrame:
    keys = frame[axis].fillna("(空欄)")
    if normalize:
        # 「東京 支店」と「東京支店」のような表記ゆれを同一視する
        keys = keys.map(lambda v: re.sub(r"\s+", "", clean_text(v)) if isinstance(v, str) else v)
    grouped = frame.groupby(keys, dropna=False)
    result = pd.DataFrame({"件数": grouped.size()})
    for target in targets:
        if target == axis or target not in frame.columns:
            continue
        result[f"{target}_合計"] = grouped[target].sum(min_count=1)
        result[f"{target}_平均"] = grouped[target].mean()
    sort_key = next((c for c in result.columns if c.endswith("_合計")), "件数")
    result = result.sort_values(sort_key, ascending=False)
    if len(result) > top:
        head = result.head(top).copy()
        rest = result.iloc[top:].sum(numeric_only=True)
        rest.name = f"その他({len(result) - top}件)"
        result = pd.concat([head, rest.to_frame().T])
    result.index.name = axis
    total = result.sum(numeric_only=True)
    for column in result.columns:
        if column.endswith("_平均"):
            total[column] = frame[column.removesuffix("_平均")].mean()
    total.name = "合計"
    return pd.concat([result, total.to_frame().T])


def monthly_trend(frame: pd.DataFrame, date_column: str, targets: list[str]) -> pd.DataFrame:
    dates = pd.to_datetime(frame[date_column], errors="coerce")
    valid = frame[dates.notna()].copy()
    if valid.empty:
        return pd.DataFrame()
    valid["_月"] = dates[dates.notna()].dt.to_period("M").astype(str)
    grouped = valid.groupby("_月")
    result = pd.DataFrame({"件数": grouped.size()})
    for target in targets:
        if target in valid.columns and target != date_column:
            result[f"{target}_合計"] = grouped[target].sum(min_count=1)
    result.index.name = "年月"
    for column in [c for c in result.columns if c.endswith("_合計") or c == "件数"]:
        result[f"{column}_前月比"] = result[column].pct_change().map(
            lambda v: "" if pd.isna(v) else f"{v:+.1%}"
        )
    return result


# ---------------------------------------------------------------- 出力

def frame_to_markdown(frame: pd.DataFrame, index_label: str | None = None) -> str:
    if frame.empty:
        return "(該当データなし)\n"
    display = frame.copy()
    for column in display.columns:
        display[column] = display[column].map(
            lambda v: format_number(v) if isinstance(v, (int, float)) else ("" if pd.isna(v) else str(v))
        )
    if index_label is not None:
        display.insert(0, index_label, [str(i) for i in frame.index])
    header = "| " + " | ".join(str(c) for c in display.columns) + " |"
    divider = "| " + " | ".join("---" for _ in display.columns) + " |"
    rows = ["| " + " | ".join(str(v) for v in row) + " |" for row in display.to_numpy()]
    return "\n".join([header, divider, *rows]) + "\n"


def build_report(path: Path, sheets: dict[str, dict], args) -> str:
    lines = [
        f"# データ分析レポート: {path.name}",
        "",
        f"- 作成日: {dt.date.today():%Y-%m-%d}",
        f"- 対象ファイル: `{path}`",
        f"- 対象シート: {', '.join(sheets)}",
        "",
    ]
    for name, result in sheets.items():
        frame: pd.DataFrame = result["frame"]
        columns: list[Column] = result["columns"]
        lines += [
            f"## シート: {name}",
            "",
            f"- 行数: {len(frame):,} 行 / 列数: {len(frame.columns)} 列",
            f"- 見出し行: {result['header_row'] + 1} 行目",
            "",
            "### 列プロファイル",
            "",
        ]
        profile = pd.DataFrame([
            {
                "列名": c.name,
                "種別": c.kind,
                "入力あり": f"{c.total - int(c.blank_mask.sum()):,}",
                "欠損率": f"{c.missing_rate:.0%}",
                "ユニーク数": f"{c.values.nunique():,}" if c.kind != "数値" else "",
                "代表値": result["summaries"][c.name],
            }
            for c in columns
        ])
        lines += [frame_to_markdown(profile), ""]

        issues = result["issues"]
        lines += ["### データ品質チェック", ""]
        if issues:
            order = {"高": 0, "中": 1, "低": 2}
            issues = sorted(issues, key=lambda i: order.get(i["重要度"], 3))
            lines += [frame_to_markdown(pd.DataFrame(issues)), ""]
        else:
            lines += ["目立つ問題は検出されませんでした。", ""]

        for axis, table in result["aggregations"].items():
            lines += [f"### 集計: {axis} 別", "", frame_to_markdown(table, axis), ""]

        if not result["trend"].empty:
            lines += [
                f"### 月次推移（{result['date_column']} 基準）",
                "",
                frame_to_markdown(result["trend"], "年月"),
                "",
            ]
    lines += [
        "---",
        "",
        "本レポートは `tools/excel_analyze.py` で自動生成しています。"
        "集計軸を変えたい場合は `--groupby` / `--value` / `--date` を指定してください。",
        "",
    ]
    return "\n".join(lines)


def write_excel(out_path: Path, sheets: dict[str, dict]) -> None:
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        for name, result in sheets.items():
            prefix = name[:20]
            profile = pd.DataFrame([
                {
                    "列名": c.name,
                    "種別": c.kind,
                    "入力あり": c.total - int(c.blank_mask.sum()),
                    "欠損率": round(c.missing_rate, 4),
                    "ユニーク数": c.values.nunique(),
                    "代表値": result["summaries"][c.name],
                }
                for c in result["columns"]
            ])
            profile.to_excel(writer, sheet_name=f"{prefix}_列"[:31], index=False)
            issues = pd.DataFrame(result["issues"]) if result["issues"] else pd.DataFrame(
                [{"重要度": "-", "対象": "-", "内容": "問題なし", "対応案": "-"}]
            )
            issues.to_excel(writer, sheet_name=f"{prefix}_品質"[:31], index=False)
            for index, (axis, table) in enumerate(result["aggregations"].items(), start=1):
                table.to_excel(writer, sheet_name=f"{prefix}_集計{index}"[:31])
            if not result["trend"].empty:
                result["trend"].to_excel(writer, sheet_name=f"{prefix}_月次"[:31])


def summarize_column(column: Column) -> str:
    if column.filled.empty:
        return "(全て空欄)"
    if column.kind == "数値":
        series = column.numeric_series().dropna()
        if series.empty:
            return ""
        return (f"合計 {format_number(series.sum())} / 平均 {format_number(series.mean())} / "
                f"最小 {format_number(series.min())} / 最大 {format_number(series.max())}")
    if column.kind == "日付":
        dates = column.date_series().dropna()
        if dates.empty:
            return ""
        return f"{dates.min():%Y-%m-%d} 〜 {dates.max():%Y-%m-%d}"
    counts = column.values.value_counts().head(3)
    return " / ".join(f"{index}({value}件)" for index, value in counts.items())


# ---------------------------------------------------------------- エントリポイント

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Excel / CSV を分析してレポートを出力する",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="入力ファイル (.xlsx / .xls / .csv / .tsv)")
    parser.add_argument("--sheet", help="対象シート名（省略時は全シート）")
    parser.add_argument("--header-row", type=int, help="見出し行の位置（0 始まり、省略時は自動判定）")
    parser.add_argument("--groupby", help="集計軸の列名（カンマ区切り、省略時は自動選択）")
    parser.add_argument("--value", help="集計する数値列（カンマ区切り、省略時は自動選択）")
    parser.add_argument("--date", help="月次推移に使う日付列（省略時は自動選択）")
    parser.add_argument("--top", type=int, default=15, help="集計表に表示する上位件数（既定: 15）")
    parser.add_argument("--out", default="output", help="出力先ディレクトリ（既定: output）")
    parser.add_argument("--normalize", action="store_true",
                        help="集計軸の表記ゆれ（全角半角・空白）を統合して集計する")
    parser.add_argument("--no-xlsx", action="store_true", help="Excel レポートを出力しない")
    args = parser.parse_args(argv)

    path = Path(args.input)
    if not path.exists():
        raise SystemExit(f"ファイルが見つかりません: {path}")

    groupby = [c.strip() for c in args.groupby.split(",")] if args.groupby else []
    values = [c.strip() for c in args.value.split(",")] if args.value else []

    tables = read_table(path, args.sheet, args.header_row)
    sheets: dict[str, dict] = {}
    for name, raw in tables.items():
        if raw.empty:
            print(f"[スキップ] シート「{name}」にデータ行がありません")
            continue
        columns = profile_columns(raw)
        frame = build_frame(columns)
        axes, targets, date_column = pick_axes(columns, groupby, values, args.date)
        aggregations = {
            axis: aggregate(frame, axis, targets, args.top, args.normalize)
            for axis in axes
        }
        trend = (monthly_trend(frame, date_column, targets)
                 if date_column else pd.DataFrame())
        sheets[name] = {
            "frame": frame,
            "columns": columns,
            "header_row": raw.attrs.get("header_row", 0),
            "summaries": {c.name: summarize_column(c) for c in columns},
            "issues": check_quality(raw, columns),
            "aggregations": aggregations,
            "trend": trend,
            "date_column": date_column,
        }

    if not sheets:
        raise SystemExit("分析できるデータがありませんでした。")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{path.stem}_分析_{dt.date.today():%Y%m%d}"

    report_path = out_dir / f"{stem}.md"
    report_path.write_text(build_report(path, sheets, args), encoding="utf-8")
    print(f"[出力] Markdown レポート: {report_path}")

    if not args.no_xlsx:
        excel_path = out_dir / f"{stem}.xlsx"
        write_excel(excel_path, sheets)
        print(f"[出力] Excel レポート: {excel_path}")

    for name, result in sheets.items():
        high = sum(1 for i in result["issues"] if i["重要度"] == "高")
        print(f"  - {name}: {len(result['frame']):,} 行 / 要確認(高) {high} 件")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:  # head などにパイプした場合
        sys.stderr.close()
        raise SystemExit(0)
