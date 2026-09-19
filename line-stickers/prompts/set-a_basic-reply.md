# セットA：ベーシック返事（basic-reply）

毎日いちばん使う「はい／OK／ありがとう」系。まずこの1セットから出すのがおすすめ。

## 使い方

1. Gemini に `reference/character.png` を添付する
2. 下の各プロンプトを1つずつ貼って生成する（1枚ずつ作るのが一番ブレません）
3. 気に入った画像を `work/raw/A-01.png` のように保存する
   （このセットなら `A-01.png` 〜 `A-16.png`）
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

## A-01　「はい！」

- ポーズ: 右の前足をピシッとまっすぐ上げて元気に挙手。目をキラキラさせた満面の笑顔。
- 保存ファイル名: `work/raw/A-01.png`

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
右の前足をピシッとまっすぐ上げて元気に挙手。目をキラキラさせた満面の笑顔。

（※このスタンプに乗せる予定のセリフは「はい！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: raising one front paw straight up, eager sparkling eyes, big smile.
(This sticker will later carry the Japanese caption "はい！" added in post - match the mood, but do not draw any text.)
```

</details>

## A-02　「OK！」

- ポーズ: 両方の前足を頭の上で合わせて大きな「まる」を作る。得意げなにっこり笑顔。
- 保存ファイル名: `work/raw/A-02.png`

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
両方の前足を頭の上で合わせて大きな「まる」を作る。得意げなにっこり笑顔。

（※このスタンプに乗せる予定のセリフは「OK！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: both front paws joined above the head forming a big circle, proud happy smile.
(This sticker will later carry the Japanese caption "OK！" added in post - match the mood, but do not draw any text.)
```

</details>

## A-03　「了解！」

- ポーズ: 右の前足を額に当てて敬礼のポーズ。キリッとした真面目な目。
- 保存ファイル名: `work/raw/A-03.png`

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
右の前足を額に当てて敬礼のポーズ。キリッとした真面目な目。

（※このスタンプに乗せる予定のセリフは「了解！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: saluting with one front paw at the forehead, determined serious eyes.
(This sticker will later carry the Japanese caption "了解！" added in post - match the mood, but do not draw any text.)
```

</details>

## A-04　「わかった」

- ポーズ: こくりと小さくうなずく。目を細めたやさしい笑顔。
- 保存ファイル名: `work/raw/A-04.png`

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
こくりと小さくうなずく。目を細めたやさしい笑顔。

（※このスタンプに乗せる予定のセリフは「わかった」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: nodding gently, softly narrowed eyes, kind smile.
(This sticker will later carry the Japanese caption "わかった" added in post - match the mood, but do not draw any text.)
```

</details>

## A-05　「ありがとう」

- ポーズ: 両前足を胸の前で合わせてペコリとおじぎ。ほっぺを赤らめ、まわりに小さなハートがふわり。
- 保存ファイル名: `work/raw/A-05.png`

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
両前足を胸の前で合わせてペコリとおじぎ。ほっぺを赤らめ、まわりに小さなハートがふわり。

（※このスタンプに乗せる予定のセリフは「ありがとう」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: paws pressed together at the chest, small polite bow, blushing, tiny hearts floating around.
(This sticker will later carry the Japanese caption "ありがとう" added in post - match the mood, but do not draw any text.)
```

</details>

## A-06　「ごめんね」

- ポーズ: 前足を揃えて深く頭を下げる。耳がぺたんと垂れて、こめかみに汗が一滴。
- 保存ファイル名: `work/raw/A-06.png`

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
前足を揃えて深く頭を下げる。耳がぺたんと垂れて、こめかみに汗が一滴。

（※このスタンプに乗せる予定のセリフは「ごめんね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: deep apologetic bow, ears drooping flat, one sweat drop.
(This sticker will later carry the Japanese caption "ごめんね" added in post - match the mood, but do not draw any text.)
```

</details>

## A-07　「おねがい」

- ポーズ: 両前足を合わせて上目づかいでお願い。目がうるうる、まわりにキラキラ。
- 保存ファイル名: `work/raw/A-07.png`

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
両前足を合わせて上目づかいでお願い。目がうるうる、まわりにキラキラ。

（※このスタンプに乗せる予定のセリフは「おねがい」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: begging with paws clasped, big watery upturned eyes, sparkles.
(This sticker will later carry the Japanese caption "おねがい" added in post - match the mood, but do not draw any text.)
```

</details>

## A-08　「いいよ〜」

- ポーズ: 首を少し傾けてにっこり。片方の前足をひらひらと軽く振る。
- 保存ファイル名: `work/raw/A-08.png`

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
首を少し傾けてにっこり。片方の前足をひらひらと軽く振る。

（※このスタンプに乗せる予定のセリフは「いいよ〜」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: head tilted, easy smile, one paw waving lightly.
(This sticker will later carry the Japanese caption "いいよ〜" added in post - match the mood, but do not draw any text.)
```

