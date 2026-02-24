#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upgrade_header_v2.py
戻るヘッダーを目立つネイビーバーに差し替え
"""

import os
import re
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')

# 新しいヘッダー（ネイビーバー・白文字・大きめ）
NAVY_HEADER = '''    <header style="position:sticky;top:0;z-index:50;background:#1e3a8a;padding:0 32px;height:56px;display:flex;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);">
      <a href="/index.html" style="display:inline-flex;align-items:center;gap:10px;color:white;text-decoration:none;font-size:15px;font-weight:700;padding:8px 20px;border-radius:8px;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
        DXポータルへ戻る
      </a>
    </header>'''


def main():
    src_dir = os.path.abspath(SRC_DIR)
    html_files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    updated = 0

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname == 'index.html':
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # パターン1: fix_headers_v3.py が入れた改善版ヘッダー（background:#f8fafc）
        content = re.sub(
            r'<header style="position:sticky;top:0;z-index:50;background:#f8fafc;[^"]*">\s*'
            r'<a href="/index\.html"[^>]*>\s*'
            r'<svg[^>]*>.*?</svg>\s*'
            r'DXポータルへ戻る\s*'
            r'</a>\s*'
            r'</header>',
            NAVY_HEADER,
            content,
            flags=re.DOTALL
        )

        # パターン2: 各ページ独自のスティッキーヘッダー（background:whiteなど）
        # "ポータルへ戻る" または "DXポータルへ戻る" を含むstickyヘッダー
        if NAVY_HEADER not in content:
            content = re.sub(
                r'<header style="position:\s*sticky;[^"]*">\s*'
                r'<a href="(?:/index\.html|index\.html)"[^>]*>\s*'
                r'(?:<svg[^>]*>.*?</svg>\s*)?'
                r'(?:DX)?ポータル(?:トップ)?へ戻る\s*'
                r'</a>\s*'
                r'</header>',
                NAVY_HEADER,
                content,
                flags=re.DOTALL
            )

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  [UPDATED] {fname}')
            updated += 1
        else:
            # ヘッダーがないか、既にネイビー版
            if NAVY_HEADER in content:
                print(f'  [OK] {fname}')
            elif 'ポータルへ戻る' in content or 'DXポータルへ戻る' in content:
                print(f'  [SKIP] {fname} (パターン不一致)')
            else:
                print(f'  [NO-HEADER] {fname}')

    print(f'\n更新: {updated} ファイル')


if __name__ == '__main__':
    main()
