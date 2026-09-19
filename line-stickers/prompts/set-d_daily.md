# セットD：毎日のひとこと（daily）

朝から夜まで、家族・恋人・友だちとの連絡に。時間帯でひと通り揃うセット。

## 使い方

1. Gemini に `reference/character.png` を添付する
2. 下の各プロンプトを1つずつ貼って生成する（1枚ずつ作るのが一番ブレません）
3. 気に入った画像を `work/raw/A-01.png` のように保存する
   （このセットなら `D-01.png` 〜 `D-16.png`）
4. `python3 scripts/stickerkit.py cutout` → `package` でZIPまで作る

## 共通スタイル（各プロンプトに含まれています）

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない
```

---

## D-01　「おはよう」

- ポーズ: ふとんから顔を出して伸びをする。目は半開き、頭の上に小さな太陽。
- 保存ファイル名: `work/raw/D-01.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
ふとんから顔を出して伸びをする。目は半開き、頭の上に小さな太陽。

（※このスタンプに乗せる予定のセリフは「おはよう」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: peeking out of a futon while stretching, half-open sleepy eyes, tiny sun above.
(This sticker will later carry the Japanese caption "おはよう" added in post - match the mood, but do not draw any text.)
```

</details>

## D-02　「おやすみ」

- ポーズ: 枕に寄り添って丸くなり目を閉じる。頭の上に「Zzz」と小さな三日月。
- 保存ファイル名: `work/raw/D-02.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
枕に寄り添って丸くなり目を閉じる。頭の上に「Zzz」と小さな三日月。

（※このスタンプに乗せる予定のセリフは「おやすみ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: curled up asleep against a pillow, Zzz and a small crescent moon above.
(This sticker will later carry the Japanese caption "おやすみ" added in post - match the mood, but do not draw any text.)
```

</details>

## D-03　「いってきます」

- ポーズ: 小さなリュックを背負って片前足を元気に上げる。晴れやかな笑顔。
- 保存ファイル名: `work/raw/D-03.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
小さなリュックを背負って片前足を元気に上げる。晴れやかな笑顔。

（※このスタンプに乗せる予定のセリフは「いってきます」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: wearing a small backpack, one paw raised energetically, bright smile.
(This sticker will later carry the Japanese caption "いってきます" added in post - match the mood, but do not draw any text.)
```

</details>

## D-04　「いってらっしゃい」

- ポーズ: 小さなハンカチを持って笑顔で見送り、もう片方の前足を振る。
- 保存ファイル名: `work/raw/D-04.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
小さなハンカチを持って笑顔で見送り、もう片方の前足を振る。

（※このスタンプに乗せる予定のセリフは「いってらっしゃい」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: holding a little handkerchief and waving goodbye with a warm smile.
(This sticker will later carry the Japanese caption "いってらっしゃい" added in post - match the mood, but do not draw any text.)
```

</details>

## D-05　「ただいま」

- ポーズ: 半分開いた玄関のドアからひょこっと顔を出す。ほっとした笑顔。
- 保存ファイル名: `work/raw/D-05.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
半分開いた玄関のドアからひょこっと顔を出す。ほっとした笑顔。

（※このスタンプに乗せる予定のセリフは「ただいま」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: peeking around a half-open door, relieved happy face.
(This sticker will later carry the Japanese caption "ただいま" added in post - match the mood, but do not draw any text.)
```

</details>

## D-06　「おかえり」

- ポーズ: しっぽを振ってこちらに駆け寄る。目を輝かせた満面の笑み、まわりにハート。
- 保存ファイル名: `work/raw/D-06.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
しっぽを振ってこちらに駆け寄る。目を輝かせた満面の笑み、まわりにハート。

（※このスタンプに乗せる予定のセリフは「おかえり」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: running toward the viewer with a wagging tail, shining eyes, hearts around.
(This sticker will later carry the Japanese caption "おかえり" added in post - match the mood, but do not draw any text.)
```

</details>

## D-07　「またね」

- ポーズ: 後ろを振り返りながら片前足を振る。にっこり。
- 保存ファイル名: `work/raw/D-07.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
後ろを振り返りながら片前足を振る。にっこり。

（※このスタンプに乗せる予定のセリフは「またね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: looking back over the shoulder while waving one paw, gentle smile.
(This sticker will later carry the Japanese caption "またね" added in post - match the mood, but do not draw any text.)
```

</details>

## D-08　「ばいばい」

- ポーズ: 両前足を大きく振る。元気な笑顔、まわりに小さな星。
- 保存ファイル名: `work/raw/D-08.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
両前足を大きく振る。元気な笑顔、まわりに小さな星。

（※このスタンプに乗せる予定のセリフは「ばいばい」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: waving both front paws widely, cheerful smile, small stars around.
(This sticker will later carry the Japanese caption "ばいばい" added in post - match the mood, but do not draw any text.)
```

</details>

## D-09　「おなかすいた」

- ポーズ: おなかを前足で押さえてへにゃりと座り込む。頭の上に小さなごはん茶碗。
- 保存ファイル名: `work/raw/D-09.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
おなかを前足で押さえてへにゃりと座り込む。頭の上に小さなごはん茶碗。

（※このスタンプに乗せる予定のセリフは「おなかすいた」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: sitting limply holding its belly, a small bowl of rice floating above the head.
(This sticker will later carry the Japanese caption "おなかすいた" added in post - match the mood, but do not draw any text.)
```

</details>

## D-10　「ねむい…」

- ポーズ: 大きなあくび。目に涙がにじみ、片前足で目をこする。
- 保存ファイル名: `work/raw/D-10.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
大きなあくび。目に涙がにじみ、片前足で目をこする。

