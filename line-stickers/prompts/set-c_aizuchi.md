# セットC：相槌・リアクション（aizuchi）

会話のテンポを作る相槌と感情リアクション。連打で使われるのでトーク内での露出が多い。

## 使い方

1. Gemini に `reference/character.png` を添付する
2. 下の各プロンプトを1つずつ貼って生成する（1枚ずつ作るのが一番ブレません）
3. 気に入った画像を `work/raw/A-01.png` のように保存する
   （このセットなら `C-01.png` 〜 `C-16.png`）
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

## C-01　「うんうん」

- ポーズ: 目を閉じて何度もうなずく。頭の動きを表す小さな残像線を上下に。
- 保存ファイル名: `work/raw/C-01.png`

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
目を閉じて何度もうなずく。頭の動きを表す小さな残像線を上下に。

（※このスタンプに乗せる予定のセリフは「うんうん」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: nodding repeatedly with eyes closed, small motion lines showing the head bobbing.
(This sticker will later carry the Japanese caption "うんうん" added in post - match the mood, but do not draw any text.)
```

</details>

## C-02　「なるほど〜」

- ポーズ: 前足をあごに当てて感心。頭の上に小さな電球がぽっと灯る。
- 保存ファイル名: `work/raw/C-02.png`

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
前足をあごに当てて感心。頭の上に小さな電球がぽっと灯る。

（※このスタンプに乗せる予定のセリフは「なるほど〜」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: paw on chin, impressed expression, a small light bulb glowing above the head.
(This sticker will later carry the Japanese caption "なるほど〜" added in post - match the mood, but do not draw any text.)
```

</details>

## C-03　「たしかに！」

- ポーズ: 両前足をポンと打ち合わせる。目を見開いた納得顔。
- 保存ファイル名: `work/raw/C-03.png`

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
両前足をポンと打ち合わせる。目を見開いた納得顔。

