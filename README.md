# kuro — 設備業務マニュアル集

現場写真と手順テキストから、同じ体裁の業務マニュアル（Markdown + 印刷用PDF）を生成します。

## マニュアル一覧

| マニュアル | Markdown | 印刷用PDF |
| --- | --- | --- |
| プールヘアキャッチャー清掃 | [md](docs/プールヘアキャッチャー清掃.md) | [pdf](docs/プールヘアキャッチャー清掃.pdf) |

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

## 既存マニュアルを直す

`manuals/<slug>.py` を編集して再ビルドします。`docs/` 配下の生成物は直接編集しないでください。

```bash
python3 tools/build_manual.py pool-hair-catcher   # 1件
python3 tools/build_manual.py --all               # 全件
python3 tools/build_manual.py --list              # スラッグ一覧
```

## PDFの体裁

A4縦。表紙相当の見出しに続けて、清掃頻度表 → 安全上の注意 → 手順（1手順＝左に説明文・右に写真の枠、1ページ3手順）
→ 作業完了後のチェックリスト → 実施記録表（印刷して記入できる空欄つき）。
ページ下部にマニュアル名とページ番号が入ります。

レイアウトを変えたいときは `tools/manual_builder.py` を編集してください（全マニュアル共通）。
