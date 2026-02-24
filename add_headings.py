import re

FILE = 'src/Antigravity_操作ガイド.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

IMG_PREFIX = 'https://codelabs.developers.google.com/static/getting-started-google-antigravity/img/'

def add_h3(content, img_filename, heading, occurrence=1):
    """img_filenameの前にh3見出しを追加（nonce回目の出現に対して）"""
    old = f'<div style="margin: 20px 0 28px; text-align: center;">\n        <img src="{IMG_PREFIX}{img_filename}'
    new = f'<h3 style="font-size:15px; font-weight:700; color:var(--dark); margin:28px 0 8px;">{heading}</h3>\n      <div style="margin: 0 0 28px; text-align: center;">\n        <img src="{IMG_PREFIX}{img_filename}'
    
    count = 0
    idx = 0
    while True:
        idx = content.find(old, idx)
        if idx == -1:
            print(f"WARNING: not found → {img_filename} (occurrence={occurrence})")
            return content
        count += 1
        if count == occurrence:
            content = content[:idx] + new + content[idx + len(old):]
            print(f"OK: [{heading}] before {img_filename}")
            return content
        idx += len(old)

# ── s-overview / s-step1 共通3画像 (各セクションで2枚目・3枚目に見出し)
# occurrence=1 → s-overview の 2枚目
content = add_h3(content, '281ac826fb44d427.png', 'Agent Manager', occurrence=1)
content = add_h3(content, 'e8afd782a8f92129.png', 'Editor', occurrence=1)

# occurrence=1 → s-step1 の 2枚目（s-overview 側は変換済みで margin:0 になっているので引っかからない）
content = add_h3(content, '281ac826fb44d427.png', 'Agent Manager', occurrence=1)
content = add_h3(content, 'e8afd782a8f92129.png', 'Editor', occurrence=1)

# ── s-step2: インストール (2枚目に見出し)
content = add_h3(content, '7ca55560ec377130.png', 'セキュリティポリシー設定')

# ── s-step3: Agent Manager (2枚目以降に見出し)
content = add_h3(content, 'ec72712ea24bf6d5.png', 'ワークスペース選択')
content = add_h3(content, '156224e223eeda36.png', 'Agent Manager ウィンドウ')
content = add_h3(content, 'fb0744dc43911365.png', 'モデル選択')
content = add_h3(content, 'f403e40ad480efc9.png', 'プランニングモード')
# 22f6dcf7b3edc583: s-step3 (1回目) に見出し、s-step12 (2回目) には不要
content = add_h3(content, '22f6dcf7b3edc583.png', '各部位の説明', occurrence=1)

# ── s-step4: Browser (2枚目以降に見出し)
content = add_h3(content, 'e7119f40e093afd2.png', 'セットアップ開始')
content = add_h3(content, '82fb87d7d75b4a6c.png', 'Chrome 拡張のインストール')
content = add_h3(content, 'f3468f0e5f3bb075.png', 'Chrome ウェブストア')
content = add_h3(content, '7f0367e00ac36d5a.png', 'ブラウザ操作中')
content = add_h3(content, 'b9d89e1ebefcfd76.png', 'Agent Manager に戻る')
content = add_h3(content, '77fcc38b5fb4ca7c.png', 'アクセス許可後')

# ── s-step5: Artifacts (2枚目以降に見出し)
content = add_h3(content, '5320f447471c43eb.png', 'Agent Manager の Artifacts')
content = add_h3(content, '19d9738bb3c7c0c9.png', 'Artifacts ビュー')
content = add_h3(content, 'e1d8fd6e7df4daf3.png', 'Review Changes')

# ── s-step6: Inbox (2枚目に見出し)
content = add_h3(content, 'b7e493765cfb1b1a.png', 'Inbox 詳細')

# ── s-step9: Rules と Workflows (2枚目以降に見出し)
content = add_h3(content, 'bfd179dfef6b2355.png', 'Rules')
content = add_h3(content, 'd22059258592f0e1.png', 'Workflows 一覧')
content = add_h3(content, '8a3efd9e3be7eb6f.png', 'Workflow 詳細')
content = add_h3(content, '11febd7940ef8199.png', 'Workflow の実行')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll done!")
