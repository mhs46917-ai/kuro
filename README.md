# kuro — 設備業務マニュアル集

現場写真と手順テキストから、同じ体裁の業務マニュアル（Markdown + 印刷用PDF）を生成します。

## マニュアル一覧

| マニュアル | Markdown | 印刷用PDF |
| --- | --- | --- |
| プールヘアキャッチャー清掃 | [md](docs/プールヘアキャッチャー清掃.md) | [pdf](docs/プールヘアキャッチャー清掃.pdf) |
| リセナ立ち上げ（A4両面1枚） | [md](docs/リセナ立ち上げ.md) | [pdf](docs/リセナ立ち上げ.pdf) |
| 水抜き機械室操作 | [md](docs/水抜き機械室操作.md) | [pdf](docs/水抜き機械室操作.pdf) |
| 冬季熱交換器操作 | [md](docs/冬季熱交換器操作.md) | [pdf](docs/冬季熱交換器操作.pdf) |
| ホワイトボード記入レイアウト（記録用紙） | — | [pdf](docs/ホワイトボード記入レイアウト.pdf) |

## セットアップ（初回のみ）

Python 3.9以上が必要です。

```bash
pip install -r requirements.txt
```

日本語フォントはOSごとに自動検出します（Windows: メイリオ／游ゴシック、macOS: ヒラギノ、Linux: IPAゴシック／Noto）。
別のフォントを使う場合は `MANUAL_FONT` に TTF/TTC のパスを指定してください。

## 新しいマニュアルを作る

```bash
# 1. 雛形を作る（手順数は後から増減できる）
python3 tools/new_manual.py "ろ過器逆洗" --slug backwash --steps 12

# 2. 写真を縮小して連番で配置する（スマホ原寸のままで渡してよい）
python3 tools/prepare_images.py backwash ~/Desktop/逆洗写真

# 3. manuals/backwash.py に各手順の title と lines（説明文）を書く

# 4. Markdown と PDF を生成する
python3 tools/build_manual.py backwash
```

生成物は `docs/<タイトル>.md` と `docs/<タイトル>.pdf` に出ます。

## ホワイトボードの記録用紙

プール水温とバルブ操作を1日分記録する枠を生成します。既定はA3縦・8行。

```bash
python3 tools/make_board_template.py                        # A3縦・8行
python3 tools/make_board_template.py --width 450 --height 600 --rows 10
```

ボードの実寸に合わせたいときは `--width` / `--height` にmmを指定してください。

## 既存マニュアルを直す

`manuals/<slug>.py` を編集して再ビルドします。`docs/` 配下の生成物は直接編集しないでください。

```bash
python3 tools/build_manual.py pool-hair-catcher   # 1件
python3 tools/build_manual.py --all               # 全件
python3 tools/build_manual.py --list              # スラッグ一覧
```

## 2つのレイアウト

定義ファイルの `layout` で切り替えます。

| layout | 用途 | 体裁 |
| --- | --- | --- |
| 省略（既定） | 手順が多い作業マニュアル | 1手順＝左に説明文・右に写真、1ページ3手順 |
| `"sheet"` | 現場に貼る1枚もの | 1ページ＝1面。写真を大きく中央に配置。`pages` に面ごとの内容を書く |

`sheet` の例は `manuals/lisena_startup.py`（A4両面1枚）を参照してください。

## PDFの体裁（既定レイアウト）

A4縦。表紙相当の見出しに続けて、清掃頻度表 → 安全上の注意 → 手順（1手順＝左に説明文・右に写真の枠、1ページ3手順）
→ 作業完了後のチェックリスト → 実施記録表（印刷して記入できる空欄つき）。
ページ下部にマニュアル名とページ番号が入ります。

レイアウトを変えたいときは `tools/manual_builder.py` を編集してください（全マニュアル共通）。
