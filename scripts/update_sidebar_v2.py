#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_sidebar_v2.py
資料ページからサイドバーを完全削除し、戻るヘッダーを追加する。
index.html はサイドバー維持（トグルボタンのみ削除）。

使用方法:
    python scripts/update_sidebar_v2.py --dry-run   # プレビュー
    python scripts/update_sidebar_v2.py              # 実行
"""

import os
import re
import sys
import glob

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')

BACK_HEADER = '''\
    <header style="position:sticky;top:0;z-index:50;background:white;border-bottom:1px solid #e2e8f0;padding:0 24px;height:48px;display:flex;align-items:center;">
      <a href="/index.html" style="display:flex;align-items:center;gap:8px;color:#64748b;text-decoration:none;font-size:13px;font-weight:600;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
        ポータルへ戻る
      </a>
    </header>'''

INDEX_JS = '''\
<script>
function toggleCategory(header) {
  header.parentElement.classList.toggle('collapsed');
}
document.addEventListener('DOMContentLoaded', function() {
  var rawPath = location.pathname.split('/').pop() || 'index.html';
  var currentPath = decodeURIComponent(rawPath);
  var categories = document.querySelectorAll('.nav-category');
  categories.forEach(function(cat) {
    var links = cat.querySelectorAll('.nav-link');
    var isActive = false;
    links.forEach(function(link) {
      var href = link.getAttribute('href');
      if (href) {
        var linkFile = decodeURIComponent(href.split('/').pop());
        if (linkFile === currentPath) {
          link.classList.add('active');
          isActive = true;
        }
      }
    });
    if (!isActive) {
      cat.classList.add('collapsed');
    }
  });
});
</script>'''


def process_resource_page(filepath, dry_run=False):
    """資料ページ: サイドバー完全削除 + 戻るヘッダー追加"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. sidebar-toggle ボタン削除
    content = re.sub(
        r'[ \t]*<button class="sidebar-toggle"[^>]*>.*?</button>[ \t]*\n?',
        '', content, flags=re.DOTALL
    )

    # 2. <!-- サイドバー --> コメント削除
    content = re.sub(r'[ \t]*<!--\s*サイドバー\s*-->[ \t]*\n?', '', content)

    # 3. <aside class="sidebar">...</aside> ブロック削除
    content = re.sub(
        r'[ \t]*<aside\s+class="sidebar">.*?</aside>[ \t]*\n?',
        '', content, flags=re.DOTALL
    )

    # 4. layout-wrapper に sidebar-hidden クラス追加
    content = content.replace(
        '<div class="layout-wrapper">',
        '<div class="layout-wrapper sidebar-hidden">'
    )

    # 5. main-scroll の直後に戻るヘッダー挿入
    content = re.sub(
        r'(<main class="main-scroll">)',
        r'\1\n' + BACK_HEADER,
        content
    )

    # 6. toggleSidebar を含む <script> ブロック全体を削除
    content = re.sub(
        r'\n?<script>\s*function toggleSidebar[\s\S]*?</script>',
        '', content
    )

    # 余分な空行整理
    content = re.sub(r'\n{3,}', '\n\n', content)

    changed = content != original
    if changed and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return changed


def process_index(filepath, dry_run=False):
    """index.html: トグルボタン削除、サイドバー維持、JS整理"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. sidebar-toggle ボタン削除
    content = re.sub(
        r'[ \t]*<button class="sidebar-toggle"[^>]*>.*?</button>[ \t]*\n?',
        '', content, flags=re.DOTALL
    )

    # 2. toggleSidebar を含む <script> ブロック → toggleCategory + DOMContentLoaded のみに差し替え
    content = re.sub(
        r'<script>\s*function toggleSidebar[\s\S]*?</script>',
        INDEX_JS,
        content
    )

    # 余分な空行整理
    content = re.sub(r'\n{3,}', '\n\n', content)

    changed = content != original
    if changed and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return changed


def main():
    dry_run = '--dry-run' in sys.argv
    src_dir = os.path.abspath(SRC_DIR)

    mode = 'DRY RUN' if dry_run else '実行'
    print(f'=== {mode} ===')
    print(f'対象: {src_dir}\n')

    html_files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    updated = 0

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname == 'index.html':
            changed = process_index(fpath, dry_run=dry_run)
            status = 'UPDATED' if changed else 'NO CHANGE'
            print(f'  [INDEX {status}] {fname}')
        else:
            changed = process_resource_page(fpath, dry_run=dry_run)
            status = 'UPDATED' if changed else 'NO CHANGE'
            print(f'  [{status}] {fname}')

        if changed:
            updated += 1

    print(f'\n完了: {updated}/{len(html_files)} ファイル更新')


if __name__ == '__main__':
    main()
