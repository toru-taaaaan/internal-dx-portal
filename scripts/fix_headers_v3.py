#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_headers_v3.py
1. version-header（黒いバー）削除
2. btn-portal（旧戻るボタン）削除
3. 重複「ポータルへ戻る」解消（既存ヘッダーがある場合は新ヘッダー削除）
4. 新ヘッダーのスタイルを改善（目立つデザインに）
"""

import os
import re
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')

# スクリプトが追加した新ヘッダー（削除対象 or 差し替え対象）
OLD_HEADER = '''    <header style="position:sticky;top:0;z-index:50;background:white;border-bottom:1px solid #e2e8f0;padding:0 24px;height:48px;display:flex;align-items:center;">
      <a href="/index.html" style="display:flex;align-items:center;gap:8px;color:#64748b;text-decoration:none;font-size:13px;font-weight:600;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
        ポータルへ戻る
      </a>
    </header>'''

# 改善版ヘッダー（目立つデザイン）
NEW_HEADER = '''    <header style="position:sticky;top:0;z-index:50;background:#f8fafc;border-bottom:2px solid #e2e8f0;padding:0 32px;height:52px;display:flex;align-items:center;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
      <a href="/index.html" style="display:inline-flex;align-items:center;gap:8px;color:#1e3a8a;text-decoration:none;font-size:14px;font-weight:700;padding:6px 16px;border-radius:6px;border:1px solid #bfdbfe;background:#eff6ff;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
        DXポータルへ戻る
      </a>
    </header>'''


def fix_file(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    actions = []

    # --- 1. version-header 削除 ---
    # <div class="version-header">...</div> ブロック削除
    if 'version-header' in content:
        content = re.sub(
            r'\n?\s*<div class="version-header">.*?</div>\s*\n?',
            '\n', content, flags=re.DOTALL
        )
        # CSS定義も削除
        content = re.sub(
            r'\s*\.version-header\s*\{[^}]*\}\s*',
            '\n', content
        )
        actions.append('version-header削除')

    # --- 2. btn-portal（旧戻るボタン）削除 ---
    if 'btn-portal' in content:
        # ボタンを含むdiv全体を削除
        content = re.sub(
            r'\n?\s*<div[^>]*>\s*<button[^>]*class="btn-portal"[^>]*>.*?</button>\s*</div>\s*\n?',
            '\n', content, flags=re.DOTALL
        )
        # CSS定義も削除
        content = re.sub(
            r'\s*\.btn-portal\s*\{[^}]*\}\s*',
            '\n', content
        )
        content = re.sub(
            r'\s*\.btn-portal:hover\s*\{[^}]*\}\s*',
            '\n', content
        )
        actions.append('btn-portal削除')

    # --- 3. 重複ヘッダー処理 ---
    portal_count = content.count('ポータルへ戻る')

    if portal_count >= 2 and OLD_HEADER in content:
        # 既存のスティッキーヘッダーがあるので、新ヘッダーを削除
        content = content.replace(OLD_HEADER + '\n', '')
        if OLD_HEADER in content:
            content = content.replace(OLD_HEADER, '')
        actions.append('重複ヘッダー削除')
    elif portal_count == 1 and OLD_HEADER in content:
        # 新ヘッダーのみ → スタイル改善版に差し替え
        content = content.replace(OLD_HEADER, NEW_HEADER)
        actions.append('ヘッダースタイル改善')

    # 余分な空行整理
    content = re.sub(r'\n{3,}', '\n\n', content)

    changed = content != original
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  [FIXED] {fname} ({", ".join(actions)})')
    else:
        print(f'  [OK] {fname}')

    return changed


def main():
    src_dir = os.path.abspath(SRC_DIR)
    print(f'対象: {src_dir}\n')

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
