# -*- coding: utf-8 -*-
"""リセナ立ち上げ マニュアル定義（A4 両面1枚）。

画像は docs/images/lisena-startup/ に置く。
ビルド: python3 tools/build_manual.py lisena-startup
"""

MANUAL = {
    "slug": "lisena-startup",
    "title": "リセナ立ち上げ",
    "layout": "sheet",
    "author": "株式会社ウェルアップ",
    "meta": [
        ["業務名", "リセナ立ち上げ"],
        ["実施時刻", "8:30まで（温まるまで30分かかるため）"],
        ["様式", "A4 両面1枚"],
        ["改訂日", "2026-10-23"],
    ],
    "pages": [
        {
            "side": "表面",
            "title": "リセナ立ち上げ",
            "highlight": "温まるまでに30分かかるため、<b>8:30まで</b>に実施する。",
            "image": "01-panel.jpg",
            "image_height_mm": 135,
            "steps": [
                {"text": "コンセントを差し込み、<b>電源ON</b>ボタンを押す。"},
                {"text": "温度設定を<b>55℃</b>にする。"},
            ],
            "notes": [
                "立ち上げた際に「水位表示」ランプが<b>低</b>になっていたら、"
                "<b>裏面の給水作業</b>を実施する。",
            ],
        },
        {
            "side": "裏面",
            "title": "給水作業",
            "lead": "ベッド近くのペットボトルから水を足す。"
                    "<b>専用水または水道水のみ</b>使用可能。",
            "image_height_mm": 74,
            "steps": [
                {
                    "text": "ロゴ中央の<b>PUSH</b>ボタンを押し、フタを開ける。",
                    "image": "02-open-lid.jpg",
                },
                {
                    "text": "ペットボトルから給水する。",
                    "image": "03-refill.jpg",
                },
            ],
            "notes": [
                "灰色カバーの網目から<b>溢れない程度</b>まで給水する。",
                "溢れた際は<b>水色のスポイト</b>で水を戻す。"
                "故障の恐れがあるので、溢れたまま運転しないこと。",
            ],
        },
    ],
}
