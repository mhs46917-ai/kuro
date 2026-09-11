#!/usr/bin/env python3
"""画像（帳票・伝票・ホワイトボード等）から起こしたデータを検証し、表形式に変換する。

想定する流れ:
    1. 項目定義を用意する      python3 tools/image_to_data.py init --fields fields/受領書.yaml
    2. 読み取り指示文を出力    python3 tools/image_to_data.py prompt --fields fields/受領書.yaml
       → 出力された指示文と画像を Claude に渡し、JSON で書き出してもらう
    3. 検証して表に変換        python3 tools/image_to_data.py build --fields fields/受領書.yaml data.json

画像の読み取り自体は Claude（または OCR）が行い、本スクリプトは
「項目定義どおりか」「数値・日付として妥当か」を機械的に検証して
Excel / CSV に落とす役割を持つ。転記ミスを人手で探さずに済ませるための道具。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import pandas as pd
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import clean_text, is_blank, parse_date, parse_number, to_hankaku  # noqa: E402

FIELD_TEMPLATE = """\
# 画像から読み取る項目の定義
# type: text（文字列） / number（数値） / date（日付） / code（記号・番号）

name: {name}
description: "読み取り対象の帳票について簡単に説明します（例: 取引先から届く受領書）"

fields:
  - key: 伝票番号
    type: code
    required: true
    unique: true      # 同じ値が複数あれば重複として指摘する
    pattern: "^[A-Z]-?\\\\d{{4,6}}$"
    hint: 右上に印字されている番号

  - key: 日付
    type: date
    required: true
    hint: 和暦の場合もそのまま書き写してよい（自動で西暦に変換される）

  - key: 取引先名
    type: text
    required: true

  - key: 品名
    type: text
    required: true

  - key: 数量
    type: number
    required: true
    min: 0

  - key: 金額
    type: number
    required: false
    min: 0

  - key: 区分
    type: text
    required: false
    choices: [新規, 継続, 返品]

  - key: 備考
    type: text
    required: false
