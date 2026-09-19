# セットB：ネガティブ返事（negative）

「行けたらいく」「だるいわー」など、気を使わない相手に送るゆるいネガティブ。家族・親友・恋人向けで刺さるセット。

## 使い方

1. Gemini に `reference/character.png` を添付する
2. 下の各プロンプトを1つずつ貼って生成する（1枚ずつ作るのが一番ブレません）
3. 気に入った画像を `work/raw/B-01.png` 〜 `work/raw/B-16.png` の名前で保存する（番号が並び順になります）
4. `python3 scripts/stickerkit.py cutout --set B` → `text --set B` → `package --set B` でZIPまで作る

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

## B-01　「行けたらいく」

- ポーズ: 目をそらして前足でほっぺをかく。あいまいな半笑い、汗が一滴。
- 保存ファイル名: `work/raw/B-01.png`

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
目をそらして前足でほっぺをかく。あいまいな半笑い、汗が一滴。

（※このスタンプに乗せる予定のセリフは「行けたらいく」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: looking away while scratching its cheek with a paw, vague awkward half-smile, one sweat drop.
(This sticker will later carry the Japanese caption "行けたらいく" added in post - match the mood, but do not draw any text.)
```

</details>

## B-02　「だるいわー」

- ポーズ: 背中を丸めてだらんと座り込む。半目の無表情、頭の上にどんよりした灰色の雲。
- 保存ファイル名: `work/raw/B-02.png`

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
背中を丸めてだらんと座り込む。半目の無表情、頭の上にどんよりした灰色の雲。

（※このスタンプに乗せる予定のセリフは「だるいわー」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: slouching and sitting limply, half-lidded blank eyes, a gloomy grey cloud above the head.
(This sticker will later carry the Japanese caption "だるいわー" added in post - match the mood, but do not draw any text.)
```

</details>

## B-03　「むりー」

- ポーズ: 力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に白いたましいがふわり。
- 保存ファイル名: `work/raw/B-03.png`

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
力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に白いたましいがふわり。

（※このスタンプに乗せる予定のセリフは「むりー」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: collapsed flat on the ground exhausted, eyes squeezed shut, a tiny white soul floating out.
(This sticker will later carry the Japanese caption "むりー" added in post - match the mood, but do not draw any text.)
```

</details>

## B-04　「めんどくさい」

- ポーズ: 床にごろんと寝転がって足を投げ出す。半目でこちらをちらっと見る。
- 保存ファイル名: `work/raw/B-04.png`

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
床にごろんと寝転がって足を投げ出す。半目でこちらをちらっと見る。

（※このスタンプに乗せる予定のセリフは「めんどくさい」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: sprawled on its back on the floor with legs flopped out, glancing at the viewer with half-lidded eyes.
(This sticker will later carry the Japanese caption "めんどくさい" added in post - match the mood, but do not draw any text.)
```

</details>

## B-05　「気が向いたらね」

- ポーズ: そっぽを向きながら片前足を軽くひらひらさせる。うすい笑み。
- 保存ファイル名: `work/raw/B-05.png`

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
そっぽを向きながら片前足を軽くひらひらさせる。うすい笑み。

（※このスタンプに乗せる予定のセリフは「気が向いたらね」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: looking away while lazily waving one paw, faint noncommittal smile.
(This sticker will later carry the Japanese caption "気が向いたらね" added in post - match the mood, but do not draw any text.)
```

</details>

## B-06　「今日はパス」

- ポーズ: 両前足を胸の前で小さくバツにして、首を横に振る。困り眉。
- 保存ファイル名: `work/raw/B-06.png`

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
両前足を胸の前で小さくバツにして、首を横に振る。困り眉。

（※このスタンプに乗せる予定のセリフは「今日はパス」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: making a small X with both paws while shaking its head, troubled eyebrows.
(This sticker will later carry the Japanese caption "今日はパス" added in post - match the mood, but do not draw any text.)
```

</details>

## B-07　「ねむすぎる」

- ポーズ: 大きなあくび。目に涙がにじみ、片前足で目をこする。
- 保存ファイル名: `work/raw/B-07.png`

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

（※このスタンプに乗せる予定のセリフは「ねむすぎる」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: huge yawn with watery eyes, rubbing one eye with a paw.
(This sticker will later carry the Japanese caption "ねむすぎる" added in post - match the mood, but do not draw any text.)
```

</details>

## B-08　「つかれた…」

- ポーズ: 肩を落としてぺたんと座り込む。耳が垂れ、頭の上に小さな湯気。
- 保存ファイル名: `work/raw/B-08.png`

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
肩を落としてぺたんと座り込む。耳が垂れ、頭の上に小さな湯気。

（※このスタンプに乗せる予定のセリフは「つかれた…」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: sitting slumped with drooping shoulders, ears down, a small puff of steam above.
(This sticker will later carry the Japanese caption "つかれた…" added in post - match the mood, but do not draw any text.)
```

