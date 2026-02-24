#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unify_header_breadcrumb.py
全リソースページのヘッダーを白背景パンくず式に統一。
「← ポータルへ戻る ｜ ページタイトル」デザイン（目立つ版）
"""

import os
import re
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')


def build_header(title):
    """ページタイトル付きのパンくず式ヘッダーHTMLを生成"""
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
    """<title>タグからページタイトルを取得"""
    m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ''


def fix_file(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    title = get_title(content)
    if not title:
        print(f'  [SKIP] {fname} (titleタグなし)')
        return False

    new_header = build_header(title)

    # --- パターン1: ネイビーバー（前回のスクリプトで入れたもの） ---
    navy_pattern = re.compile(
        r'\s*<header style="position:sticky;top:0;z-index:50;background:#1e3a8a;[^"]*">\s*'
        r'<a href="/index\.html"[^>]*>\s*'
        r'<svg[^>]*>.*?</svg>\s*'
        r'DXポータルへ戻る\s*'
        r'</a>\s*'
        r'</header>',
        re.DOTALL
    )
    if navy_pattern.search(content):
        content = navy_pattern.sub('\n' + new_header, content)

    # --- パターン2: 旧改善版ヘッダー（background:#f8fafc） ---
    old_improved = re.compile(
        r'\s*<header style="position:sticky;top:0;z-index:50;background:#f8fafc;[^"]*">\s*'
        r'<a href="/index\.html"[^>]*>\s*'
        r'<svg[^>]*>.*?</svg>\s*'
        r'DXポータルへ戻る\s*'
        r'</a>\s*'
        r'</header>',
        re.DOTALL
    )
    if old_improved.search(content):
        content = old_improved.sub('\n' + new_header, content)

    # --- パターン3: クラスベースの既存ヘッダー ---
    # <header class="bg-white border-b ... sticky top-0 z-50"> ... </header>
    class_header = re.compile(
        r'\s*(?:<!-- .*? -->\s*)?'
        r'<header class="[^"]*sticky[^"]*">\s*'
        r'.*?'
        r'</header>',
        re.DOTALL
    )
    if class_header.search(content) and 'ポータルへ戻る' in content:
        # クラスベースヘッダー内に「ポータルへ戻る」があれば置換
        match = class_header.search(content)
        if match and 'ポータルへ戻る' in match.group(0):
            content = content[:match.start()] + '\n' + new_header + content[match.end():]

    changed = content != original
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  [UPDATED] {fname}')
    else:
        if 'ポータルへ戻る' in content:
            print(f'  [SKIP] {fname} (パターン不一致)')
        else:
            print(f'  [NO-HEADER] {fname}')

    return changed


def main():
    src_dir = os.path.abspath(SRC_DIR)
    html_files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    updated = 0

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname == 'index.html':
            continue
        if fix_file(fpath):
            updated += 1

    print(f'\n更新: {updated} ファイル')


if __name__ == '__main__':
    main()
