# ローカルPCでの画像編集セットアップ手順

`tools/line_sticker_prep.py` をこのクラウドセッションではなく、自分のPC上で
実行するための手順。目的は「Gemini等で生成したグリッド画像を、自分のPC上で
そのまま提出用データに変換できるようにする」こと。

## 1. 自分のPC上でClaudeのセッションを開く

このクラウドセッションはコンテナ上で動いていて、あなたのPCのファイルには
触れない。ローカルで作業するには、PC側で新しくセッションを立ち上げる。

どちらか一方でよい。

- **Claude Desktopアプリ**を開く
- または、作業したいフォルダでターミナルを開いて次を実行する

  ```bash
  claude remote-control
  ```

  実行すると、そのPCのセッションがClaude Codeアプリの画面にも表示されるようになる。

## 2. リポジトリを取得する

ローカルのターミナルで、作業用フォルダに移動してからクローンする。

```bash
git clone https://github.com/mhs46917-ai/kuro.git
cd kuro
git checkout claude/line-sticker-popularity-analysis-gqvbhq
```

すでにPhotoshopなどで使っているフォルダがあれば、その中で `git clone` してもよい。

## 3. Pythonの用意

Python 3.9以降が必要。

- **Windows**: [python.org](https://www.python.org/downloads/) からインストーラを
  取得してインストールする。インストール時に「Add python.exe to PATH」に
  チェックを入れる。
- **Mac**: すでに入っていることが多い。ターミナルで `python3 --version` を実行して
  確認する。入っていなければ `brew install python3`（Homebrewが無ければ先に
  [brew.sh](https://brew.sh/) の手順でインストール）。

確認コマンド：

```bash
python3 --version
```

## 4. 必要なライブラリをインストールする

```bash
python3 -m pip install pillow numpy scipy
```

Windowsで `python3` が見つからない場合は `python` に読み替える。

## 5. 日本語フォントを用意する

`tools/line_sticker_prep.py` はデフォルトで
`/usr/share/fonts/truetype/fonts-japanese-gothic.ttf`（Linux専用パス）を見に行く。
Windows/Macではこのパスが存在しないので、実行時に `--font` オプションで
自分のPCの日本語フォントを指定する。

- **Windows**: 例
  ```
  --font "C:\Windows\Fonts\YuGothB.ttc"
  ```
  （游ゴシック Bold。無ければ `C:\Windows\Fonts\meiryob.ttc` でも可）
- **Mac**: 例
  ```
  --font "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc"
  ```
  （ヒラギノ角ゴシック。見つからない場合は「フォントブック」アプリで
  インストール済みの日本語フォントのファイルパスを確認する）

毎回打つのが面倒なら、後述のシェルスクリプト／バッチファイルに埋め込んでおく。

## 6. 動作確認

適当な生成画像（3×3グリッドのjpg/pngなど）を1枚用意し、リポジトリ直下で
実行してみる。

```bash
python3 tools/line_sticker_prep.py sample_grid.jpg -o test_out --grid 3x3 \
  --upscale 2.0 --keep-all --no-outline --inset 0.025 \
  --font "<3で確認した自分のフォントパス>"
```

`test_out` フォルダに `01.png`〜`09.png`・`main.png`・`tab.png` ができれば成功。

## 7. 普段の実行コマンド（このプロジェクトの標準運用）

`CLAUDE.md` に書いてある標準コマンドに `--font` を足すだけでよい。

```bash
python3 tools/line_sticker_prep.py grid1.jpg grid2.jpg grid3.jpg \
  -o out --grid 3x3 --upscale 2.0 --keep-all --no-outline --inset 0.025 \
  --select "<採用するコマの番号を並べ順で>" --main-index <mainにするコマ> \
  --text-band <74通常 / 110-125デカ文字> --text-bold <0-3> --text-stroke <-1/0/N> \
  --labels "<セリフをカンマ区切りで>" \
  --font "<自分のPCの日本語フォントパス>"
```

生成画像（grid1.jpg等）は、Geminiからダウンロードしてこのリポジトリのフォルダに
置いてから実行する。

## 8. 完了後

出来上がった `out/` フォルダの中身（01.png〜, main.png, tab.png）を
LINE Creators Studioにそのままアップロードすればよい。

ツールに直したい挙動が出てきたら、そのPC上のClaudeセッションで
「ここがこう直したい」と伝えれば、`tools/line_sticker_prep.py` を直接
編集できる。直したらこのブランチにコミット・プッシュしておくと、
クラウド側のセッションとも共有できる。

```bash
git add tools/line_sticker_prep.py
git commit -m "説明"
git push
```