"""


# ---------------------------------------------------------------- 項目定義

def load_fields(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"項目定義が見つかりません: {path}（init サブコマンドで作成できます）")
    try:
        definition = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as error:
        raise SystemExit(
            f"YAML を読み込めません: {path}\n{error}\n"
            "ヒント: 値に「: 」や「#」を含める場合は \"二重引用符\" で囲んでください。"
        )
    if not isinstance(definition, dict) or not definition.get("fields"):
        raise SystemExit("項目定義に fields がありません。")
    for field in definition["fields"]:
        if not field.get("key"):
            raise SystemExit("fields の各項目には key が必要です。")
        field.setdefault("type", "text")
        if field["type"] not in ("text", "number", "date", "code"):
            raise SystemExit(f"不明な type です: {field['type']}（{field['key']}）")
    return definition


def build_prompt(definition: dict) -> str:
    """画像を読み取らせるための指示文を組み立てる。"""
    lines = [
        f"# 読み取り指示: {definition.get('name', '帳票')}",
        "",
        "添付した画像から、下記の項目を読み取って JSON 配列で出力してください。",
        "",
    ]
    if definition.get("description"):
        lines += [str(definition["description"]).strip(), ""]
    lines += ["## 読み取る項目", ""]
    lines += ["| 項目名 | 種別 | 必須 | 指示 |", "| --- | --- | --- | --- |"]
    type_label = {"text": "文字列", "number": "数値", "date": "日付", "code": "番号・記号"}
    for field in definition["fields"]:
        notes = []
        if field.get("hint"):
            notes.append(str(field["hint"]))
        if field.get("choices"):
            notes.append("次のいずれか: " + " / ".join(str(c) for c in field["choices"]))
        if field.get("pattern"):
            notes.append(f"形式: {field['pattern']}")
        lines.append(
            f"| {field['key']} | {type_label.get(field['type'], field['type'])} | "
            f"{'必須' if field.get('required') else '任意'} | {' / '.join(notes)} |"
        )

    sample = {field["key"]: "" for field in definition["fields"]}
    sample["_source"] = "画像ファイル名"
    lines += [
        "",
        "## 出力ルール",
        "",
        "- 1 レコード（伝票 1 枚、明細 1 行）につき JSON オブジェクト 1 つ",
        "- 画像に写っている値をそのまま書き写す。単位や桁区切りは付けたままでよい",
        "- 読み取れない・記載がない項目は空文字 \"\" にする（推測で埋めない）",
        "- 判読に自信がない値は `_confidence` に \"低\" と記録し、`_note` に理由を書く",
        "- どの画像から読んだかを `_source` に必ず記録する",
        "",
        "## 出力形式",
        "",
        "```json",
        json.dumps([sample], ensure_ascii=False, indent=2),
        "```",
        "",
        "出力した JSON をファイルに保存し、次のコマンドで検証してください。",
        "",
        "```",
        "python3 tools/image_to_data.py build --fields <項目定義.yaml> <保存したJSON>",
        "```",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------- 検証

def load_records(paths: list[Path]) -> list[dict]:
    records: list[dict] = []
    for path in paths:
        if not path.exists():
            raise SystemExit(f"データファイルが見つかりません: {path}")
        text = path.read_text(encoding="utf-8").strip()
        # ```json ... ``` で囲まれていても読めるようにする
        fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
        if fenced:
            text = fenced.group(1).strip()
        try:
            data = json.loads(text)
        except json.JSONDecodeError as error:
            raise SystemExit(f"JSON として読み込めません: {path} ({error})")
        if isinstance(data, dict):
            data = data.get("records") or [data]
        if not isinstance(data, list):
            raise SystemExit(f"JSON は配列（またはrecordsキー）である必要があります: {path}")
        for record in data:
            if isinstance(record, dict):
                record.setdefault("_source", path.name)
                records.append(record)
    return records


def validate_record(record: dict, fields: list[dict], row_no: int) -> tuple[dict, list[dict]]:
    """1 レコードを検証・正規化し、(整形済みレコード, 指摘リスト) を返す。"""
    cleaned: dict = {}
    issues: list[dict] = []

    def add(level: str, key: str, message: str) -> None:
        issues.append({"行": row_no, "出典": record.get("_source", ""),
                       "項目": key, "重要度": level, "内容": message})

    for field in fields:
        key = field["key"]
        raw = record.get(key)
        if key not in record:
            add("中", key, "項目自体が出力されていません")

        if is_blank(raw):
            cleaned[key] = None
            if field.get("required"):
                add("高", key, "必須項目が空です")
            continue

        if field["type"] == "number":
            value = parse_number(raw)
            if value is None:
                add("高", key, f"数値として読めません: {raw!r}")
                cleaned[key] = raw
                continue
            if field.get("min") is not None and value < field["min"]:
                add("高", key, f"下限 {field['min']} を下回っています: {value}")
            if field.get("max") is not None and value > field["max"]:
                add("高", key, f"上限 {field['max']} を超えています: {value}")
            cleaned[key] = int(value) if float(value).is_integer() else value

        elif field["type"] == "date":
            value = parse_date(raw)
            if value is None:
                add("高", key, f"日付として読めません: {raw!r}")
                cleaned[key] = raw
                continue
            if value > dt.date.today():
                add("中", key, f"未来日付です: {value}")
            cleaned[key] = value.isoformat()

        elif field["type"] == "code":
            value = to_hankaku(str(raw)).strip().upper() if field.get("upper", True) \
                else to_hankaku(str(raw)).strip()
            if field.get("pattern") and not re.match(field["pattern"], value):
                add("高", key, f"形式が一致しません（{field['pattern']}）: {value}")
            cleaned[key] = value

        else:  # text
            value = clean_text(str(raw))
            if field.get("choices") and value not in [str(c) for c in field["choices"]]:
                add("中", key, f"選択肢にない値です（{'/'.join(map(str, field['choices']))}）: {value}")
            if field.get("max_length") and len(value) > field["max_length"]:
                add("中", key, f"{field['max_length']} 文字を超えています: {len(value)} 文字")
            cleaned[key] = value

    known = {f["key"] for f in fields}
    for key in record:
        if key not in known and not key.startswith("_"):
            add("低", key, "項目定義にない項目が含まれています")

    if str(record.get("_confidence", "")).strip() in ("低", "low", "LOW"):
        add("中", "-", f"読み取り自信度が低い記録です: {record.get('_note', '')}")

    cleaned["_出典"] = record.get("_source", "")
    cleaned["_メモ"] = record.get("_note", "")
    return cleaned, issues


def find_duplicates(frame: pd.DataFrame, fields: list[dict]) -> list[dict]:
    """一意であるべき項目（code かつ unique）の重複を検出する。"""
    issues: list[dict] = []
    for field in fields:
        if field["type"] != "code" or not field.get("unique"):
            continue
        key = field["key"]
        if key not in frame.columns:
            continue
        duplicated = frame[key][frame[key].duplicated(keep=False) & frame[key].notna()]
        for index, value in duplicated.items():
            issues.append({"行": index + 1, "出典": frame.at[index, "_出典"], "項目": key,
                           "重要度": "高", "内容": f"重複した値です: {value}"})
    return issues


# ---------------------------------------------------------------- 出力

def write_outputs(frame: pd.DataFrame, issues: list[dict], out_dir: Path, stem: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / f"{stem}.csv"
    frame.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"[出力] CSV: {csv_path}")

    excel_path = out_dir / f"{stem}.xlsx"
    issue_frame = pd.DataFrame(issues) if issues else pd.DataFrame(
        [{"行": "-", "出典": "-", "項目": "-", "重要度": "-", "内容": "指摘なし"}]
    )
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        frame.to_excel(writer, sheet_name="データ", index=False)
        issue_frame.to_excel(writer, sheet_name="検証結果", index=False)
    print(f"[出力] Excel: {excel_path}")


# ---------------------------------------------------------------- エントリポイント

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="画像から起こしたデータを検証して表形式に変換する",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="項目定義のひな形を作成する")
    init.add_argument("--fields", required=True, help="作成する項目定義ファイル (.yaml)")

    prompt = sub.add_parser("prompt", help="画像読み取り用の指示文を出力する")
    prompt.add_argument("--fields", required=True, help="項目定義ファイル (.yaml)")
    prompt.add_argument("--out", help="指示文の保存先（省略時は標準出力）")

    build = sub.add_parser("build", help="読み取り結果の JSON を検証して表にする")
    build.add_argument("json", nargs="+", help="読み取り結果の JSON ファイル")
    build.add_argument("--fields", required=True, help="項目定義ファイル (.yaml)")
    build.add_argument("--out", default="output", help="出力先ディレクトリ（既定: output）")
    build.add_argument("--strict", action="store_true",
                       help="重要度『高』の指摘があれば異常終了する")

    args = parser.parse_args(argv)

    if args.command == "init":
        path = Path(args.fields)
        if path.exists():
            raise SystemExit(f"既にファイルが存在します: {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(FIELD_TEMPLATE.format(name=path.stem), encoding="utf-8")
        print(f"[作成] 項目定義のひな形: {path}")
        print("項目を編集したあと、prompt サブコマンドで読み取り指示文を出力できます。")
        return 0

    definition = load_fields(Path(args.fields))

    if args.command == "prompt":
        text = build_prompt(definition)
        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(text, encoding="utf-8")
            print(f"[出力] 読み取り指示文: {out_path}")
        else:
            print(text)
        return 0

    records = load_records([Path(p) for p in args.json])
    if not records:
        raise SystemExit("レコードが 1 件もありません。")

    fields = definition["fields"]
    rows: list[dict] = []
    issues: list[dict] = []
    for index, record in enumerate(records, start=1):
        cleaned, record_issues = validate_record(record, fields, index)
        rows.append(cleaned)
        issues += record_issues

    order = [f["key"] for f in fields] + ["_出典", "_メモ"]
    frame = pd.DataFrame(rows)[order]

    # 空欄があると整数列が小数表示になるため、整数のみの列は Int64 に寄せる
    for field in fields:
        if field["type"] != "number":
            continue
        column = frame[field["key"]]
        values = column.dropna()
        if not values.empty and all(
            isinstance(v, int) or (isinstance(v, float) and float(v).is_integer())
            for v in values
        ):
            frame[field["key"]] = column.astype("Int64")
    issues += find_duplicates(frame, fields)

    high = sum(1 for i in issues if i["重要度"] == "高")
    medium = sum(1 for i in issues if i["重要度"] == "中")

    levels = {"高": 0, "中": 1, "低": 2}
    issues.sort(key=lambda i: (levels.get(i["重要度"], 3), i["行"]))
    flags = {i["行"] for i in issues if i["重要度"] == "高"}
    frame.insert(0, "_確認", ["要確認" if i + 1 in flags else "" for i in range(len(frame))])

    stem = f"{definition.get('name', 'データ')}_{dt.date.today():%Y%m%d}"
    write_outputs(frame, issues, Path(args.out), stem)

    print(f"  - 取り込み: {len(frame)} 件 / 指摘: 高 {high} 件, 中 {medium} 件, "
          f"低 {len(issues) - high - medium} 件")
    for issue in issues[:10]:
        print(f"    [{issue['重要度']}] {issue['行']}行目 {issue['項目']}: {issue['内容']}")
    if len(issues) > 10:
        print(f"    ... 他 {len(issues) - 10} 件（Excel の「検証結果」シート参照）")

    if args.strict and high:
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:  # head などにパイプした場合
        sys.stderr.close()
        raise SystemExit(0)
