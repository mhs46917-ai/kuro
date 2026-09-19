# セットA：あいさつ返事（greeting）

「はーい」「了解」「またね」など、毎日いちばん使うあいさつと返事。誰に送っても外さない基本セット。

## 作り方

1. Gemini に `reference/character.png` を添付する
2. 下の「シート1」のプロンプトを貼って3×3の一覧画像を出す
3. できた画像を `work/sheets/A-sheet1.png` として保存する
4. 一覧画像を1コマずつに切り分ける

```bash
python3 scripts/stickerkit.py split --sheet work/sheets/A-sheet1.png \
    --set A --grid 3x3 --start 1
```

5. 残りのシートも同じように（`--start` の数字を変える）
6. 崩れたコマだけ、下の「1枚ずつ描き直す用」で描き直して `work/raw/A-xx.png` を上書きする
7. `cutout --set A` → `text --set A` → `package --set A`

---

## シート1（A-01 〜 A-09／9コマ）

- 保存先: `work/sheets/A-sheet1.png`
- 切り分け: `python3 scripts/stickerkit.py split --sheet work/sheets/A-sheet1.png --set A --grid 3x3 --start 1`

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・9個を3×3のグリッド一覧画像にし、左上から右下へこの順で配置する
・必ず全身を描く。体の一部がコマの外で切れないようにする
・コマとコマの間に枠線・区切り線・番号を描かない
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない
・小物（湯のみ・カバン・財布など）は淡い色で小さく、キャラクターの顔に重ならないように描く

【ポーズ】
・「はーい」… 右の前足をピンとまっすぐ上げて元気に返事。目を輝かせた満面の笑顔。
・「OK！」… 両方の前足を頭の上で合わせて大きな「まる」を作る。得意げなにっこり顔。
・「了解！」… 右の前足を額に当てて敬礼のポーズ。キリッとした真面目な目。
・「わかった」… こくりと小さくうなずく。目を細めたやさしい笑顔。
・「ありがとう」… 両前足を胸の前で合わせてペコリとおじぎ。ほっぺを赤らめ、まわりに小さなハートがふわり。
・「ごめんね」… 前足を揃えて深く頭を下げる。耳がぺたんと垂れ、こめかみに汗が一滴。
・「よろしく」… 片方の前足をこちらに差し出して握手を求める。人懐っこいにっこり顔。
・「いいよ〜」… 首を少し傾けてにっこり。片方の前足をひらひらと軽く振る。
・「おはよう」… ふとんから顔を出して大きく伸びをする。目は半開き、頭の上に小さな太陽。

背景は淡いミントグリーンの単色。正方形。できるだけ高解像度で出力してください。
```

<details><summary>English version</summary>

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Lay out 9 illustrations as a 3 x 3 grid sheet, in this order from top-left to bottom-right
- Always draw the full body; never let any part be cut off by the edge of its cell
- No panel borders, dividing lines or numbers between the cells
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere. Do not write any of the words used below
- Keep props small and pale so they never cover the character

POSES:
- "はーい" ... raising one front paw straight up to answer, bright sparkling eyes, big happy smile
- "OK！" ... both front paws joined above the head forming a big circle, proud cheerful smile
- "了解！" ... saluting with one front paw at the forehead, crisp determined eyes
- "わかった" ... nodding gently once, softly narrowed eyes, kind smile
- "ありがとう" ... paws pressed together at the chest in a small grateful bow, blushing, tiny hearts floating around
- "ごめんね" ... deep apologetic bow with paws together, ears drooping flat, one sweat drop
- "よろしく" ... holding out one front paw for a handshake, friendly open smile
- "いいよ〜" ... head tilted with an easy smile, one paw waving lightly
- "おはよう" ... peeking out of a futon while stretching, half-open sleepy eyes, tiny sun above the head

Background: a flat pale mint green, flat. Square canvas. Output at the highest resolution available.
```

</details>

| コマ | セリフ | ファイル名 |
|---|---|---|
| 1 | はーい | `A-01.png` |
| 2 | OK！ | `A-02.png` |
| 3 | 了解！ | `A-03.png` |
| 4 | わかった | `A-04.png` |
| 5 | ありがとう | `A-05.png` |
| 6 | ごめんね | `A-06.png` |
| 7 | よろしく | `A-07.png` |
| 8 | いいよ〜 | `A-08.png` |
| 9 | おはよう | `A-09.png` |

---

## シート2（A-10 〜 A-16／7コマ）

- 保存先: `work/sheets/A-sheet2.png`
- 切り分け: `python3 scripts/stickerkit.py split --sheet work/sheets/A-sheet2.png --set A --grid 3x3 --start 10`
- このシートは7コマだけで、右下の2コマは空にします

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・7個を3×3のグリッド一覧画像にし、左上から右下へこの順で配置する
・右下の2コマは何も描かず、背景色のまま空けておく
・必ず全身を描く。体の一部がコマの外で切れないようにする
・コマとコマの間に枠線・区切り線・番号を描かない
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない
・小物（湯のみ・カバン・財布など）は淡い色で小さく、キャラクターの顔に重ならないように描く

