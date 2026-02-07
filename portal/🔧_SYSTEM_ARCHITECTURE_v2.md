# 🔧 Internal DX Portal - システムアーキテクチャ完全ガイド v2.0

**作成日**: 2026-02-07
**対象**: Akiba Holdings 社内DX Portal システム（丹治統 管理）
**目的**: 複雑化した6つのプロジェクトHTMLファイルの完全統一・整理

---

## 📋 目次

1. [全体構成](#全体構成)
2. [ファイル分類](#ファイル分類)
3. [ナビゲーション機構](#ナビゲーション機構)
4. [デザインシステム](#デザインシステム)
5. [編集ワークフロー](#編集ワークフロー)
6. [トラブルシューティング](#トラブルシューティング)

---

## 全体構成

### 本当に必要なメインファイル（7つ）

```
✅ ACTIVE - 本番環境で使用中
├─ index.html              (プロジェクト一覧 / Command Center)
├─ landing.html            (ポータルホーム / ゲートウェイ)
├─ executive_hub.html      (全体課題管理表)
│
└─ Phase 1 (現状評価)
   └─ project_15_14.html   (インフラ環境の可視化と評価)
│
└─ Phase 2 (インフラ刷新) - 4ファイル
   ├─ project_15_01.html   (ADクラウド化)
   ├─ project_15_02.html   (セコム入退室クラウド化)
   ├─ project_15_combined.html (AD+SECOM統合比較)
   └─ project_ad_scenarios.html (AD移行シナリオ比較)
   └─ project_ad_matrix.html (3社権限・責任分界点)
   └─ line_dashboard.html   (SD-WAN Map)
│
└─ Phase 3 (AI推進)
   └─ project_15_12.html   (AIチャンピオン推進)
│
└─ Phase 4 (BuddyNet DX)
   └─ project_bn_report.html (財務自動化レポート)
```

### その他のファイル（整理対象）

```
❓ LEGACY / BACKUP - 削除または整理予定
├─ project_15_02_v20260121_1420.html (複数バージョン)
├─ project_15_02_v20260121_1430.html
├─ project_15_combined_v20260122_1120.html
├─ project_sd_wan_backup.html
├─ project_sd_wan_v1.html
├─ index_old_backup.html
├─ index_new.html
├─ project_15_12_ishii.html (共有用・限定公開)
├─ project_15_12_proposal.html (共有用・限定公開)
├─ project_15_12_antigravity.html (共有用・限定公開)
├─ project_buddynet.html (古い構成)
└─ ... その他多数の試験版
```

---

## ファイル分類

### 1️⃣ メインナビゲーション（2ファイル）

| ファイル | 役割 | 特徴 |
|---------|------|------|
| `index.html` | プロジェクト一覧 | 7つの主要プロジェクトへのゲートウェイ |
| `landing.html` | ポータルホーム | ウェルカムスクリーン＋プロジェクトカード |

**ナビゲーション方式**: `?page=xxx` クエリパラメータベース

```html
<!-- 例1: Phase 1 プロジェクト -->
<a href="?page=project_15_14">
  インフラ評価へ移動
</a>

<!-- 例2: Phase 4 プロジェクト (修正後) -->
<a href="?page=project_bn_report">
  財務自動化レポートへ移動
</a>
```

---

### 2️⃣ メインコンテンツファイル（10ファイル）

#### Phase 1: 現状評価

| ファイル | ページパラメータ | 説明 |
|---------|-----------------|------|
| `project_15_14.html` | `?page=project_15_14` | 現状インフラ環境の可視化と評価 |

**スタイル**: Cyberpunk テーマ（Orbitron フォント、cyan/purple）

---

#### Phase 2: インフラ刷新（6ファイル）

| ファイル | ページパラメータ | 説明 |
|---------|-----------------|------|
| `project_15_01.html` | `?page=project_15_01` | ADクラウド化（IIJ/USEN/LAJ比較） |
| `project_15_02.html` | `?page=project_15_02` | セコム入退室クラウド化（3社比較） |
| `project_15_combined.html` | `?page=project_15_combined` | AD+SECOM統合比較・TCO分析 |
| `project_ad_scenarios.html` | `?page=project_ad_scenarios` | AD移行シナリオ比較（3パターン） |
| `project_ad_matrix.html` | `?page=project_ad_matrix` | 3社の権限・責任分界点比較表 |
| `line_dashboard.html` | `?page=line_dashboard` | SD-WAN vs Vario Secure 比較マップ |

**スタイル**: Unified Design System（Navy/Gray/Red）

---

#### Phase 3: AI推進

| ファイル | ページパラメータ | 説明 |
|---------|-----------------|------|
| `project_15_12.html` | `?page=project_15_12` | AIチャンピオン推進・コミュニティ運営 |

**スタイル**: Unified Design System

---

#### Phase 4: BuddyNet DX

| ファイル | ページパラメータ | 説明 |
|---------|-----------------|------|
| `project_bn_report.html` | `?page=project_bn_report` | PL予実・着地予測の自動化レポート |

**スタイル**: Modern Blue（Montserrat フォント）

---

### 3️⃣ 管理・参考ファイル（5ファイル）

| ファイル | 役割 |
|---------|------|
| `executive_hub.html` | 全体課題管理表 |
| `evaluation_sheet.html` | 人事考課原本（最新版） |
| `daily_log.html` | 活動全史（ログ） |
| `meeting_minutes_20260123.html` | 議事録：1/23調査報告会 |
| `bcp_risk_matrix.html` | BCPリスク評価マトリクス |

---

## ナビゲーション機構

### 統一ナビゲーション方式

**すべてのプロジェクトページ** は `index.html` から `?page=` クエリパラメータで遷移します。

```
index.html
  ├─ ?page=project_15_14  → project_15_14.html
  ├─ ?page=project_15_01  → project_15_01.html
  ├─ ?page=project_15_02  → project_15_02.html
  ├─ ?page=project_15_combined → project_15_combined.html
  ├─ ?page=project_ad_scenarios → project_ad_scenarios.html
  ├─ ?page=project_ad_matrix → project_ad_matrix.html
  ├─ ?page=line_dashboard → line_dashboard.html
  ├─ ?page=project_15_12  → project_15_12.html
  └─ ?page=project_bn_report → project_bn_report.html
```

### 各プロジェクトファイルの「戻るリンク」

各プロジェクトHTMLの上部に "back-link" を配置し、`index.html` に戻す：

```html
<!-- project_15_14.html の例 -->
<a href="index.html" class="back-link">
  &lt; COMMAND CENTER
</a>
```

---

## デザインシステム

### CSS ファイル（2つ）

```
assets/
├─ portal_nexus.css (3.0 KB)
│  └─ 共通レイアウト・サイドバー・基本スタイル
│
└─ unified_design_system.css (15 KB)
   └─ Phase 2-3 プロジェクト用の統一スタイル
       (Navy #1e293b / Gray #64748b / Red #dc2626)
```

### 各プロジェクトの適用状況

| ファイル | portal_nexus | unified_design | 備考 |
|---------|:---:|:---:|------|
| `project_15_14.html` | ✅ | ✅ | Cyberpunk テーマ（独自色） |
| `project_15_01.html` | ✅ | ✅ | ✅ 適用完了 |
| `project_15_02.html` | ✅ | ⏳ | 未適用 |
| `project_15_combined.html` | ✅ | ⏳ | 未適用 |
| `project_ad_scenarios.html` | ✅ | ⏳ | 未適用 |
| `project_ad_matrix.html` | ✅ | ⏳ | 未適用 |
| `line_dashboard.html` | ✅ | ⏳ | 未適用 |
| `project_15_12.html` | ✅ | ⏳ | 未適用 |
| `project_bn_report.html` | ✅ | ⏳ | 未適用 |

### 色彩設計

```css
/* Navy Base */
--color-navy-darkest: #0f172a
--color-navy-dark: #1e293b
--color-navy-light: #334155

/* Gray Neutral */
--color-gray-600: #64748b
--color-gray-300: #cbd5e1

/* Accent */
--color-accent-red: #dc2626
--color-accent-blue: #0284c7

/* Text */
--text-primary: #1e293b
--text-secondary: #64748b
```

---

## 編集ワークフロー

### Step 1: ローカルプレビューの起動

```bash
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"
npx http-server -p 8000 -g
```

ブラウザで開く：
```
http://localhost:8000/?page=project_15_01
```

### Step 2: ファイルの編集

例：`project_15_02.html` を編集する場合

```bash
# ローカルプレビューで確認
http://localhost:8000/?page=project_15_02

# テキストエディタで編集
code project_15_02.html

# ブラウザで F5 リロード → 変更確認
```

### Step 3: デザインシステムの適用

新しいプロジェクトを作成する、または既存ファイルを統一する場合：

```html
<!-- Head セクションに追加 -->
<link rel="stylesheet" href="assets/unified_design_system.css">
<link rel="stylesheet" href="assets/portal_nexus.css">
```

### Step 4: SVG アイコンの標準化

**標準サイズ**: 20px × 20px
**stroke-width**: 2.5

```html
<!-- 正しい例 -->
<svg style="width: 20px; height: 20px;" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="..." />
</svg>
```

### Step 5: 本番デプロイ

```bash
./deploy_auto_v2.sh
```

---

## ファイルクリーンアップ計画

### 削除対象（バージョンファイル）

```
❌ 削除予定
├─ project_15_02_v20260121_1xxx.html (24個のバージョンファイル)
├─ project_15_combined_v20260121_xxxx.html (10個のバージョンファイル)
├─ project_15_combined_v20260122_xxxx.html (2個のバージョンファイル)
├─ project_15_02_backup_*.html (複数)
├─ project_sd_wan_backup.html
├─ project_sd_wan_v1.html
├─ index_old_backup.html
├─ index_new.html
└─ project_15_01_entraid_proposal.html
```

**理由**:
- 最新のメインファイルで置き換え済み
- ディレクトリを圧迫
- 混乱の原因

### 保持対象（共有・限定公開）

```
⚠️ 検討中
├─ project_15_12_ishii.html (石井様向け)
├─ project_15_12_proposal.html (提案書)
├─ project_15_12_antigravity.html (Antigravity案内)
└─ project_buddynet.html (古い BuddyNet ポータル)
```

**判断**: 実際に使用しているか確認してから削除

---

## トラブルシューティング

### 1. ナビゲーションが機能しない

**症状**: リンクをクリックしても別ページに移動しない

**原因**:
- `?page=` パラメータの綴り間違い
- ファイル名と `?page=` の値が一致していない

**解決**:
```html
<!-- ❌ 間違い -->
<a href="?page=project_15_01.html">

<!-- ✅ 正しい -->
<a href="?page=project_15_01">
```

### 2. SVG アイコンが巨大化している

**症状**: ページ内のアイコンが異常に大きく表示される

**原因**:
- SVG に `width` / `height` 属性がない
- Tailwind の `w-4 h-4` などが無視されている

**解決**:
```html
<!-- ❌ 間違い -->
<svg class="w-4 h-4" ...>

<!-- ✅ 正しい -->
<svg style="width: 20px; height: 20px;" ...>
```

### 3. スタイルが適用されない

**症状**: CSS リンクが正しく読み込まれていない

**原因**:
- `href` パスが間違っている
- CSS ファイルが削除されている

**確認**:
```bash
# CSS ファイルの存在確認
ls -l assets/*.css

# ブラウザの開発者ツール (F12) で Network タブを確認
# 404 エラーが出ていないか
```

### 4. ローカルプレビューが更新されない

**症状**: ファイルを編集しても古い内容が表示される

**原因**: ブラウザのキャッシュ

**解決**:
```bash
# Ctrl + Shift + R でハードリロード
# または http-server を再起動
```

---

## 次のステップ（優先度順）

### 🔴 高優先度（今週中に完了）

- [ ] 残り5ファイルに `unified_design_system.css` を適用
  - `project_15_02.html`
  - `project_15_combined.html`
  - `project_ad_scenarios.html`
  - `project_ad_matrix.html`
  - `line_dashboard.html`

- [ ] `project_bn_report.html` の design system 適用

- [ ] 各ページのナビゲーション動作確認（全9ファイル）

### 🟡 中優先度（来週）

- [ ] バージョンファイルの削除（38ファイル）

- [ ] 共有用ファイルの確認・整理
  - `project_15_12_ishii.html`
  - `project_15_12_proposal.html`
  - `project_15_12_antigravity.html`

### 🟢 低優先度（2月中）

- [ ] `project_buddynet.html` の利用状況確認

- [ ] その他ユーティリティファイルの整理

---

## 最後に

このドキュメントは、複雑化したプロジェクトの**完全な全体図**を示しています。

**重要な数字**:
- 🎯 **メインファイル**: 11個（ナビゲーション + コンテンツ + 管理）
- 🔧 **デザインファイル**: 2個（portal_nexus.css + unified_design_system.css）
- 📦 **ページパラメータ**: 9個（`?page=project_15_01` など）
- ❌ **削除対象**: 38個のバージョンファイル

徹底的な整理により、スケーラブルで保守しやすいシステムになります。

---

**最終更新**: 2026-02-07
**管理者**: 丹治統（Toru Tanji）
**バージョン**: 2.0