</details>

## B-09　「やる気でない」

- ポーズ: 小さなクッションに顔をうずめて突っ伏す。目は線になっている。
- 保存ファイル名: `work/raw/B-09.png`

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
小さなクッションに顔をうずめて突っ伏す。目は線になっている。

（※このスタンプに乗せる予定のセリフは「やる気でない」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: face-planted into a small cushion, eyes drawn as flat lines.
(This sticker will later carry the Japanese caption "やる気でない" added in post - match the mood, but do not draw any text.)
```

</details>

## B-10　「お金ない…」

- ポーズ: 空っぽのがま口財布を逆さにしてふりふり。涙目で口がへの字。
- 保存ファイル名: `work/raw/B-10.png`

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
空っぽのがま口財布を逆さにしてふりふり。涙目で口がへの字。

（※このスタンプに乗せる予定のセリフは「お金ない…」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: shaking an empty coin purse upside down, teary eyes, wobbly frown.
(This sticker will later carry the Japanese caption "お金ない…" added in post - match the mood, but do not draw any text.)
```

</details>

## B-11　「あとでいい？」

- ポーズ: 片前足を前に出して「待って」のポーズ。ばつの悪そうな笑顔。
- 保存ファイル名: `work/raw/B-11.png`

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
片前足を前に出して「待って」のポーズ。ばつの悪そうな笑顔。

（※このスタンプに乗せる予定のセリフは「あとでいい？」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: one paw held out in a wait gesture, sheepish apologetic smile.
(This sticker will later carry the Japanese caption "あとでいい？" added in post - match the mood, but do not draw any text.)
```

</details>

## B-12　「しらんがな」

- ポーズ: 両前足を軽く広げて肩をすくめる。完全な無表情、目が点。
- 保存ファイル名: `work/raw/B-12.png`

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
両前足を軽く広げて肩をすくめる。完全な無表情、目が点。

（※このスタンプに乗せる予定のセリフは「しらんがな」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: shrugging with both paws open, completely deadpan face, dot eyes.
(This sticker will later carry the Japanese caption "しらんがな" added in post - match the mood, but do not draw any text.)
```

</details>

## B-13　「ほっといて」

- ポーズ: ぷいっと横を向いて目を閉じる。ほっぺをぷくっと膨らませたすねた顔。
- 保存ファイル名: `work/raw/B-13.png`

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
ぷいっと横を向いて目を閉じる。ほっぺをぷくっと膨らませたすねた顔。

（※このスタンプに乗せる予定のセリフは「ほっといて」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: turning its face away with eyes closed, sulking with puffed cheeks.
(This sticker will later carry the Japanese caption "ほっといて" added in post - match the mood, but do not draw any text.)
```

</details>

## B-14　「やだー」

- ポーズ: 床に寝転がって手足をじたばたさせる。口を大きく開けたイヤイヤ顔。
- 保存ファイル名: `work/raw/B-14.png`

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
床に寝転がって手足をじたばたさせる。口を大きく開けたイヤイヤ顔。

（※このスタンプに乗せる予定のセリフは「やだー」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: lying on its back kicking all four legs in a tantrum, mouth wide open in protest.
(This sticker will later carry the Japanese caption "やだー" added in post - match the mood, but do not draw any text.)
```

</details>

## B-15　「まあいっか」

- ポーズ: 前足を頭の後ろに組んで天を仰ぐ。吹っ切れたゆるい笑顔。
- 保存ファイル名: `work/raw/B-15.png`

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
前足を頭の後ろに組んで天を仰ぐ。吹っ切れたゆるい笑顔。

（※このスタンプに乗せる予定のセリフは「まあいっか」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: paws behind its head, looking up at the sky, carefree relaxed smile.
(This sticker will later carry the Japanese caption "まあいっか" added in post - match the mood, but do not draw any text.)
```

</details>

## B-16　「聞いてないよ」

- ポーズ: 両前足で耳をぎゅっと塞ぐ。目をぎゅっとつぶる。
- 保存ファイル名: `work/raw/B-16.png`

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
両前足で耳をぎゅっと塞ぐ。目をぎゅっとつぶる。

（※このスタンプに乗せる予定のセリフは「聞いてないよ」です。セリフの雰囲気に合う表情にしてください。画像内に文字は描かないでください）
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

Pose and expression: covering both ears tightly with its paws, eyes scrunched shut.
(This sticker will later carry the Japanese caption "聞いてないよ" added in post - match the mood, but do not draw any text.)
```

</details>
