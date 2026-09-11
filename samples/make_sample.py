#!/usr/bin/env python3
"""動作確認用のサンプル業務データ（売上明細）を生成する。

タイトル行・表記ゆれ・和暦・空欄・重複行・外れ値を意図的に含めてあり、
`tools/excel_analyze.py` の挙動確認に使える。
"""

from __future__ import annotations

import random
from pathlib import Path

import pandas as pd

BRANCHES = ["東京支店", "大阪支店", "名古屋支店", "福岡支店"]
PRODUCTS = ["A-100", "A-200", "B-100", "C-300"]
CHANNELS = ["直販", "代理店", "EC"]


def build_rows(count: int, seed: int = 20260911) -> list[list]:
    random.seed(seed)
    rows: list[list] = []
    for i in range(count):
        month = random.randint(1, 9)
        day = random.randint(1, 28)
        branch = random.choice(BRANCHES)
        # 表記ゆれを混ぜる（全角スペース・前後空白）
        if i % 23 == 0:
            branch = f" {branch} "
        elif i % 31 == 0:
            branch = branch.replace("支店", "　支店")
        quantity = random.randint(1, 40)
        unit_price = random.choice([1200, 3500, 8000, 15000])
        amount = quantity * unit_price
        date = f"2026/{month}/{day}"
        if i % 17 == 0:  # 和暦表記
            date = f"令和8年{month}月{day}日"
        amount_cell: object = amount
        if i % 13 == 0:  # 通貨付き文字列
            amount_cell = f"{amount:,}円"
        note = "" if i % 4 else random.choice(["値引きあり", "再送分", "検収待ち"])
        rows.append([
            f"S{i + 1001}", date, branch, random.choice(PRODUCTS),
            random.choice(CHANNELS), quantity, unit_price, amount_cell, note,
        ])

    rows.append(rows[5][:])                      # 重複行
    rows[10][7] = 9_800_000                      # 外れ値
    rows[12][5] = None                           # 欠損
    rows[20][1] = "2026/2/30"                    # 不正な日付
    return rows


def main() -> None:
    header = ["伝票番号", "計上日", "支店", "商品コード", "販路", "数量", "単価", "金額", "備考"]
    rows = build_rows(180)

    # 表の上に 2 行のタイトル行を置く（実務ファイルでよくある形）
    padded = [
        ["2026年度 売上明細", None, None, None, None, None, None, None, None],
        ["※社内資料（サンプル）", None, None, None, None, None, None, None, None],
        header,
        *rows,
    ]
    frame = pd.DataFrame(padded)

    out_dir = Path(__file__).resolve().parent
    excel_path = out_dir / "売上明細_サンプル.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        frame.to_excel(writer, sheet_name="売上明細", index=False, header=False)
    pd.DataFrame([header, *rows]).to_csv(
        out_dir / "売上明細_サンプル.csv", index=False, header=False, encoding="utf-8-sig"
    )
    print(f"[生成] {excel_path}")
    print(f"[生成] {out_dir / '売上明細_サンプル.csv'}")


if __name__ == "__main__":
    main()
