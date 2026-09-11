# kuro — 業務管理ツールキット

日々の業務で繰り返し発生する「Excel の集計・確認」「マニュアル作成」「画像からのデータ起こし」を、
毎回同じ手順・同じ品質で片付けるためのコマンド集です。

| ツール | できること | 主な出力 |
| --- | --- | --- |
| `tools/excel_analyze.py` | Excel / CSV の内容把握、品質チェック、集計、月次推移 | Markdown レポート + Excel レポート |
| `tools/manual_build.py` | YAML の定義から業務マニュアルを生成 | 配布用 HTML（印刷で PDF 化）+ Markdown |
| `tools/image_to_data.py` | 画像から起こしたデータの検証・表形式化 | Excel（データ + 検証結果）+ CSV |

## セットアップ

```bash
pip install -r requirements.txt
```

必要なのは `pandas` / `openpyxl` / `PyYAML` の 3 つだけです。

---

## 1. エクセルデータから分析

```bash
# いちばん簡単な使い方（集計軸・日付列は自動で判定）
python3 tools/excel_analyze.py 売上.xlsx

# 集計軸と集計値を指定する
python3 tools/excel_analyze.py 売上.xlsx --sheet 明細 --groupby 支店 --value 金額 --date 計上日

# 表記ゆれ（「東京支店」と「東京　支店」など）を統合して集計する
python3 tools/excel_analyze.py 売上.xlsx --groupby 支店 --normalize
```

出力される内容:

- **列プロファイル** — 列ごとの種別（数値 / 日付 / カテゴリ / テキスト）、欠損率、代表値
- **データ品質チェック** — 重複行、欠損、表記ゆれ、外れ値、変換できない値、未来日付などを重要度つきで指摘
- **集計表** — 指定（または自動選択）した軸ごとの件数・合計・平均。上位 N 件 + その他 + 合計行
- **月次推移** — 日付列を基準にした月別集計と前月比

実務ファイルでよくある次の状態にそのまま対応します。

- 表の上にタイトル行がある（見出し行を自動判定。`--header-row` で明示指定も可能）
- 金額が `1,234円` や `▲500`、数量が全角数字 `１２`
- 日付が `令和8年4月1日` と `2026/4/1` の混在、Excel シリアル値
- 空欄が `-` や `該当なし` で表現されている

主なオプション: `--sheet` / `--header-row` / `--groupby` / `--value` / `--date` / `--top` / `--normalize` / `--out` / `--no-xlsx`

### 試してみる

```bash
python3 samples/make_sample.py                                   # サンプルデータを生成
python3 tools/excel_analyze.py samples/売上明細_サンプル.xlsx      # 分析してみる
```

出力例: [`samples/売上明細_分析レポート例.md`](samples/売上明細_分析レポート例.md)

---

## 2. マニュアル作成

手順を YAML に書くと、体裁の整ったマニュアルが生成されます。
体裁を毎回作り込む必要がなくなり、改訂も差分が追えます。

```bash
# ひな形を作る
python3 tools/manual_build.py --new manuals/受注処理.yaml

# 編集したあとマニュアルを生成する
python3 tools/manual_build.py manuals/受注処理.yaml              # HTML
python3 tools/manual_build.py manuals/受注処理.yaml --format both # HTML + Markdown
```

生成される HTML には次が含まれます。

- 文書番号・版数・所管部署・適用開始日のヘッダー
- 目的 / 適用範囲 / 用語定義 / 改訂履歴 / 目次
- 章・手順の自動採番（`1-2` 形式）、担当・システム・所要時間のタグ
- 「補足」「注意」の囲み、手順ごとの確認チェックリスト
- よくある質問、問い合わせ先

**PDF にするには**: 生成された HTML をブラウザで開き、印刷 → PDF に保存。A4 の余白・改ページを指定済みです。
画像は base64 で埋め込まれるため、HTML 1 ファイルだけで配布できます。

定義ファイルに不備（手順の説明がない等）があれば警告を出したうえで生成します。

記入例: [`manuals/受注処理.yaml`](manuals/受注処理.yaml) /
出力例: [`samples/受注処理マニュアル.html`](samples/受注処理マニュアル.html)

---

## 3. 画像からデータ作成

画像の読み取りは Claude（または OCR）が行い、本ツールは
**「項目定義どおりか」「数値・日付として妥当か」を機械的に検証して表に落とす**役割を担います。
転記ミスを人が目視で探す作業をなくすための仕組みです。

```bash
# 1. 読み取る項目を定義する
python3 tools/image_to_data.py init --fields fields/受領書.yaml

# 2. 読み取り指示文を出力する
python3 tools/image_to_data.py prompt --fields fields/受領書.yaml --out output/指示.md
#    → 出力された指示文と画像を Claude に渡し、JSON で書き出してもらう

# 3. 受け取った JSON を検証して Excel / CSV にする
python3 tools/image_to_data.py build --fields fields/受領書.yaml data.json
```

検証される内容:

- 必須項目の空欄、項目自体の出力漏れ
- 数値・日付として読めない値、上下限の超過、未来日付
- 番号の形式（正規表現）、`unique: true` を付けた項目の重複
- 選択肢（`choices`）にない値、文字数超過
- 読み取り側が「自信が低い」と申告したレコード

指摘があった行には `_確認` 列に「要確認」が立ち、Excel の「検証結果」シートに理由が一覧化されます。
`--strict` を付けると重要度「高」の指摘がある場合に異常終了するので、定型処理への組み込みにも使えます。

**値は勝手に直しません。** 正規化（全角→半角、和暦→西暦、`1,234円`→`1234`）は行いますが、
おかしい値はおかしいまま残して指摘します。判断は人が行う前提です。

---

## ディレクトリ構成

```
tools/     ツール本体（common.py は日本語表記ゆれの正規化を担う共通処理）
manuals/   マニュアルの定義ファイル(YAML)
fields/    画像読み取りの項目定義(YAML)
samples/   動作確認用のサンプルデータと出力例
output/    生成物の出力先（git 管理外）
```

実業務のデータ（`.xlsx` / `.csv`）と `output/` は `.gitignore` で追跡対象外にしています。
社外秘のデータがそのままコミットされることを防ぐためです。