（※このスタンプに乗せる予定のセリフは「たしかに！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: clapping both front paws together, wide-open eyes, convinced look.
(This sticker will later carry the Japanese caption "たしかに！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-04　「ほんと？」

- ポーズ: 首を大きく傾げて目を丸くする。頭の上に大きな「？」。
- 保存ファイル名: `work/raw/C-04.png`

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
首を大きく傾げて目を丸くする。頭の上に大きな「？」。

（※このスタンプに乗せる予定のセリフは「ほんと？」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: head tilted far to one side, round surprised eyes, a big question mark above.
(This sticker will later carry the Japanese caption "ほんと？" added in post - match the mood, but do not draw any text.)
```

</details>

## C-05　「すごい！」

- ポーズ: 両前足を口元に当てて目を大きくキラキラ。まわりに星が飛ぶ。
- 保存ファイル名: `work/raw/C-05.png`

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
両前足を口元に当てて目を大きくキラキラ。まわりに星が飛ぶ。

（※このスタンプに乗せる予定のセリフは「すごい！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: both paws at the mouth, huge sparkling eyes, stars bursting around.
(This sticker will later carry the Japanese caption "すごい！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-06　「えー！」

- ポーズ: びょんと飛び上がって驚く。目が点、口が大きく開き、上に「!?」。
- 保存ファイル名: `work/raw/C-06.png`

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
びょんと飛び上がって驚く。目が点、口が大きく開き、上に「!?」。

（※このスタンプに乗せる予定のセリフは「えー！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: leaping up in shock, dot eyes, mouth wide open, an interrobang above.
(This sticker will later carry the Japanese caption "えー！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-07　「わかる〜」

- ポーズ: 目を細めてしみじみ笑い、片前足を胸に当てる。
- 保存ファイル名: `work/raw/C-07.png`

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
目を細めてしみじみ笑い、片前足を胸に当てる。

（※このスタンプに乗せる予定のセリフは「わかる〜」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: eyes narrowed in knowing sympathy, one paw on the chest.
(This sticker will later carry the Japanese caption "わかる〜" added in post - match the mood, but do not draw any text.)
```

</details>

## C-08　「それな！」

- ポーズ: 前足をビシッとこちらに向けて指さす。ノリノリの笑顔。
- 保存ファイル名: `work/raw/C-08.png`

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
前足をビシッとこちらに向けて指さす。ノリノリの笑顔。

（※このスタンプに乗せる予定のセリフは「それな！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: pointing a paw straight at the viewer, hyped grinning face.
(This sticker will later carry the Japanese caption "それな！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-09　「うれしい！」

- ポーズ: その場でくるっと回って跳ねる。まわりにハートと音符。
- 保存ファイル名: `work/raw/C-09.png`

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
その場でくるっと回って跳ねる。まわりにハートと音符。

（※このスタンプに乗せる予定のセリフは「うれしい！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: spinning and hopping with joy, hearts and music notes around.
(This sticker will later carry the Japanese caption "うれしい！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-10　「かなしい…」

- ポーズ: うつむいて目に涙をためる。耳が垂れ、青い雫が一滴。
- 保存ファイル名: `work/raw/C-10.png`

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
うつむいて目に涙をためる。耳が垂れ、青い雫が一滴。

（※このスタンプに乗せる予定のセリフは「かなしい…」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: looking down with tears welling up, ears drooping, one blue teardrop.
(This sticker will later carry the Japanese caption "かなしい…" added in post - match the mood, but do not draw any text.)
```

</details>

## C-11　「びっくり！」

- ポーズ: 毛が逆立ってのけぞる。目が真ん丸、まわりに衝撃の集中線。
- 保存ファイル名: `work/raw/C-11.png`

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
毛が逆立ってのけぞる。目が真ん丸、まわりに衝撃の集中線。

（※このスタンプに乗せる予定のセリフは「びっくり！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: fur standing on end, leaning back startled, perfectly round eyes, impact lines.
(This sticker will later carry the Japanese caption "びっくり！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-12　「ドキドキ」

- ポーズ: 両前足を胸に当ててほっぺ真っ赤。頭の上に大きなピンクのハート。
- 保存ファイル名: `work/raw/C-12.png`

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
両前足を胸に当ててほっぺ真っ赤。頭の上に大きなピンクのハート。

（※このスタンプに乗せる予定のセリフは「ドキドキ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: both paws on the chest, deeply blushing, a big pink heart above the head.
(This sticker will later carry the Japanese caption "ドキドキ" added in post - match the mood, but do not draw any text.)
```

</details>

## C-13　「がんばれ！」

- ポーズ: 小さな応援ポンポンを両前足で振る。元気いっぱいの笑顔。
- 保存ファイル名: `work/raw/C-13.png`

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
小さな応援ポンポンを両前足で振る。元気いっぱいの笑顔。

（※このスタンプに乗せる予定のセリフは「がんばれ！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: waving small cheer pompoms with both paws, energetic cheering smile.
(This sticker will later carry the Japanese caption "がんばれ！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-14　「おつかれ〜」

- ポーズ: だらんと座り込んだゆるい笑顔。頭の上に小さな湯気。
- 保存ファイル名: `work/raw/C-14.png`

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
だらんと座り込んだゆるい笑顔。頭の上に小さな湯気。

（※このスタンプに乗せる予定のセリフは「おつかれ〜」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: slumped sitting pose, loose relaxed smile, small steam puff above.
(This sticker will later carry the Japanese caption "おつかれ〜" added in post - match the mood, but do not draw any text.)
```

</details>

## C-15　「ふむふむ」

- ポーズ: 丸い眼鏡をかけて小さなメモを見つめる。真剣な表情。
- 保存ファイル名: `work/raw/C-15.png`

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
丸い眼鏡をかけて小さなメモを見つめる。真剣な表情。

（※このスタンプに乗せる予定のセリフは「ふむふむ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: wearing round glasses, studying a small notepad, focused expression.
(This sticker will later carry the Japanese caption "ふむふむ" added in post - match the mood, but do not draw any text.)
```

</details>

## C-16　「ぐすん…」

- ポーズ: 前足で目をこする。鼻先が赤く、小さな涙がぽろり。
- 保存ファイル名: `work/raw/C-16.png`

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
前足で目をこする。鼻先が赤く、小さな涙がぽろり。

（※このスタンプに乗せる予定のセリフは「ぐすん…」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: rubbing the eyes with a paw, red nose, small tears falling.
(This sticker will later carry the Japanese caption "ぐすん…" added in post - match the mood, but do not draw any text.)
```

</details>