</details>

## A-09　「だめ！」

- ポーズ: 両前足を胸の前で交差させて大きなバツ印。眉を吊り上げ、ほっぺをぷくっと膨らませる。
- 保存ファイル名: `work/raw/A-09.png`

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
両前足を胸の前で交差させて大きなバツ印。眉を吊り上げ、ほっぺをぷくっと膨らませる。

（※このスタンプに乗せる予定のセリフは「だめ！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: front paws crossed into an X, raised brows, puffed cheeks.
(This sticker will later carry the Japanese caption "だめ！" added in post - match the mood, but do not draw any text.)
```

</details>

## A-10　「まかせて！」

- ポーズ: 胸を張って片前足で自分の胸をドンと叩く。自信満々のドヤ顔。
- 保存ファイル名: `work/raw/A-10.png`

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
胸を張って片前足で自分の胸をドンと叩く。自信満々のドヤ顔。

（※このスタンプに乗せる予定のセリフは「まかせて！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: chest puffed out, one paw thumping own chest, confident smug face.
(This sticker will later carry the Japanese caption "まかせて！" added in post - match the mood, but do not draw any text.)
```

</details>

## A-11　「ちょっと待って」

- ポーズ: 片前足を前にぐっと突き出して「待て」のポーズ。少し焦った顔と汗一滴。
- 保存ファイル名: `work/raw/A-11.png`

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
片前足を前にぐっと突き出して「待て」のポーズ。少し焦った顔と汗一滴。

（※このスタンプに乗せる予定のセリフは「ちょっと待って」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: one paw thrust forward in a stop gesture, slightly flustered face, one sweat drop.
(This sticker will later carry the Japanese caption "ちょっと待って" added in post - match the mood, but do not draw any text.)
```

</details>

## A-12　「あとでね」

- ポーズ: 片前足を軽く振りながら横目でウインク。口角を上げた軽やかな笑顔。
- 保存ファイル名: `work/raw/A-12.png`

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
片前足を軽く振りながら横目でウインク。口角を上げた軽やかな笑顔。

（※このスタンプに乗せる予定のセリフは「あとでね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: winking with one eye while casually waving a paw, breezy smile.
(This sticker will later carry the Japanese caption "あとでね" added in post - match the mood, but do not draw any text.)
```

</details>

## A-13　「どっちでもいいよ」

- ポーズ: 両前足を軽く広げて肩をすくめる。半目のゆるい無表情。
- 保存ファイル名: `work/raw/A-13.png`

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
両前足を軽く広げて肩をすくめる。半目のゆるい無表情。

（※このスタンプに乗せる予定のセリフは「どっちでもいいよ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: shrugging with both paws open, half-lidded neutral face.
(This sticker will later carry the Japanese caption "どっちでもいいよ" added in post - match the mood, but do not draw any text.)
```

</details>

## A-14　「むり〜」

- ポーズ: 力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に小さな白いたましいがふわり。
- 保存ファイル名: `work/raw/A-14.png`

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
力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に小さな白いたましいがふわり。

（※このスタンプに乗せる予定のセリフは「むり〜」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: collapsed flat on the ground exhausted, eyes squeezed shut, tiny white soul floating up.
(This sticker will later carry the Japanese caption "むり〜" added in post - match the mood, but do not draw any text.)
```

</details>

## A-15　「できた！」

- ポーズ: 両前足を万歳に上げてぴょんとジャンプ。目を輝かせ、まわりにキラキラ。
- 保存ファイル名: `work/raw/A-15.png`

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
両前足を万歳に上げてぴょんとジャンプ。目を輝かせ、まわりにキラキラ。

（※このスタンプに乗せる予定のセリフは「できた！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: jumping with both paws raised in a cheer, shining eyes, sparkles around.
(This sticker will later carry the Japanese caption "できた！" added in post - match the mood, but do not draw any text.)
```

</details>

## A-16　「しらない…」

- ポーズ: ぷいっと横を向いて目を閉じる。ほっぺを膨らませたすねた顔。
- 保存ファイル名: `work/raw/A-16.png`

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
ぷいっと横を向いて目を閉じる。ほっぺを膨らませたすねた顔。

（※このスタンプに乗せる予定のセリフは「しらない…」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: turning the face away with eyes closed, sulking with puffed cheeks.
(This sticker will later carry the Japanese caption "しらない…" added in post - match the mood, but do not draw any text.)
```

</details>
