#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_duplicate_header.py
既存のスティッキーヘッダーがあるファイルから、
新規追加した重複ヘッダーを削除する。
"""

import os
import re
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')

# 新規追加したヘッダーの正確なパターン
NEW_HEADER = '''    <header style="position:sticky;top:0;z-index:50;background:white;border-bottom:1px solid #e2e8f0;padding:0 24px;height:48px;display:flex;align-items:center;">
      <a href="/index.html" style="display:flex;align-items:center;gap:8px;color:#64748b;text-decoration:none;font-size:13px;font-weight:600;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
        ポータルへ戻る
      </a>
    </header>'''


def main():
    src_dir = os.path.abspath(SRC_DIR)
    html_files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    fixed = 0

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname == 'index.html':
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 「ポータルへ戻る」が2回以上ある場合だけ修正
        count = content.count('ポータルへ戻る')
        if count >= 2:
            # 新規追加ヘッダーを削除（改行含む）
            new_content = content.replace(NEW_HEADER + '\n', '')
            if new_content == content:
                # 改行なしパターン
                new_content = content.replace(NEW_HEADER, '')

            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'  [FIXED] {fname} (重複ヘッダー削除)')
                fixed += 1
            else:
                print(f'  [SKIP] {fname} (パターン不一致)')
        # 「ポータルへ戻る」が0回 = 古い形式の戻るボタン("ポータルトップへ戻る"等)がある可能性
        elif count == 0:
            # "戻る" を含む既存リンクがあるか確認
            if '戻る' in content and NEW_HEADER not in content:
                print(f'  [INFO] {fname} (「戻る」リンクあり、ヘッダー未追加)')

    print(f'\n修正: {fixed} ファイル')


if __name__ == '__main__':
    main()
