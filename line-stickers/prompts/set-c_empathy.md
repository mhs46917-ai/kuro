# セットC：共感返事（empathy）

「わかる」「たしかに」「なるほど」に全振りした共感特化セット。会話のテンポを作るので連打で使われます。

## 使い方

1. Gemini に `reference/character.png` を添付する
2. 下の各プロンプトを1つずつ貼って生成する（1枚ずつ作るのが一番ブレません）
3. 気に入った画像を `work/raw/C-01.png` 〜 `work/raw/C-16.png` の名前で保存する（番号が並び順になります）
4. `python3 scripts/stickerkit.py cutout --set C` → `text --set C` → `package --set C` でZIPまで作る

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

## C-01　「わかる」

- ポーズ: 目を細めてしみじみうなずく。片前足をそっと胸に当てる。
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
目を細めてしみじみうなずく。片前足をそっと胸に当てる。

（※このスタンプに乗せる予定のセリフは「わかる」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: nodding slowly with narrowed knowing eyes, one paw resting on its chest.
(This sticker will later carry the Japanese caption "わかる" added in post - match the mood, but do not draw any text.)
```

</details>

## C-02　「めっちゃわかる」

- ポーズ: 前のめりになって何度も激しくうなずく。動きの残像線、目がきらり。
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
前のめりになって何度も激しくうなずく。動きの残像線、目がきらり。

（※このスタンプに乗せる予定のセリフは「めっちゃわかる」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: leaning forward nodding vigorously, motion after-image lines, eyes glinting.
(This sticker will later carry the Japanese caption "めっちゃわかる" added in post - match the mood, but do not draw any text.)
```

</details>

## C-03　「たしかに」

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

（※このスタンプに乗せる予定のセリフは「たしかに」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: clapping both front paws together, wide-open eyes, convinced expression.
(This sticker will later carry the Japanese caption "たしかに" added in post - match the mood, but do not draw any text.)
```

</details>

## C-04　「なるほど〜」

- ポーズ: 前足をあごに当てて感心。頭の上に小さな電球がぽっと灯る。
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

Pose and expression: paw on chin, impressed look, a small light bulb glowing above the head.
(This sticker will later carry the Japanese caption "なるほど〜" added in post - match the mood, but do not draw any text.)
```

</details>

## C-05　「それな」

- ポーズ: 前足をビシッとこちらに向けて指さす。ノリノリの笑顔。
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
前足をビシッとこちらに向けて指さす。ノリノリの笑顔。

（※このスタンプに乗せる予定のセリフは「それな」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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
(This sticker will later carry the Japanese caption "それな" added in post - match the mood, but do not draw any text.)
```

</details>

## C-06　「だよねー」

- ポーズ: 首をかしげてにっこり、片前足を軽く上げて同意する。
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
首をかしげてにっこり、片前足を軽く上げて同意する。

（※このスタンプに乗せる予定のセリフは「だよねー」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: head tilted with a warm smile, one paw raised lightly in agreement.
(This sticker will later carry the Japanese caption "だよねー" added in post - match the mood, but do not draw any text.)
```

</details>

## C-07　「うんうん」

- ポーズ: 目を閉じて何度もうなずく。頭の動きを表す小さな残像線を上下に。
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

## C-08　「ほんとそれ」

- ポーズ: 両前足をぐっと握って力説する。目を輝かせた熱い表情。
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
両前足をぐっと握って力説する。目を輝かせた熱い表情。

（※このスタンプに乗せる予定のセリフは「ほんとそれ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: clenching both front paws while passionately agreeing, fired-up shining eyes.
(This sticker will later carry the Japanese caption "ほんとそれ" added in post - match the mood, but do not draw any text.)
```

</details>

## C-09　「わかりみが深い」

- ポーズ: 目を閉じて前足を組み、深く大きくうなずく。頭の上に小さな「…！」。
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
目を閉じて前足を組み、深く大きくうなずく。頭の上に小さな「…！」。

（※このスタンプに乗せる予定のセリフは「わかりみが深い」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: eyes closed with front paws folded, nodding deeply, a small ellipsis-exclamation above.
(This sticker will later carry the Japanese caption "わかりみが深い" added in post - match the mood, but do not draw any text.)
```

</details>

## C-10　「そっかー」

- ポーズ: 少し眉を下げてやわらかく微笑み、首をかしげる。
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
少し眉を下げてやわらかく微笑み、首をかしげる。

（※このスタンプに乗せる予定のセリフは「そっかー」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: eyebrows slightly lowered, soft gentle smile, head tilted.
(This sticker will later carry the Japanese caption "そっかー" added in post - match the mood, but do not draw any text.)
```

</details>

## C-11　「ふむふむ」

- ポーズ: 丸い眼鏡をかけて小さなメモを見つめる。真剣な表情。
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

## C-12　「わたしも！」

- ポーズ: 片前足で自分を指さして目を大きく見開く。うれしそうな笑顔。
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
片前足で自分を指さして目を大きく見開く。うれしそうな笑顔。

（※このスタンプに乗せる予定のセリフは「わたしも！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: pointing at itself with one paw, eyes wide open, delighted smile.
(This sticker will later carry the Japanese caption "わたしも！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-13　「つらかったね」

- ポーズ: 前足をそっと差し出して寄り添う。眉を下げたやさしい目。
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
前足をそっと差し出して寄り添う。眉を下げたやさしい目。

（※このスタンプに乗せる予定のセリフは「つらかったね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: gently reaching out one paw in comfort, lowered brows, tender caring eyes.
(This sticker will later carry the Japanese caption "つらかったね" added in post - match the mood, but do not draw any text.)
```

</details>

## C-14　「がんばったね」

- ポーズ: 小さなタオルを両前足で持って差し出す。あたたかい笑顔。
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
小さなタオルを両前足で持って差し出す。あたたかい笑顔。

（※このスタンプに乗せる予定のセリフは「がんばったね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: holding out a small towel with both paws, warm approving smile.
(This sticker will later carry the Japanese caption "がんばったね" added in post - match the mood, but do not draw any text.)
```

</details>

## C-15　「えらい！」

- ポーズ: 両前足で拍手する。目をキラキラさせ、まわりに星が飛ぶ。
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
両前足で拍手する。目をキラキラさせ、まわりに星が飛ぶ。

（※このスタンプに乗せる予定のセリフは「えらい！」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: applauding with both front paws, sparkling eyes, stars bursting around.
(This sticker will later carry the Japanese caption "えらい！" added in post - match the mood, but do not draw any text.)
```

</details>

## C-16　「気持ちわかるよ」

- ポーズ: 目を閉じて、そっと抱きしめるように両前足を広げる。まわりにふんわりハート。
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
目を閉じて、そっと抱きしめるように両前足を広げる。まわりにふんわりハート。

（※このスタンプに乗せる予定のセリフは「気持ちわかるよ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: eyes closed, both front paws opened wide for a gentle hug, soft hearts floating around.
(This sticker will later carry the Japanese caption "気持ちわかるよ" added in post - match the mood, but do not draw any text.)
```

</details>
