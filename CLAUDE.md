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
| `tools/annotate_image.py` | 写真に番号マーカーと引き出し線を焼き込む（全体図の説明用） |
| `tools/redraw_display.py` | 計器の7セグメント数値をマニュアル記載値に描き直す |
| `tools/make_board_template.py` | ホワイトボード用の記録枠を生成（`--width/--height/--rows`） |

## 新しいマニュアルを作るときの手順

1. `python3 tools/new_manual.py "<タイトル>" --slug <英数字slug> --steps <手順数>`
2. `python3 tools/prepare_images.py <slug> <写真フォルダ>`
   - 写真はスマホ原寸のままでよい。幅1400px・JPEG品質82に縮小され `01.jpg` から連番で並ぶ
   - 並び順はファイル名順。撮影順にしたいときは `--by-time`
3. `manuals/<slug>.py` の各手順に `title` と `lines`（説明文の配列、1要素＝1段落）を書く
4. `python3 tools/build_manual.py <slug>` で `docs/` に Markdown と PDF が出る
5. 生成物を確認してコミットする

## レイアウトの使い分け

定義ファイルの `layout` で決まる。

- **省略（既定）** — 手順が多い作業マニュアル。1手順＝左に説明文・右に写真。
  `steps` に手順を並べる（例：`manuals/pool_hair_catcher.py`）
  - `image` の代わりに `images`（`{"image":…, "caption":…}` の配列）を書くと、
    説明文が全幅になり写真が横並びになる。開・閉など2つの状態を見比べさせたいときに使う
  - 手順ごとに `image_height_mm` を書くと、その手順だけ写真の大きさを変えられる
    （既定はマニュアル全体の `image_max_height_mm`、さらに既定は62）
  - ページの詰まり具合は写真の高さで決まる。数mm変えると改ページ位置が動くので、
    生成後に必ずページ割りを確認する（例：`manuals/winter_heat_exchanger.py` は76mm/84mmで3ページ）
- **`"sheet"`** — 現場に貼る1枚もの。1ページ＝1面（表面・裏面）で、写真を大きく中央に置く。
  `steps` ではなく `pages` に面ごとの内容を書く（例：`manuals/lisena_startup.py`）

`sheet` の 1ページ分のキー：`side`（面の名前）、`title`、`highlight`（紺の強調枠）、
`lead`（リード文）、`steps`（`text` と任意の `image`）、`image`（面全体で1枚のとき）、
`image_height_mm`（写真の高さ。既定78）、`notes`（赤い注意枠）。手順番号は面ごとに1から振り直す。

## 文章を書くときの約束

- 1手順の説明は**3行以内**。4行を超えるとPDFで写真とのバランスが崩れる
- `sheet` レイアウトは貼り紙なので**1手順1行**。読む側は立ったまま見る
- 強調は `<b>…</b>` で囲む（PDFでは太字、Markdownでは `**…**` になる）
- 操作対象は盤面やバルブの**表示そのままの名称**で書く（例：「底引 運転」「常時開」）
- 「〜する」で止める常体。敬体は使わない
- 危険を伴う操作は手順本文ではなく `safety` に書く

## 画像についての約束

- リポジトリに入れるのは縮小後のJPEGのみ。原寸写真（10MB超）はコミットしない
- 丸印などの書き込みは写真側に入れておく（PDF生成時には加工しない）
- 引きの写真は該当箇所にトリミングする。印刷すると丸印やラベルが読めなくなるため
- 全体図の「どこが何か」は `tools/annotate_image.py` で番号マーカーだけ焼き込み、
  その説明文は手順の `lines` に書く（画像に凡例を焼き込むと印刷時に小さくて読めない）
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
