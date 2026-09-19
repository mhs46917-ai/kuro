# 作り方（全体の流れ）

```
prompts/*.md ──▶ Gemini ──▶ work/raw/  ──cutout──▶ work/cutout/ ──text──▶ work/final/ ──package──▶ dist/*.zip
  プロンプト      画像生成    白背景の元絵        透過+370x320      セリフ合成         提出用ZIP
```

## 0. 準備（1回だけ）

```bash
pip install -r scripts/requirements.txt
```

## 1. 画像を作る（Gemini）

1. `prompts/README.md` から作りたいセットを開く
2. Gemini（画像生成対応のモデル）に **`reference/character.png` を添付**する
3. プロンプトを1枚ずつ貼って生成する
   - 1回のやり取りで1枚だけ作るのが、いちばん絵柄がブレません
   - 同じチャットを続けて使うと、前の絵の雰囲気を引き継いでくれます
   - 崩れたら「参考画像の毛色・線の太さに合わせて描き直して」と追加で指示
4. 気に入った画像を **`work/raw/A-01.png` のような名前**で保存する
   - `セット記号 + 2桁の番号`（`A-01` 〜 `A-16`）。この番号がスタンプの並び順になります

> 背景は**純白（#FFFFFF）の単色**で出してもらってください。
> プロンプトにその指定は入っていますが、薄い影や地面が付いていたら描き直しを。

## 2. 切り抜く

```bash
python3 scripts/stickerkit.py cutout --set A
```

- 白背景を透過にし、キャラの周りを詰めて 370×320 の透明キャンバスに配置します
- 白フチ（ハロー）も除去します
- うまく抜けないとき:
  - 背景が少し残る → `--tol 45` のように数字を上げる
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
