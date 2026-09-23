# kuro

Geminiなどで生成した画像を、LINE Creators Market のスタンプ規格
(メイン画像 240x240 / 一覧タブ画像 96x74 / スタンプ本体 370x320以内、
すべて透過PNG・1ファイル1MB以内) に変換し、そのままZIPにまとめるCLIツールです。

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

背景除去の精度を上げたい場合は、オプションでrembg (ML背景除去) を追加できます
(初回実行時に学習済みモデルをダウンロードするためネットワーク接続が必要です)。

```bash
pip install rembg
```

rembgが入っていない場合は、四隅からのフラッドフィルによる単色背景除去に自動で
フォールバックします(白背景など単色バックの画像向け)。

## 使い方

1. Geminiで生成した画像(8〜40枚)を1つのフォルダに集める(例: `raw/`)。
2. 変換してZIPを作成する。

```bash
python -m line_sticker.cli process raw/ -o sticker_set.zip
```

主なオプション:

- `--main <path>`: メイン画像(main.png)の元にする画像を指定(省略時は先頭の画像)
- `--tab <path>`: 一覧タブ画像(tab.png)の元にする画像を指定(省略時は先頭の画像)
- `--no-bg-removal`: 背景除去をスキップ(すでに透過済みの画像を使う場合)
- `--tolerance <int>`: フォールバックの背景除去の色許容度(デフォルト30)
- `--keep-dir <dir>`: ZIPに加えて生成したPNGをディレクトリにも残す
- `--text "N:テキスト"`: N番目(入力の並び順、1始まり)のスタンプの左上に、白フチ付き
  文字を入れる。繰り返し指定可能。例: `--text "1:了解" --text "2:おかえり"`
- `--font <path>`: 文字に使うフォント(省略時はIPAGothicなど日本語対応フォントを自動検出)
- `--font-size <int>` / `--text-color <color>` / `--outline-color <color>` / `--outline-width <int>`:
  文字サイズ・色・フチ色・フチ太さを調整

生成される `sticker_set.zip` の中身:

```
main.png   # 240x240
tab.png    # 96x74
01.png     # スタンプ本体(370x320以内)
02.png
...
```

このZIPはLINE Creators Studioへのアップロード前の下準備用です。実際の申請は
LINE Creators Market の画面から各画像をアップロードしてください。