【ポーズ】
・「おやすみ」… 枕に寄り添って丸くなり、目を閉じてすやすや。頭の上に「Zzz」と小さな三日月。
・「またね」… 後ろを振り返りながら片前足を振る。名残惜しそうなにっこり顔。
・「ばいばい」… 両方の前足を大きく振る。元気いっぱいの笑顔、まわりに小さな星。
・「いってきます」… 小さなリュックを背負って片前足を元気に上げる。晴れやかな笑顔。
・「ただいま」… 半分開いた玄関のドアからひょこっと顔を出す。ほっとした笑顔。
・「おかえり」… しっぽを振ってこちらに駆け寄る。目を輝かせた満面の笑み、まわりにハート。
・「おつかれさま」… 湯気の立つ湯のみを両前足で持って差し出す。ねぎらうやさしい笑顔。

背景は淡いミントグリーンの単色。正方形。できるだけ高解像度で出力してください。
```

<details><summary>English version</summary>

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Lay out 7 illustrations as a 3 x 3 grid sheet, in this order from top-left to bottom-right
- Leave the last 2 cells at the bottom right empty, background color only
- Always draw the full body; never let any part be cut off by the edge of its cell
- No panel borders, dividing lines or numbers between the cells
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere. Do not write any of the words used below
- Keep props small and pale so they never cover the character

POSES:
- "おやすみ" ... curled up asleep against a pillow, Zzz and a small crescent moon above
- "またね" ... looking back over the shoulder while waving one paw, fond gentle smile
- "ばいばい" ... waving both front paws widely, energetic happy smile, small stars around
- "いってきます" ... wearing a small backpack, one paw raised energetically, bright cheerful smile
- "ただいま" ... peeking around a half-open door, relieved happy face
- "おかえり" ... running toward the viewer with a wagging tail, shining eyes, hearts around
- "おつかれさま" ... offering a steaming teacup with both paws, warm caring smile

Background: a flat pale mint green, flat. Square canvas. Output at the highest resolution available.
```

</details>

| コマ | セリフ | ファイル名 |
|---|---|---|
| 1 | おやすみ | `A-10.png` |
| 2 | またね | `A-11.png` |
| 3 | ばいばい | `A-12.png` |
| 4 | いってきます | `A-13.png` |
| 5 | ただいま | `A-14.png` |
| 6 | おかえり | `A-15.png` |
| 7 | おつかれさま | `A-16.png` |

---

## 1枚ずつ描き直す用

グリッドで崩れたコマだけ、これで単体生成して差し替えてください。

<details><summary><b>A-01「はーい」</b> … 右の前足をピンとまっすぐ上げて元気に返事。目を輝かせた満面の笑顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
右の前足をピンとまっすぐ上げて元気に返事。目を輝かせた満面の笑顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: raising one front paw straight up to answer, bright sparkling eyes, big happy smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-02「OK！」</b> … 両方の前足を頭の上で合わせて大きな「まる」を作る。得意げなにっこり顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
両方の前足を頭の上で合わせて大きな「まる」を作る。得意げなにっこり顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: both front paws joined above the head forming a big circle, proud cheerful smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-03「了解！」</b> … 右の前足を額に当てて敬礼のポーズ。キリッとした真面目な目。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
右の前足を額に当てて敬礼のポーズ。キリッとした真面目な目。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: saluting with one front paw at the forehead, crisp determined eyes

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-04「わかった」</b> … こくりと小さくうなずく。目を細めたやさしい笑顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
こくりと小さくうなずく。目を細めたやさしい笑顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: nodding gently once, softly narrowed eyes, kind smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-05「ありがとう」</b> … 両前足を胸の前で合わせてペコリとおじぎ。ほっぺを赤らめ、まわりに小さなハートがふわり。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
両前足を胸の前で合わせてペコリとおじぎ。ほっぺを赤らめ、まわりに小さなハートがふわり。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: paws pressed together at the chest in a small grateful bow, blushing, tiny hearts floating around

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-06「ごめんね」</b> … 前足を揃えて深く頭を下げる。耳がぺたんと垂れ、こめかみに汗が一滴。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
前足を揃えて深く頭を下げる。耳がぺたんと垂れ、こめかみに汗が一滴。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: deep apologetic bow with paws together, ears drooping flat, one sweat drop

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-07「よろしく」</b> … 片方の前足をこちらに差し出して握手を求める。人懐っこいにっこり顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
片方の前足をこちらに差し出して握手を求める。人懐っこいにっこり顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: holding out one front paw for a handshake, friendly open smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-08「いいよ〜」</b> … 首を少し傾けてにっこり。片方の前足をひらひらと軽く振る。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
首を少し傾けてにっこり。片方の前足をひらひらと軽く振る。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: head tilted with an easy smile, one paw waving lightly

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-09「おはよう」</b> … ふとんから顔を出して大きく伸びをする。目は半開き、頭の上に小さな太陽。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
ふとんから顔を出して大きく伸びをする。目は半開き、頭の上に小さな太陽。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: peeking out of a futon while stretching, half-open sleepy eyes, tiny sun above the head

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-10「おやすみ」</b> … 枕に寄り添って丸くなり、目を閉じてすやすや。頭の上に「Zzz」と小さな三日月。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
枕に寄り添って丸くなり、目を閉じてすやすや。頭の上に「Zzz」と小さな三日月。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: curled up asleep against a pillow, Zzz and a small crescent moon above

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-11「またね」</b> … 後ろを振り返りながら片前足を振る。名残惜しそうなにっこり顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
後ろを振り返りながら片前足を振る。名残惜しそうなにっこり顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: looking back over the shoulder while waving one paw, fond gentle smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-12「ばいばい」</b> … 両方の前足を大きく振る。元気いっぱいの笑顔、まわりに小さな星。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
両方の前足を大きく振る。元気いっぱいの笑顔、まわりに小さな星。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: waving both front paws widely, energetic happy smile, small stars around

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-13「いってきます」</b> … 小さなリュックを背負って片前足を元気に上げる。晴れやかな笑顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
小さなリュックを背負って片前足を元気に上げる。晴れやかな笑顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: wearing a small backpack, one paw raised energetically, bright cheerful smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-14「ただいま」</b> … 半分開いた玄関のドアからひょこっと顔を出す。ほっとした笑顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
半分開いた玄関のドアからひょこっと顔を出す。ほっとした笑顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: peeking around a half-open door, relieved happy face

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-15「おかえり」</b> … しっぽを振ってこちらに駆け寄る。目を輝かせた満面の笑み、まわりにハート。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
しっぽを振ってこちらに駆け寄る。目を輝かせた満面の笑み、まわりにハート。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: running toward the viewer with a wagging tail, shining eyes, hearts around

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>A-16「おつかれさま」</b> … 湯気の立つ湯のみを両前足で持って差し出す。ねぎらうやさしい笑顔。</summary>

