# 作り方（全体の流れ）

```
prompts/*.md ─▶ Gemini ─▶ work/sheets/ ─split─▶ work/raw/ ─cutout─▶ work/cutout/ ─text─▶ work/final/ ─package─▶ dist/*.zip
 プロンプト     画像生成   3x3の一覧画像       1コマずつ      透過+370x320     セリフ合成        提出用ZIP
```

## 0. 準備（1回だけ）

```bash
pip install -r scripts/requirements.txt
```

## 1. 画像を作る（Gemini）

プロンプトは **3×3のグリッド一覧画像をまとめて出す形式**になっています。
1回の生成で9コマ出るので、絵柄が揃いやすく、生成回数も少なくて済みます。

1. `prompts/README.md` から作りたいセットを開く
2. Gemini（画像生成対応のモデル）に **`reference/character.png` を添付**する
3. 「シート1」のプロンプトをそのまま貼って生成する
   - **出力解像度はいちばん大きいものを選んでください**（1コマの画質が変わります）
   - 体が切れている／耳の形が変わっているコマがあれば、
     「参考画像の耳の形と毛色に合わせて、◯コマ目だけ描き直して」と指示
4. できた一覧画像を `work/sheets/A-sheet1.png` として保存する
5. 「シート2」も同じように `work/sheets/A-sheet2.png` へ

> 背景は**淡いミントグリーンの単色**で出してもらってください。
> キャラの毛色（クリーム・グレー）と色が離れているので、切り抜きがきれいに決まります。

## 1.5. 一覧画像を1コマずつに切り分ける

```bash
python3 scripts/stickerkit.py split --sheet work/sheets/A-sheet1.png --set A --grid 3x3 --start 1
python3 scripts/stickerkit.py split --sheet work/sheets/A-sheet2.png --set A --grid 3x3 --start 10
```

- 左上から右へ順に `A-01.png` … と `work/raw/` に保存されます
- 何も描かれていないコマは自動で飛ばします
- コマの境目に線が入ってしまったときは `--inset 0.02` で外周を少し削れます

崩れたコマがあれば、プロンプト集の「**1枚ずつ描き直す用**」で単体生成して、
同じファイル名（例 `work/raw/A-07.png`）で上書きしてください。

## 2. 切り抜く

```bash
python3 scripts/stickerkit.py cutout --set A
```

- 白背景を透過にし、キャラの周りを詰めて 370×320 の透明キャンバスに配置します
- 白フチ（ハロー）も除去します
- うまく抜けないとき:
  - 背景（ミントグリーン）が少し残る → `--tol 45` のように数字を上げる
  - キャラの明るい部分まで消える → `--tol 22` のように下げる
  - 小さなゴミが残る → `--min-area 200`

## 3. セリフを入れる（任意）

```bash
python3 scripts/stickerkit.py text --set A
```

- `prompts/prompts.json` のセリフを、ファイル名の番号に合わせて自動で入れます
- `--position top` で上に、`--band 0.28` で文字を大きく、`--font <path>` で別のフォントに
- **文字を入れずに出したい場合**はこの手順を飛ばしてください（`package` が自動で `work/cutout` を使います）

好きなフォントを使いたいときは、商用利用OKのフォント（M PLUS Rounded 1c、
しっぽり明朝、キルゴUなど）をダウンロードして `--font` で指定してください。

## 4. ZIPにする

```bash
python3 scripts/stickerkit.py package --set A
```

- `01.png`〜`16.png` にリネーム、`main.png`（240×240）と `tab.png`（96×74）も自動生成
- `dist/kuro-stickers-A.zip` ができます
- メイン画像を指定したいとき: `--main work/cutout/A-05.png`

## 5. 最終チェック

```bash
python3 scripts/stickerkit.py check dist/kuro-stickers-A.zip
```

サイズ・枚数・透過・容量を確認します。あとは**目視で文字化けがないか**を必ず見てください。

## 6. 申請

1. [LINE Creators Market](https://creator.line.me/) に登録・ログイン
2. 「新規登録」→ スタンプ（Sticker）
3. スタンプ名・説明文（日本語／英語）を入力
4. 画像アップロードで **ZIPを一括アップロード**
5. 販売価格を設定して申請 → 審査（数日〜2週間ほど）

## セットを増やすとき

`--set B`（ネガティブ返事）、`--set C`（共感返事）に変えて 1〜5 を繰り返すだけです。
セリフを変えたい・増やしたいときは `prompts/prompts.json` を編集して

```bash
python3 scripts/gen_prompts.py
```

を実行すると、プロンプト集のMarkdownが作り直されます。
