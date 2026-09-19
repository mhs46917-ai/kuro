# セットB：ネガティブ返事（negative）

「行けたらいく」「だるいわー」など、気を使わない相手に送るゆるいネガティブ。家族・親友・恋人向けで刺さるセット。

## 作り方

1. Gemini に `reference/character.png` を添付する
2. 下の「シート1」のプロンプトを貼って3×3の一覧画像を出す
3. できた画像を `work/sheets/B-sheet1.png` として保存する
4. 一覧画像を1コマずつに切り分ける

```bash
python3 scripts/stickerkit.py split --sheet work/sheets/B-sheet1.png \
    --set B --grid 3x3 --start 1
```

5. 残りのシートも同じように（`--start` の数字を変える）
6. 崩れたコマだけ、下の「1枚ずつ描き直す用」で描き直して `work/raw/B-xx.png` を上書きする
7. `cutout --set B` → `text --set B` → `package --set B`

---

## シート1（B-01 〜 B-09／9コマ）

- 保存先: `work/sheets/B-sheet1.png`
- 切り分け: `python3 scripts/stickerkit.py split --sheet work/sheets/B-sheet1.png --set B --grid 3x3 --start 1`

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
・「行けたらいく」… 目をそらして前足でほっぺをかく。あいまいな半笑い、汗が一滴。
・「だるいわー」… 背中を丸めてだらんと座り込む。半目の無表情、頭の上にどんよりした灰色の雲。
・「むりー」… 力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に白いたましいがふわり。
・「めんどくさい」… 床にごろんと寝転がって足を投げ出す。半目でこちらをちらっと見る。
・「気が向いたらね」… そっぽを向きながら片前足を軽くひらひらさせる。うすい笑み。
・「今日はパス」… 両前足を胸の前で小さくバツにして、首を横に振る。困り眉。
・「ねむすぎる」… 大きなあくび。目に涙がにじみ、片前足で目をこする。
・「つかれた…」… 肩を落としてぺたんと座り込む。耳が垂れ、頭の上に小さな湯気。
・「やる気でない」… 小さなクッションに顔をうずめて突っ伏す。目は線になっている。

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
- "行けたらいく" ... looking away while scratching its cheek with a paw, vague awkward half-smile, one sweat drop
- "だるいわー" ... slouching and sitting limply, half-lidded blank eyes, a gloomy grey cloud above the head
- "むりー" ... collapsed flat on the ground exhausted, eyes squeezed shut, a tiny white soul floating out
- "めんどくさい" ... sprawled on its back on the floor with legs flopped out, glancing at the viewer with half-lidded eyes
- "気が向いたらね" ... looking away while lazily waving one paw, faint noncommittal smile
- "今日はパス" ... making a small X with both paws while shaking its head, troubled eyebrows
- "ねむすぎる" ... huge yawn with watery eyes, rubbing one eye with a paw
- "つかれた…" ... sitting slumped with drooping shoulders, ears down, a small puff of steam above
- "やる気でない" ... face-planted into a small cushion, eyes drawn as flat lines

Background: a flat pale mint green, flat. Square canvas. Output at the highest resolution available.
```

</details>

| コマ | セリフ | ファイル名 |
|---|---|---|
| 1 | 行けたらいく | `B-01.png` |
| 2 | だるいわー | `B-02.png` |
| 3 | むりー | `B-03.png` |
| 4 | めんどくさい | `B-04.png` |
| 5 | 気が向いたらね | `B-05.png` |
| 6 | 今日はパス | `B-06.png` |
| 7 | ねむすぎる | `B-07.png` |
| 8 | つかれた… | `B-08.png` |
| 9 | やる気でない | `B-09.png` |

---

## シート2（B-10 〜 B-16／7コマ）

- 保存先: `work/sheets/B-sheet2.png`
- 切り分け: `python3 scripts/stickerkit.py split --sheet work/sheets/B-sheet2.png --set B --grid 3x3 --start 10`
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
・「お金ない…」… 空っぽのがま口財布を逆さにしてふりふり。涙目で口がへの字。
・「あとでいい？」… 片前足を前に出して「待って」のポーズ。ばつの悪そうな笑顔。
・「しらんがな」… 両前足を軽く広げて肩をすくめる。完全な無表情、目が点。
・「ほっといて」… ぷいっと横を向いて目を閉じる。ほっぺをぷくっと膨らませたすねた顔。
・「やだー」… 床に寝転がって手足をじたばたさせる。口を大きく開けたイヤイヤ顔。
・「まあいっか」… 前足を頭の後ろに組んで天を仰ぐ。吹っ切れたゆるい笑顔。
・「聞いてないよ」… 両前足で耳をぎゅっと塞ぐ。目をぎゅっとつぶる。

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
- "お金ない…" ... shaking an empty coin purse upside down, teary eyes, wobbly frown
- "あとでいい？" ... one paw held out in a wait gesture, sheepish apologetic smile
- "しらんがな" ... shrugging with both paws open, completely deadpan face, dot eyes
- "ほっといて" ... turning its face away with eyes closed, sulking with puffed cheeks
- "やだー" ... lying on its back kicking all four legs in a tantrum, mouth wide open in protest
- "まあいっか" ... paws behind its head, looking up at the sky, carefree relaxed smile
- "聞いてないよ" ... covering both ears tightly with its paws, eyes scrunched shut

Background: a flat pale mint green, flat. Square canvas. Output at the highest resolution available.
```

</details>

