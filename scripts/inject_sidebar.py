#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inject_sidebar.py
全HTMLファイルに統一カテゴリ折りたたみサイドバーを注入するスクリプト

使用方法:
    python scripts/inject_sidebar.py           # 実際に変更
    python scripts/inject_sidebar.py --dry-run # プレビューのみ
"""

import os
import re
import sys
import shutil

SRC_DIR = os.path.join(os.path.dirname(__file__), '..', 'src')

# ===== 削除対象ファイル =====
FILES_TO_DELETE = [
    'landing.html',
    'archive_resources.html',
    'SITEMAP.html',
    'project_15_12_proposal.html',
]

# ===== 統一サイドバーHTML =====
SIDEBAR_HTML = '''\
<aside class="sidebar">
  <header class="sidebar-header">
    <h1>AKIBAホールディングス</h1>
    <p>情報システム部 DXポータル</p>
  </header>
  <nav>
    <!-- ホーム -->
    <div class="nav-category" data-category="home">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>ホーム</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/index.html" class="nav-link">ダッシュボード</a>
        <a href="https://docs.google.com/spreadsheets/d/1_ehi9Ylc16KD3WfGNfktRzTtDQsvlXVsWo1_5x0L3c8/edit" class="nav-link" target="_blank" rel="noopener">タスク管理表 ↗</a>
      </div>
    </div>
    <!-- NW ネットワーク -->
    <div class="nav-category" data-category="nw">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>NW ネットワーク</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/SD-WAN刷新_3社4シナリオ比較検討資料.html" class="nav-link"><span class="nav-id">NW-001</span>SD-WAN 3社比較</a>
        <a href="/ネットワーク・セキュリティ刷新_費用比較.html" class="nav-link"><span class="nav-id">NW-002</span>NW刷新 費用比較</a>
        <a href="/VarioSecure費用分解_整理ノート.html" class="nav-link"><span class="nav-id">NW-003</span>VarioSecure費用分解</a>
        <a href="/network_topology.html" class="nav-link"><span class="nav-id">NW-004</span>構成図</a>
        <a href="/sdwan_scope_definition.html" class="nav-link"><span class="nav-id">NW-005</span>対象拠点定義</a>
        <a href="/bcp_risk_matrix.html" class="nav-link"><span class="nav-id">NW-006</span>BCP リスク評価</a>
      </div>
    </div>
    <!-- AD 認証基盤 -->
    <div class="nav-category" data-category="ad">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>AD 認証基盤</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/ADクラウド移行_3社比較・導入計画.html" class="nav-link"><span class="nav-id">AD-001</span>3社比較・導入計画</a>
        <a href="/AD・EntraID刷新_移行シナリオ比較検討資料.html" class="nav-link"><span class="nav-id">AD-002</span>EntraID移行シナリオ</a>
        <a href="/AD・SECOM同時依頼_コスト最適化分析.html" class="nav-link"><span class="nav-id">AD-003</span>AD+SECOMコスト最適化</a>
        <a href="/ADクラウド化_3社権限・責任分界点.html" class="nav-link"><span class="nav-id">AD-004</span>3社 権限・分界点</a>
        <a href="/project_15_01_entraid_proposal.html" class="nav-link"><span class="nav-id">AD-005</span>EntraID移行提案</a>
      </div>
    </div>
    <!-- ACC 入退室 -->
    <div class="nav-category" data-category="acc">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>ACC 入退室</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/入退室管理_フルクラウド型_ベンダー調査.html" class="nav-link"><span class="nav-id">ACC-001</span>ベンダー調査</a>
        <a href="/SECOM入退室クラウド化_導入検討資料.html" class="nav-link"><span class="nav-id">ACC-002</span>SECOMクラウド化検討</a>
        <a href="/判断フロー_SECOM問題.html" class="nav-link"><span class="nav-id">ACC-003</span>SECOM判断フロー</a>
      </div>
    </div>
    <!-- FIN 予算・契約 -->
    <div class="nav-category" data-category="fin">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>FIN 予算・契約</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/IT基盤刷新_概算予算一覧.html" class="nav-link"><span class="nav-id">FIN-001</span>概算予算一覧</a>
        <a href="/IT基盤刷新_説明資料.html" class="nav-link"><span class="nav-id">FIN-002</span>IT基盤刷新 説明資料</a>
        <a href="/契約管理台帳.html" class="nav-link"><span class="nav-id">FIN-003</span>契約管理台帳</a>
        <a href="/エビデンス集.html" class="nav-link"><span class="nav-id">FIN-004</span>エビデンス集</a>
      </div>
    </div>
    <!-- AI AI Champion -->
    <div class="nav-category" data-category="ai">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>AI Champion</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/AI_Champion_カリキュラム.html" class="nav-link"><span class="nav-id">AI-001</span>カリキュラム</a>
        <a href="/AI_Champion_ハンドブック.html" class="nav-link"><span class="nav-id">AI-002</span>ハンドブック</a>
        <a href="/Antigravity_操作ガイド.html" class="nav-link"><span class="nav-id">AI-003</span>Antigravity操作ガイド</a>
        <a href="/Antigravity_セキュリティガイドライン.html" class="nav-link"><span class="nav-id">AI-004</span>セキュリティGL</a>
        <a href="/Antigravity_想定問答集.html" class="nav-link"><span class="nav-id">AI-005</span>想定問答集</a>
        <a href="/project_15_12.html" class="nav-link"><span class="nav-id">AI-006</span>AI Champion Portal</a>
        <a href="/project_15_12_antigravity.html" class="nav-link"><span class="nav-id">AI-007</span>Antigravity導入案内</a>
        <a href="/project_15_12_ishii.html" class="nav-link"><span class="nav-id">AI-008</span>相談資料（石井）</a>
      </div>
    </div>
    <!-- OPS 運用・管理 -->
    <div class="nav-category" data-category="ops">
      <div class="nav-category-header" onclick="toggleCategory(this)">
        <span>OPS 運用・管理</span>
        <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
      </div>
      <div class="nav-category-items">
        <a href="/executive_hub.html" class="nav-link"><span class="nav-id">OPS-001</span>全体課題管理表</a>
        <a href="/evaluation_sheet.html" class="nav-link"><span class="nav-id">OPS-002</span>人事考課原本</a>
        <a href="/daily_log.html" class="nav-link"><span class="nav-id">OPS-003</span>活動ログ</a>
        <a href="/ヒアリング管理.html" class="nav-link"><span class="nav-id">OPS-004</span>ヒアリング管理</a>
        <a href="/file_server_cloud_migration.html" class="nav-link"><span class="nav-id">OPS-005</span>ファイルサーバー統合</a>
        <a href="/project_15_14.html" class="nav-link"><span class="nav-id">OPS-006</span>Infra Assessment</a>
        <a href="/project_bn_report.html" class="nav-link"><span class="nav-id">OPS-007</span>BuddyNetレポート</a>
      </div>
    </div>
  </nav>
  <footer class="sidebar-footer">
    <p>情報システム部 丹治</p>
  </footer>
</aside>'''

# ===== サイドバーのJS =====
SIDEBAR_JS = '''\
<script>
function toggleCategory(header) {
  header.parentElement.classList.toggle('collapsed');
}
document.addEventListener('DOMContentLoaded', function() {
  var currentPath = location.pathname.split('/').pop() || 'index.html';
  var categories = document.querySelectorAll('.nav-category');
  categories.forEach(function(cat) {
    var links = cat.querySelectorAll('.nav-link');
    var isActive = false;
    links.forEach(function(link) {
      var href = link.getAttribute('href');
      if (href && href.split('/').pop() === currentPath) {
        link.classList.add('active');
        isActive = true;
      }
    });
    if (!isActive) {
      cat.classList.add('collapsed');
    }
  });
});
</script>'''


def has_sidebar(content):
    """既存のサイドバーがあるか確認"""
    return bool(re.search(r'<aside\s[^>]*class=["\'][^"\']*sidebar[^"\']*["\']', content, re.IGNORECASE)
                or re.search(r'<aside\s+class="sidebar"', content, re.IGNORECASE))


def replace_sidebar(content):
    """既存の<aside class="sidebar">...</aside> を置換"""
    # aside.sidebar ブロック全体を正規表現で検出（ネストを考慮してシンプルな方法）
    # <aside ... sidebar ... > から </aside> まで
    pattern = re.compile(
        r'<aside[^>]*class=["\'][^"\']*sidebar[^"\']*["\'][^>]*>.*?</aside>',
        re.DOTALL | re.IGNORECASE
    )
    result, count = pattern.subn(SIDEBAR_HTML, content, count=1)
    if count == 0:
        # class属性が先に来るパターン
        pattern2 = re.compile(r'<aside\s+class="sidebar">.*?</aside>', re.DOTALL)
        result, count = pattern2.subn(SIDEBAR_HTML, content, count=1)
    return result, count > 0


def inject_sidebar_into_no_sidebar(content):
    """サイドバーなしのHTMLにlayout-wrapper + サイドバー + main-scrollを追加"""
    # すでにlayout-wrapperがある場合はサイドバー置換として扱う（念のためチェック）
    if 'layout-wrapper' in content:
        # layout-wrapperはあるがasideがない → サイドバーをlayout-wrapper直後に挿入
        pattern = re.compile(r'(<div[^>]*class=["\'][^"\']*layout-wrapper[^"\']*["\'][^>]*>)', re.IGNORECASE)
        m = pattern.search(content)
        if m:
            insert_pos = m.end()
            content = content[:insert_pos] + '\n    ' + SIDEBAR_HTML + content[insert_pos:]
            return content, True
        return content, False

    # <body...> を検出して直後にlayout-wrapper + sidebarを挿入
    body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
    body_match = body_pattern.search(content)
    if not body_match:
        return content, False

    body_tag = body_match.group(1)
    body_end = body_match.end()

    # </body> の直前にJSと閉じタグを追加
    close_body_pattern = re.compile(r'</body>', re.IGNORECASE)

    # bodyタグの直後のコンテンツをmain-scrollで囲む
    rest_after_body = content[body_end:]

    # </body>で分割
    close_match = close_body_pattern.search(rest_after_body)
    if not close_match:
        return content, False

    original_main_content = rest_after_body[:close_match.start()]
    after_close = rest_after_body[close_match.start():]  # </body>以降

    new_body_content = (
        '\n<div class="layout-wrapper">\n'
        + '    ' + SIDEBAR_HTML + '\n'
        + '    <main class="main-scroll">'
        + original_main_content
        + '    </main>\n'
        + SIDEBAR_JS + '\n'
        + '</div>\n'
    )

    return content[:body_end] + new_body_content + after_close, True


def inject_js_before_body_close(content):
    """JSが未挿入の場合、</body>直前に挿入"""
    if 'function toggleCategory' in content:
        return content  # すでにJS挿入済み
    close_body_pattern = re.compile(r'</body>', re.IGNORECASE)
    return close_body_pattern.sub(SIDEBAR_JS + '\n</body>', content, count=1)


def process_file(filepath, dry_run=False):
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    if has_sidebar(original):
        new_content, changed = replace_sidebar(original)
        if changed:
            # JSも挿入
            new_content = inject_js_before_body_close(new_content)
            action = 'REPLACE sidebar'
        else:
            action = 'SKIP (sidebar pattern not matched)'
            changed = False
    else:
        new_content, changed = inject_sidebar_into_no_sidebar(original)
        action = 'ADD sidebar+layout' if changed else 'SKIP (no body tag)'

    if changed:
        print(f'  [{action}] {filename}')
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
    else:
        print(f'  [SKIP] {filename}')

    return changed


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print('=== DRY RUN モード（変更なし） ===\n')
    else:
        print('=== 実行モード（ファイルを変更します） ===\n')

    src_dir = os.path.abspath(SRC_DIR)
    print(f'対象ディレクトリ: {src_dir}\n')

    # --- 削除対象ファイルの処理 ---
    print('--- 削除対象ファイル ---')
    for fname in FILES_TO_DELETE:
        fpath = os.path.join(src_dir, fname)
        if os.path.exists(fpath):
            print(f'  [DELETE] {fname}')
            if not dry_run:
                os.remove(fpath)
        else:
            print(f'  [NOT FOUND] {fname} (スキップ)')

    print()

    # --- HTMLファイルの処理 ---
    print('--- サイドバー注入 ---')
    html_files = [f for f in os.listdir(src_dir)
                  if f.endswith('.html') and f not in FILES_TO_DELETE]
    html_files.sort()

    changed_count = 0
    for fname in html_files:
        fpath = os.path.join(src_dir, fname)
        if process_file(fpath, dry_run=dry_run):
            changed_count += 1

    print(f'\n完了: {changed_count}/{len(html_files)} ファイルを処理しました。')


if __name__ == '__main__':
    main()
