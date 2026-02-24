#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_remaining_headers.py
nav.top-nav や別形式 header の残り数ファイルを統一ヘッダーに差し替え
"""

import os
import re
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')


def build_header(title):
    return f'''    <header style="position:sticky;top:0;z-index:50;background:white;border-bottom:2px solid #e2e8f0;box-shadow:0 1px 4px rgba(0,0,0,0.08);">
      <div style="max-width:1400px;margin:0 auto;padding:0 32px;height:56px;display:flex;align-items:center;">
        <a href="/index.html" style="display:inline-flex;align-items:center;gap:8px;color:#1e3a8a;text-decoration:none;font-size:14px;font-weight:700;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
          ポータルへ戻る
        </a>
        <div style="width:1px;height:20px;background:#cbd5e1;margin:0 16px;"></div>
        <span style="font-size:15px;font-weight:700;color:#334155;">{title}</span>
      </div>
    </header>'''


def get_title(content):
    m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    return m.group(1).strip() if m else ''


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

        # 既に統一ヘッダーが入っていればスキップ
        if 'border-bottom:2px solid #e2e8f0;box-shadow:0 1px 4px' in content:
            continue

        # ポータルへ戻るリンクがないファイルはスキップ
        if 'ポータルへ戻る' not in content:
            continue

        original = content
        title = get_title(content)
        if not title:
            continue

        new_header = build_header(title)

        # パターンA: <nav class="top-nav"> ... </nav>
        nav_match = re.search(
            r'\s*(?:<!--.*?-->\s*)?<nav class="top-nav">.*?</nav>',
            content, re.DOTALL
        )
        if nav_match and 'ポータルへ戻る' in nav_match.group(0):
            content = content[:nav_match.start()] + '\n' + new_header + content[nav_match.end():]

        # パターンB: <header style="background:white; ..."> ... </header>
        if content == original:
            header_match = re.search(
                r'\s*<header style="background:\s*white;[^"]*position:\s*sticky;[^"]*">'
                r'.*?</header>',
                content, re.DOTALL
            )
            if header_match and 'ポータルへ戻る' in header_match.group(0):
                content = content[:header_match.start()] + '\n' + new_header + content[header_match.end():]

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  [FIXED] {fname}')
            updated += 1
        else:
            print(f'  [SKIP] {fname}')

    print(f'\n修正: {updated} ファイル')


if __name__ == '__main__':
    main()
