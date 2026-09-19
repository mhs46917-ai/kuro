# セットC：共感返事（empathy）

「わかる」「たしかに」「なるほど」に全振りした共感特化セット。会話のテンポを作るので連打で使われます。

## 作り方

1. Gemini に `reference/character.png` を添付する
2. 下の「シート1」のプロンプトを貼って3×3の一覧画像を出す
3. できた画像を `work/sheets/C-sheet1.png` として保存する
4. 一覧画像を1コマずつに切り分ける

```bash
python3 scripts/stickerkit.py split --sheet work/sheets/C-sheet1.png \
    --set C --grid 3x3 --start 1
```

5. 残りのシートも同じように（`--start` の数字を変える）
6. 崩れたコマだけ、下の「1枚ずつ描き直す用」で描き直して `work/raw/C-xx.png` を上書きする
7. `cutout --set C` → `text --set C` → `package --set C`

---

## シート1（C-01 〜 C-09／9コマ）

- 保存先: `work/sheets/C-sheet1.png`
- 切り分け: `python3 scripts/stickerkit.py split --sheet work/sheets/C-sheet1.png --set C --grid 3x3 --start 1`

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
・「わかる」… 目を細めてしみじみうなずく。片前足をそっと胸に当てる。
・「めっちゃわかる」… 前のめりになって何度も激しくうなずく。動きの残像線、目がきらり。
・「たしかに」… 両前足をポンと打ち合わせる。目を見開いた納得顔。
・「なるほど〜」… 前足をあごに当てて感心。頭の上に小さな電球がぽっと灯る。
・「それな」… 前足をビシッとこちらに向けて指さす。ノリノリの笑顔。
・「だよねー」… 首をかしげてにっこり、片前足を軽く上げて同意する。
・「うんうん」… 目を閉じて何度もうなずく。頭の動きを表す小さな残像線を上下に。
・「ほんとそれ」… 両前足をぐっと握って力説する。目を輝かせた熱い表情。
・「わかりみが深い」… 目を閉じて前足を組み、深く大きくうなずく。頭の上に小さな「…！」。

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
- "わかる" ... nodding slowly with narrowed knowing eyes, one paw resting on its chest
- "めっちゃわかる" ... leaning forward nodding vigorously, motion after-image lines, eyes glinting
- "たしかに" ... clapping both front paws together, wide-open eyes, convinced expression
- "なるほど〜" ... paw on chin, impressed look, a small light bulb glowing above the head
- "それな" ... pointing a paw straight at the viewer, hyped grinning face
- "だよねー" ... head tilted with a warm smile, one paw raised lightly in agreement
- "うんうん" ... nodding repeatedly with eyes closed, small motion lines showing the head bobbing
- "ほんとそれ" ... clenching both front paws while passionately agreeing, fired-up shining eyes
- "わかりみが深い" ... eyes closed with front paws folded, nodding deeply, a small ellipsis-exclamation above

Background: a flat pale mint green, flat. Square canvas. Output at the highest resolution available.
```

</details>

| コマ | セリフ | ファイル名 |
|---|---|---|
| 1 | わかる | `C-01.png` |
| 2 | めっちゃわかる | `C-02.png` |
| 3 | たしかに | `C-03.png` |
| 4 | なるほど〜 | `C-04.png` |
| 5 | それな | `C-05.png` |
| 6 | だよねー | `C-06.png` |
| 7 | うんうん | `C-07.png` |
| 8 | ほんとそれ | `C-08.png` |
| 9 | わかりみが深い | `C-09.png` |

---

## シート2（C-10 〜 C-16／7コマ）

- 保存先: `work/sheets/C-sheet2.png`
- 切り分け: `python3 scripts/stickerkit.py split --sheet work/sheets/C-sheet2.png --set C --grid 3x3 --start 10`
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
・「そっかー」… 少し眉を下げてやわらかく微笑み、首をかしげる。
・「ふむふむ」… 丸い眼鏡をかけて小さなメモを見つめる。真剣な表情。
・「わたしも！」… 片前足で自分を指さして目を大きく見開く。うれしそうな笑顔。
・「つらかったね」… 前足をそっと差し出して寄り添う。眉を下げたやさしい目。
・「がんばったね」… 小さなタオルを両前足で持って差し出す。あたたかい笑顔。
・「えらい！」… 両前足で拍手する。目をキラキラさせ、まわりに星が飛ぶ。
・「気持ちわかるよ」… 目を閉じて、そっと抱きしめるように両前足を広げる。まわりにふんわりハート。

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
- "そっかー" ... eyebrows slightly lowered, soft gentle smile, head tilted
- "ふむふむ" ... wearing round glasses, studying a small notepad, focused expression
- "わたしも！" ... pointing at itself with one paw, eyes wide open, delighted smile
- "つらかったね" ... gently reaching out one paw in comfort, lowered brows, tender caring eyes
- "がんばったね" ... holding out a small towel with both paws, warm approving smile
- "えらい！" ... applauding with both front paws, sparkling eyes, stars bursting around
- "気持ちわかるよ" ... eyes closed, both front paws opened wide for a gentle hug, soft hearts floating around

Background: a flat pale mint green, flat. Square canvas. Output at the highest resolution available.
```

