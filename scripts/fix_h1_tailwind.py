#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_h1_tailwind.py
Tailwind CDN preflight が h1 { font-size: inherit } で上書きする問題を修正。
inline <style> 内の h1 の font-size / font-weight に !important を追加。
"""

import os
import re
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')


def fix_file(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tailwind CDN を使っていないファイルはスキップ
    if 'cdn.tailwindcss.com' not in content:
        return False

    original = content

    # <style> ブロック内の h1 定義を探して font-size / font-weight に !important を追加
    # h1 に既に !important がある場合はスキップ
    def add_important(match):
        block = match.group(0)
        if '!important' in block:
            return block  # 既に修正済み
        block = re.sub(
            r'(font-size\s*:\s*[^;!]+?)(\s*;)',
            r'\1 !important\2',
            block
        )
        block = re.sub(
            r'(font-weight\s*:\s*[^;!]+?)(\s*;)',
            r'\1 !important\2',
            block
        )
        block = re.sub(
            r'(margin\s*:\s*[^;!]+?)(\s*;)',
            r'\1 !important\2',
            block
        )
        return block

    # h1 { ... } ブロック（<style>内のみ）
    # 各<style>ブロック内で処理
    def fix_style_block(style_match):
        style_content = style_match.group(0)
        # h1 { ... } を探す（セレクタがh1のみ、.sidebar-header h1 等は除外）
        style_content = re.sub(
            r'(?<![.\w-])\bh1\s*\{[^}]*\}',
            add_important,
            style_content
        )
        return style_content

    content = re.sub(
        r'<style[^>]*>.*?</style>',
        fix_style_block,
        content,
        flags=re.DOTALL
    )

    changed = content != original
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  [FIXED] {fname}')
    else:
        print(f'  [OK] {fname}')

    return changed


def main():
    src_dir = os.path.abspath(SRC_DIR)
    html_files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    fixed = 0

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname == 'index.html':
            continue
        if fix_file(fpath):
            fixed += 1

    print(f'\n修正: {fixed} ファイル')


if __name__ == '__main__':
    main()
