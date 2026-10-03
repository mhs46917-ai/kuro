# kuro — 設備業務マニュアル集

現場写真と手順テキストから、同じ体裁の業務マニュアル（Markdown + 印刷用PDF）を生成するリポジトリ。

## 構成

| パス | 役割 |
| --- | --- |
| `manuals/<slug>.py` | マニュアル1件分のデータ（タイトル・頻度・手順文・画像名）。**編集するのはここだけ** |
| `docs/images/<slug>/` | その マニュアルの写真（連番JPEG） |
| `docs/<タイトル>.md` / `.pdf` | 生成物。手で編集しない（次回ビルドで上書きされる） |
| `tools/build_manual.py` | 定義 → Markdown + PDF を生成 |
| `tools/prepare_images.py` | 写真を縮小・連番化して `docs/images/<slug>/` に配置 |
| `tools/new_manual.py` | 新規マニュアルの定義雛形を作る |
| `tools/manual_builder.py` | レイアウト本体（配色・組版はここに集約） |
| `tools/jp_font.py` | 日本語フォントのOS別自動検出 |

## 新しいマニュアルを作るときの手順

1. `python3 tools/new_manual.py "<タイトル>" --slug <英数字slug> --steps <手順数>`
2. `python3 tools/prepare_images.py <slug> <写真フォルダ>`
   - 写真はスマホ原寸のままでよい。幅1400px・JPEG品質82に縮小され `01.jpg` から連番で並ぶ
   - 並び順はファイル名順。撮影順にしたいときは `--by-time`
3. `manuals/<slug>.py` の各手順に `title` と `lines`（説明文の配列、1要素＝1段落）を書く
4. `python3 tools/build_manual.py <slug>` で `docs/` に Markdown と PDF が出る
5. 生成物を確認してコミットする

## 文章を書くときの約束

- 1手順の説明は**3行以内**。4行を超えるとPDFで写真とのバランスが崩れる
- 強調は `<b>…</b>` で囲む（PDFでは太字、Markdownでは `**…**` になる）
- 操作対象は盤面やバルブの**表示そのままの名称**で書く（例：「底引 運転」「常時開」）
- 「〜する」で止める常体。敬体は使わない
- 危険を伴う操作は手順本文ではなく `safety` に書く

## 画像についての約束

- リポジトリに入れるのは縮小後のJPEGのみ。原寸写真（10MB超）はコミットしない
- 丸印などの書き込みは写真側に入れておく（PDF生成時には加工しない）
- 画像の過不足は `tools/build_manual.py` 実行時に警告が出る

## 既存マニュアルの修正

`manuals/<slug>.py` を直して `python3 tools/build_manual.py <slug>` を再実行する。
`docs/` 配下の `.md` / `.pdf` を直接編集しても次回ビルドで消える。

## 環境

```
pip install -r requirements.txt   # pillow, reportlab
```

日本語フォントはOSごとに自動検出する（Windows: メイリオ/游ゴシック、macOS: ヒラギノ、
Linux: IPAゴシック/Noto）。見つからない場合や別のフォントを使いたい場合は環境変数で指定する。

```
MANUAL_FONT=/path/to/font.ttf python3 tools/build_manual.py <slug>
```

なお Linux の IPAゴシックには太字がないため、`<b>` が太く見えないことがある。
Windows（メイリオ／游ゴシック）と macOS（ヒラギノ）では太字になる。
