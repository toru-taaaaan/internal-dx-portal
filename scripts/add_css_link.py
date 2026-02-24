#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""portal_nexus.css を未リンクの layout-wrapper ファイルに追加"""
import os, re

CSS_LINK = '<link rel="stylesheet" href="assets/portal_nexus.css">'

src = os.path.join(os.path.dirname(__file__), '..', 'src')
count = 0
for fname in sorted(os.listdir(src)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(src, fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'layout-wrapper' in content and 'portal_nexus.css' not in content:
        new_content = re.sub(
            r'(</head>)',
            CSS_LINK + '\n' + r'\1',
            content, count=1, flags=re.IGNORECASE
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'OK: {fname}')

print(f'Done: {count}件にCSSリンクを追加')