</details>

| コマ | セリフ | ファイル名 |
|---|---|---|
| 1 | そっかー | `C-10.png` |
| 2 | ふむふむ | `C-11.png` |
| 3 | わたしも！ | `C-12.png` |
| 4 | つらかったね | `C-13.png` |
| 5 | がんばったね | `C-14.png` |
| 6 | えらい！ | `C-15.png` |
| 7 | 気持ちわかるよ | `C-16.png` |

---

## 1枚ずつ描き直す用

グリッドで崩れたコマだけ、これで単体生成して差し替えてください。

<details><summary><b>C-01「わかる」</b> … 目を細めてしみじみうなずく。片前足をそっと胸に当てる。</summary>

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
目を細めてしみじみうなずく。片前足をそっと胸に当てる。

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

POSE: nodding slowly with narrowed knowing eyes, one paw resting on its chest

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-02「めっちゃわかる」</b> … 前のめりになって何度も激しくうなずく。動きの残像線、目がきらり。</summary>

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
前のめりになって何度も激しくうなずく。動きの残像線、目がきらり。

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

POSE: leaning forward nodding vigorously, motion after-image lines, eyes glinting

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-03「たしかに」</b> … 両前足をポンと打ち合わせる。目を見開いた納得顔。</summary>

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
両前足をポンと打ち合わせる。目を見開いた納得顔。

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

POSE: clapping both front paws together, wide-open eyes, convinced expression

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-04「なるほど〜」</b> … 前足をあごに当てて感心。頭の上に小さな電球がぽっと灯る。</summary>

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
前足をあごに当てて感心。頭の上に小さな電球がぽっと灯る。

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

POSE: paw on chin, impressed look, a small light bulb glowing above the head

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-05「それな」</b> … 前足をビシッとこちらに向けて指さす。ノリノリの笑顔。</summary>

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
前足をビシッとこちらに向けて指さす。ノリノリの笑顔。

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

POSE: pointing a paw straight at the viewer, hyped grinning face

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-06「だよねー」</b> … 首をかしげてにっこり、片前足を軽く上げて同意する。</summary>

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
首をかしげてにっこり、片前足を軽く上げて同意する。

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

POSE: head tilted with a warm smile, one paw raised lightly in agreement

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-07「うんうん」</b> … 目を閉じて何度もうなずく。頭の動きを表す小さな残像線を上下に。</summary>

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
目を閉じて何度もうなずく。頭の動きを表す小さな残像線を上下に。

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

POSE: nodding repeatedly with eyes closed, small motion lines showing the head bobbing

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-08「ほんとそれ」</b> … 両前足をぐっと握って力説する。目を輝かせた熱い表情。</summary>

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
両前足をぐっと握って力説する。目を輝かせた熱い表情。

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

POSE: clenching both front paws while passionately agreeing, fired-up shining eyes

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-09「わかりみが深い」</b> … 目を閉じて前足を組み、深く大きくうなずく。頭の上に小さな「…！」。</summary>

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
目を閉じて前足を組み、深く大きくうなずく。頭の上に小さな「…！」。

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

POSE: eyes closed with front paws folded, nodding deeply, a small ellipsis-exclamation above

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-10「そっかー」</b> … 少し眉を下げてやわらかく微笑み、首をかしげる。</summary>

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
少し眉を下げてやわらかく微笑み、首をかしげる。

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

POSE: eyebrows slightly lowered, soft gentle smile, head tilted

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-11「ふむふむ」</b> … 丸い眼鏡をかけて小さなメモを見つめる。真剣な表情。</summary>

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
丸い眼鏡をかけて小さなメモを見つめる。真剣な表情。

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

POSE: wearing round glasses, studying a small notepad, focused expression

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-12「わたしも！」</b> … 片前足で自分を指さして目を大きく見開く。うれしそうな笑顔。</summary>

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
片前足で自分を指さして目を大きく見開く。うれしそうな笑顔。

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

POSE: pointing at itself with one paw, eyes wide open, delighted smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-13「つらかったね」</b> … 前足をそっと差し出して寄り添う。眉を下げたやさしい目。</summary>

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
前足をそっと差し出して寄り添う。眉を下げたやさしい目。

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

POSE: gently reaching out one paw in comfort, lowered brows, tender caring eyes

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-14「がんばったね」</b> … 小さなタオルを両前足で持って差し出す。あたたかい笑顔。</summary>

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
小さなタオルを両前足で持って差し出す。あたたかい笑顔。

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

POSE: holding out a small towel with both paws, warm approving smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-15「えらい！」</b> … 両前足で拍手する。目をキラキラさせ、まわりに星が飛ぶ。</summary>

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
両前足で拍手する。目をキラキラさせ、まわりに星が飛ぶ。

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

POSE: applauding with both front paws, sparkling eyes, stars bursting around

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>C-16「気持ちわかるよ」</b> … 目を閉じて、そっと抱きしめるように両前足を広げる。まわりにふんわりハート。</summary>

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
目を閉じて、そっと抱きしめるように両前足を広げる。まわりにふんわりハート。

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

POSE: eyes closed, both front paws opened wide for a gentle hug, soft hearts floating around

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>