| コマ | セリフ | ファイル名 |
|---|---|---|
| 1 | お金ない… | `B-10.png` |
| 2 | あとでいい？ | `B-11.png` |
| 3 | しらんがな | `B-12.png` |
| 4 | ほっといて | `B-13.png` |
| 5 | やだー | `B-14.png` |
| 6 | まあいっか | `B-15.png` |
| 7 | 聞いてないよ | `B-16.png` |

---

## 1枚ずつ描き直す用

グリッドで崩れたコマだけ、これで単体生成して差し替えてください。

<details><summary><b>B-01「行けたらいく」</b> … 目をそらして前足でほっぺをかく。あいまいな半笑い、汗が一滴。</summary>

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
目をそらして前足でほっぺをかく。あいまいな半笑い、汗が一滴。

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

POSE: looking away while scratching its cheek with a paw, vague awkward half-smile, one sweat drop

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-02「だるいわー」</b> … 背中を丸めてだらんと座り込む。半目の無表情、頭の上にどんよりした灰色の雲。</summary>

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
背中を丸めてだらんと座り込む。半目の無表情、頭の上にどんよりした灰色の雲。

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

POSE: slouching and sitting limply, half-lidded blank eyes, a gloomy grey cloud above the head

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-03「むりー」</b> … 力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に白いたましいがふわり。</summary>

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
力尽きて前のめりにぺたんと伏せる。目が「＞＜」、頭の上に白いたましいがふわり。

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

POSE: collapsed flat on the ground exhausted, eyes squeezed shut, a tiny white soul floating out

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-04「めんどくさい」</b> … 床にごろんと寝転がって足を投げ出す。半目でこちらをちらっと見る。</summary>

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
床にごろんと寝転がって足を投げ出す。半目でこちらをちらっと見る。

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

POSE: sprawled on its back on the floor with legs flopped out, glancing at the viewer with half-lidded eyes

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-05「気が向いたらね」</b> … そっぽを向きながら片前足を軽くひらひらさせる。うすい笑み。</summary>

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
そっぽを向きながら片前足を軽くひらひらさせる。うすい笑み。

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

POSE: looking away while lazily waving one paw, faint noncommittal smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-06「今日はパス」</b> … 両前足を胸の前で小さくバツにして、首を横に振る。困り眉。</summary>

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
両前足を胸の前で小さくバツにして、首を横に振る。困り眉。

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

POSE: making a small X with both paws while shaking its head, troubled eyebrows

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-07「ねむすぎる」</b> … 大きなあくび。目に涙がにじみ、片前足で目をこする。</summary>

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
大きなあくび。目に涙がにじみ、片前足で目をこする。

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

POSE: huge yawn with watery eyes, rubbing one eye with a paw

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-08「つかれた…」</b> … 肩を落としてぺたんと座り込む。耳が垂れ、頭の上に小さな湯気。</summary>

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
肩を落としてぺたんと座り込む。耳が垂れ、頭の上に小さな湯気。

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

POSE: sitting slumped with drooping shoulders, ears down, a small puff of steam above

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-09「やる気でない」</b> … 小さなクッションに顔をうずめて突っ伏す。目は線になっている。</summary>

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
小さなクッションに顔をうずめて突っ伏す。目は線になっている。

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

POSE: face-planted into a small cushion, eyes drawn as flat lines

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-10「お金ない…」</b> … 空っぽのがま口財布を逆さにしてふりふり。涙目で口がへの字。</summary>

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
空っぽのがま口財布を逆さにしてふりふり。涙目で口がへの字。

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

POSE: shaking an empty coin purse upside down, teary eyes, wobbly frown

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-11「あとでいい？」</b> … 片前足を前に出して「待って」のポーズ。ばつの悪そうな笑顔。</summary>

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
片前足を前に出して「待って」のポーズ。ばつの悪そうな笑顔。

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

POSE: one paw held out in a wait gesture, sheepish apologetic smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-12「しらんがな」</b> … 両前足を軽く広げて肩をすくめる。完全な無表情、目が点。</summary>

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
両前足を軽く広げて肩をすくめる。完全な無表情、目が点。

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

POSE: shrugging with both paws open, completely deadpan face, dot eyes

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-13「ほっといて」</b> … ぷいっと横を向いて目を閉じる。ほっぺをぷくっと膨らませたすねた顔。</summary>

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
ぷいっと横を向いて目を閉じる。ほっぺをぷくっと膨らませたすねた顔。

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

POSE: turning its face away with eyes closed, sulking with puffed cheeks

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-14「やだー」</b> … 床に寝転がって手足をじたばたさせる。口を大きく開けたイヤイヤ顔。</summary>

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
床に寝転がって手足をじたばたさせる。口を大きく開けたイヤイヤ顔。

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

POSE: lying on its back kicking all four legs in a tantrum, mouth wide open in protest

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-15「まあいっか」</b> … 前足を頭の後ろに組んで天を仰ぐ。吹っ切れたゆるい笑顔。</summary>

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
前足を頭の後ろに組んで天を仰ぐ。吹っ切れたゆるい笑顔。

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

POSE: paws behind its head, looking up at the sky, carefree relaxed smile

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>

<details><summary><b>B-16「聞いてないよ」</b> … 両前足で耳をぎゅっと塞ぐ。目をぎゅっとつぶる。</summary>

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
両前足で耳をぎゅっと塞ぐ。目をぎゅっとつぶる。

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

POSE: covering both ears tightly with its paws, eyes scrunched shut

Background: a flat pale mint green, flat. Square canvas, character centered with margins on all sides.
```

</details>