```text
添付した画像のキャラクターを、まったく同じ体型・同じ顔・
同じ耳の形・同じ輪郭線で描いてください。
変えるのはポーズと表情だけです。

【絶対に変えないもの】
・頭と体の比率（2頭身。頭が大きく体は小さい）
・首の長さ（首はほとんど無い）
・耳の形と大きさ（頭の左右に大きく張り出した、毛先がギザギザの立ち耳。
　小さくしない、垂らさない、丸くしない）
・前足と後ろ足の短さ（短くて丸い。指は描かない）
・毛色（クリームベージュ地に、頭頂・耳まわり・背中・胸から前足へシルバーグレーの差し色）
・毛先のふわふわギザギザした輪郭
・目の描き方（大きめの真っ黒な楕円。白いハイライトは入れない）
・鼻と口（小さなこげ茶の丸い鼻、その下にW字の口。開けたときは中がピンク）
・ほっぺ（左右にピンクの斜線が2本ずつ）
・線の色と太さ（こげ茶色の太い手描き線）
・塗りの質感（色鉛筆・クレヨン風のざらついた塗り、ムラのある手描き感）

【必ず守ること】
・キャラクターは1体だけ。グリッドや複数バリエーションにしない
・必ず全身を描く。体の一部が画面の外で切れないようにする
・背景に物や風景を描かない（切り抜いて使うため）
・影・地面・グラデーション・模様を描かない
・文字も数字も一切描かない。下の説明に出てくる言葉を絵の中に書かない

【ポーズ】
湯気の立つ湯のみを両前足で持って差し出す。ねぎらうやさしい笑顔。

背景は淡いミントグリーンの単色。正方形。キャラクターは中央に、四辺に余白をあけて描く。
```

```text
Draw the character from the attached image with exactly the same body shape,
the same face, the same ear shape and the same outline.
Only the pose and the expression change.

NEVER CHANGE:
- Head-to-body ratio (about 2 heads tall, big head, small body)
- Neck length (there is almost no neck)
- Ear shape and size (large upright ears flaring out to both sides with jagged fur tips;
  do not shrink them, do not make them floppy, do not round them off)
- Short round front and hind legs (no separated toes)
- Fur colors (cream beige base, silver-grey accents on the crown, around the ears,
  along the back and from the chest down the front legs)
- The fluffy jagged fur silhouette
- Eye style (fairly large solid black ovals, no white highlight)
- Nose and mouth (small dark-brown round nose, W-shaped mouth below it, pink inside when open)
- Cheeks (two pink diagonal strokes on each cheek)
- Line color and weight (thick hand-drawn dark-brown outlines)
- Coloring texture (grainy colored-pencil / crayon shading with uneven hand-drawn strokes)

MUST FOLLOW:
- Exactly one character. Not a grid, not multiple variations
- Always draw the full body, never cut off by the edge of the canvas
- No objects and no scenery in the background (the art will be cut out later)
- No shadows, no ground, no gradients, no patterns
- No text and no numbers anywhere

POSE: offering a steaming teacup with both paws, warm caring smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>