（※このスタンプに乗せる予定のセリフは「ねむい…」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: big yawn with watery eyes, rubbing one eye with a paw.
(This sticker will later carry the Japanese caption "ねむい…" added in post - match the mood, but do not draw any text.)
```

</details>

## D-11　「たのしみ！」

- ポーズ: 前足を胸の前で組んでそわそわ。目をキラキラ、まわりに音符。
- 保存ファイル名: `work/raw/D-11.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
前足を胸の前で組んでそわそわ。目をキラキラ、まわりに音符。

（※このスタンプに乗せる予定のセリフは「たのしみ！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: paws clasped at the chest, fidgeting with excitement, sparkling eyes, music notes.
(This sticker will later carry the Japanese caption "たのしみ！" added in post - match the mood, but do not draw any text.)
```

</details>

## D-12　「いまどこ？」

- ポーズ: 前足を目の上にかざして遠くを探す。頭の上に「？」。
- 保存ファイル名: `work/raw/D-12.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
前足を目の上にかざして遠くを探す。頭の上に「？」。

（※このスタンプに乗せる予定のセリフは「いまどこ？」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: shading the eyes with a paw while looking into the distance, question mark above.
(This sticker will later carry the Japanese caption "いまどこ？" added in post - match the mood, but do not draw any text.)
```

</details>

## D-13　「今から行くね」

- ポーズ: 元気に走り出すポーズ。後ろに走行線、笑顔。
- 保存ファイル名: `work/raw/D-13.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
元気に走り出すポーズ。後ろに走行線、笑顔。

（※このスタンプに乗せる予定のセリフは「今から行くね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: dashing forward mid-run, speed lines behind, happy face.
(This sticker will later carry the Japanese caption "今から行くね" added in post - match the mood, but do not draw any text.)
```

</details>

## D-14　「ちょっと遅れます」

- ポーズ: 大きな目覚まし時計を前足で抱えて焦る。汗マークが二つ。
- 保存ファイル名: `work/raw/D-14.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
大きな目覚まし時計を前足で抱えて焦る。汗マークが二つ。

（※このスタンプに乗せる予定のセリフは「ちょっと遅れます」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: hugging a big alarm clock in a panic, two sweat drops.
(This sticker will later carry the Japanese caption "ちょっと遅れます" added in post - match the mood, but do not draw any text.)
```

</details>

## D-15　「着いたよ」

- ポーズ: 片前足を上げて到着の合図。にこにこ顔、足元に小さなピンのマーク。
- 保存ファイル名: `work/raw/D-15.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
片前足を上げて到着の合図。にこにこ顔、足元に小さなピンのマーク。

（※このスタンプに乗せる予定のセリフは「着いたよ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: raising one paw to signal arrival, happy face, a small location pin near the feet.
(This sticker will later carry the Japanese caption "着いたよ" added in post - match the mood, but do not draw any text.)
```

</details>

## D-16　「会いたいな」

- ポーズ: ほっぺに前足を当ててうっとり目を細める。まわりにふわふわのハート。
- 保存ファイル名: `work/raw/D-16.png`

<details><summary>日本語プロンプト（クリックで展開・これをコピー）</summary>

```text
添付の参考画像のキャラクターを、同じ子だと分かるように維持して描いてください。

【キャラクター設定】
- ヨークシャーテリアの子犬。2〜3頭身のデフォルメ、基本は正面向き
- 毛色はクリームベージュ、耳まわり・背中・足先にシルバーグレーの差し色。毛先はふわふわギザギザ
- 線はこげ茶色の太めの手描き線。色鉛筆／クレヨンのようなざらついた塗り、はみ出しのある手描き感
- 顔は大きな丸い黒目、小さなこげ茶の鼻、ピンクのほっぺ（斜線2本）、開いた口にピンクの舌
- やさしくて、ゆるくて、かわいい雰囲気

【画面の指定】
- 正方形キャンバス（1:1）、キャラクターは中央
- 背景は純白（#FFFFFF）の単色のみ。影・地面・枠線・グラデーション・模様は一切描かない
- キャラクターは1体だけ。コマ割り・複数バリエーション・見本シートにしない
- 全体を画面の80%くらいの大きさに収め、四辺に余白をあける
- 文字・ロゴ・透かしは入れない

【今回のポーズ・表情】
ほっぺに前足を当ててうっとり目を細める。まわりにふわふわのハート。

（※このスタンプに乗せる予定のセリフは「会いたいな」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
```

</details>

<details><summary>English prompt（英語のほうが安定する場合はこちら）</summary>

```text
Keep the character from the attached reference image recognizably the same dog.

Character: chibi Yorkshire Terrier puppy, 2-3 heads tall, facing the viewer.
Cream-beige fur with silver-grey accents on the ears, back and paws, fluffy jagged fur tips.
Thick hand-drawn dark-brown outlines, colored-pencil / crayon texture with visible grain.
Big round black eyes, small dark-brown nose, pink blush strokes on the cheeks, open mouth with a pink tongue.
Soft, gentle, cute picture-book mood.

Canvas: square 1:1, character centered, occupying about 80% of the frame with clear margins.
Background: pure white #FFFFFF, flat, absolutely nothing else - no shadow, no ground, no frame, no gradient, no pattern.
Exactly one character. Not a sheet, not a grid, not multiple variations.
No text, no logo, no watermark.

Pose and expression: paw against its cheek, dreamy narrowed eyes, soft hearts floating around.
(This sticker will later carry the Japanese caption "会いたいな" added in post - match the mood, but do not draw any text.)
```

</details>
