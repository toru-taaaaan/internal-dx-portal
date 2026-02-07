# ✅ 組織化チェックリスト - 完全整理計画

**作成日**: 2026-02-07
**目的**: System Architecture の完全な整理・統一を段階的に実行

---

## 📋 実行計画チェックリスト

### Phase A: ドキュメント整備（✅ 完了）

- [x] システムアーキテクチャドキュメント作成（🔧_SYSTEM_ARCHITECTURE_v2.md）
- [x] クリーンアップ計画書作成（📋_CLEANUP_PLAN.md）
- [x] ファイル状態マトリクス作成（📑_FILE_STATUS_MATRIX.md）
- [x] このチェックリスト作成（✅_ORGANIZATION_CHECKLIST.md）

**状態**: ✅ 完了

---

### Phase B: ナビゲーション修正（✅ 完了）

#### B-1: Phase 4 リンク修正

- [x] index.html の Phase 4 リンク修正
  - 変更前: `href="project_bn_report.html"`
  - 変更後: `href="?page=project_bn_report"`
  - ファイル: index.html (line 216)

- [x] すべてのナビゲーションリンクが `?page=` 統一パターンになっていることを確認

**状態**: ✅ 完了

---

### Phase C: デザインシステム適用（⏳ 進行中）

#### C-1: unified_design_system.css の確認

- [x] unified_design_system.css が assets フォルダに存在
- [x] CSS ファイルサイズ確認（15 KB）
- [x] CSS 内の CSS 変数定義確認
  - `--color-navy-darkest: #0f172a`
  - `--color-navy-dark: #1e293b`
  - `--color-accent-red: #dc2626`
  - その他

**状態**: ✅ 確認完了

#### C-2: すでに適用されているファイル（1個）

- [x] project_15_01.html
  - `<link rel="stylesheet" href="assets/unified_design_system.css">` 確認
  - SVG アイコンサイズ確認（20px）

**状態**: ✅ 確認完了

#### C-3: 適用予定ファイル（5個）

- [ ] **project_15_02.html** (セコム入退室クラウド化)
  - [ ] `<link rel="stylesheet" href="assets/unified_design_system.css">` を `<head>` に追加
  - [ ] SVG アイコンサイズを 20px に統一
  - [ ] ローカルプレビューで確認
  - [ ] デプロイ

- [ ] **project_15_combined.html** (AD+SECOM統合比較)
  - [ ] CSS リンク追加
  - [ ] SVG 標準化
  - [ ] ローカルプレビューで確認
  - [ ] デプロイ

- [ ] **project_ad_scenarios.html** (AD移行シナリオ)
  - [ ] CSS リンク追加
  - [ ] SVG 標準化
  - [ ] ローカルプレビューで確認
  - [ ] デプロイ

- [ ] **project_ad_matrix.html** (3社責任分界)
  - [ ] CSS リンク追加
  - [ ] SVG 標準化
  - [ ] ローカルプレビューで確認
  - [ ] デプロイ

- [ ] **line_dashboard.html** (SD-WAN Map)
  - [ ] CSS リンク追加
  - [ ] SVG 標準化
  - [ ] ローカルプレビューで確認
  - [ ] デプロイ

**状態**: ⏳ 未開始

#### C-4: 特別判定が必要なファイル（2個）

- [ ] **project_15_14.html** (Cyberpunk テーマ)
  - **判定**: Cyberpunk テーマ (Orbitron font, cyan/purple) を保持するか、unified_design に統一するか？
  - [ ] Cyberpunk テーマを保持する場合：そのまま
  - [ ] 統一する場合：CSS リンク追加・色変更

- [ ] **project_bn_report.html** (BuddyNet 財務)
  - **判定**: 現在のブルー・Montserrat テーマを保持するか、unified_design に統一するか？
  - [ ] 現テーマを保持する場合：そのまま
  - [ ] 統一する場合：CSS リンク追加・色変更

**状態**: ⏳ 判定待機

---

### Phase D: SVG アイコン標準化（⏳ 進行中）

#### D-1: すべてのプロジェクトファイルで SVG アイコンを検証

基準:
- **サイズ**: `style="width: 20px; height: 20px;"`
- **stroke-width**: `stroke-width="2.5"`

ファイルリスト:

- [ ] `index.html` ✅ 既修正
- [ ] `project_15_01.html` (確認)
- [ ] `project_15_02.html`
- [ ] `project_15_combined.html`
- [ ] `project_ad_scenarios.html`
- [ ] `project_ad_matrix.html`
- [ ] `line_dashboard.html`
- [ ] `project_15_12.html`
- [ ] `project_bn_report.html`
- [ ] `project_15_14.html` ✅ 既修正

**状態**: ⏳ 確認中

---

### Phase E: ファイルクリーンアップ（⏳ 未開始）

#### E-1: Phase 1 - 安全な削除（27個）

確認: すべてのバージョンファイルが最新版に統合されていることを確認

- [ ] `project_15_02_v20260121_*.html` (16個)
- [ ] `project_15_02_backup_*.html` (5個)
- [ ] `project_15_02_before_*.html` (複数)
- [ ] `project_15_combined_v20260121_*.html` (11個)
- [ ] `project_15_combined_v20260122_*.html` (2個)
- [ ] `project_sd_wan_backup.html`
- [ ] `project_sd_wan_v1.html`
- [ ] `index_old_backup.html`
- [ ] `index_new.html`
- [ ] `index_hub.html`
- [ ] その他ユーティリティ（7個）

実行コマンド:
```bash
# バージョンファイル削除
rm -f project_15_02_v20260121_*.html
rm -f project_15_02_backup_*.html
rm -f project_15_02_before_*.html
rm -f project_15_combined_v20260121_*.html
rm -f project_15_combined_v20260122_*.html
rm -f project_sd_wan_backup.html
rm -f project_sd_wan_v1.html
rm -f index_old_backup.html
rm -f index_new.html
rm -f index_hub.html
rm -f _generated_css.html
rm -f AccessDenied.html
rm -f action_dashboard.html
rm -f project.html
rm -f project_management.html
rm -f landing_new_concept.html
rm -f infrastructure_strategy.html
```

**状態**: ⏳ 承認待機

#### E-2: Phase 2 - 条件付き削除（6個）

確認が必要なファイル:

- [ ] `project_15_03.html` - index.html でリンクされているか確認
- [ ] `project_15_01_entraid_proposal.html` - 参考資料として必要か確認
- [ ] `project_15_12_ishii.html` - 石井様に配布中か確認
- [ ] `project_15_12_proposal.html` - 最新構成で必要か確認
- [ ] `project_15_12_antigravity.html` - 使用中か確認
- [ ] `project_buddynet.html` - project_bn_report が新版か確認

**状態**: ⏳ 確認待機

---

### Phase F: 最終検証（⏳ 未開始）

#### F-1: ローカルプレビュー検証

```bash
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"
npx http-server -p 8000 -g
```

ナビゲーション検証:

- [ ] http://localhost:8000 で index.html が読み込まれる
- [ ] http://localhost:8000/?page=project_15_01 で各ページが遷移
- [ ] すべてのプロジェクトリンクが動作する
- [ ] back-link で index.html に戻る

#### F-2: 本番環境デプロイ前の確認

- [ ] すべての CSS リンクが正しい
- [ ] すべてのナビゲーションが `?page=` パターンで統一
- [ ] SVG アイコンが 20px で標準化
- [ ] デザイン統一性が確認できる

**状態**: ⏳ 未開始

---

## 📊 進捗サマリー

```
Phase A: ドキュメント整備 ████████████ 100% ✅
Phase B: ナビゲーション修正 ████████████ 100% ✅
Phase C: デザインシステム適用 ██░░░░░░░░░ 16% ⏳
Phase D: SVG標準化 ██░░░░░░░░░ 20% ⏳
Phase E: ファイルクリーンアップ ░░░░░░░░░░░ 0% ⏳
Phase F: 最終検証 ░░░░░░░░░░░ 0% ⏳

全体進捗: ███░░░░░░░░░░░░░░░░░░ 21%
```

---

## 🎯 実行スケジュール（推奨）

### 🔴 今週（2月7-8日）

**优先度: 高**

```
[ ] Phase C-3: unified_design_system.css を5ファイルに適用
    project_15_02.html
    project_15_combined.html
    project_ad_scenarios.html
    project_ad_matrix.html
    line_dashboard.html

    所要時間: 各5分 × 5 = 25分

[ ] Phase D-1: SVG アイコン検証
    所要時間: 各3分 × 9ファイル = 27分

[ ] Phase E-1: Phase 1 クリーンアップ実行
    所要時間: 5分
    結果: 27個のバージョンファイル削除
```

**小計**: 約1時間

### 🟡 来週（2月10-14日）

**优先度: 中**

```
[ ] Phase C-4: 特別判定ファイルの判定
    project_15_14.html
    project_bn_report.html

[ ] Phase D: 必要に応じてアイコン修正

[ ] Phase E-2: 条件付きファイル確認・削除

[ ] Phase F-1: ローカルプレビュー検証
```

**小計**: 約2時間

### 🟢 2月中（2月17-28日）

**优先度: 低**

```
[ ] Phase F-2: 本番環境デプロイ前確認

[ ] 最終クリーンアップ確認
```

---

## 💾 バックアップ手順

削除前に、念のため全ファイルのバックアップを取ることをお勧めします：

```bash
# バックアップの作成
zip -r "社内DXポータル_backup_2026-02-07.zip" . \
  -x "node_modules/*" ".npm-cache/*" ".git/*"

# 別フォルダに保存
mkdir -p "C:\Backup"
cp "社内DXポータル_backup_2026-02-07.zip" "C:\Backup\"
```

---

## ✅ 最終確認リスト

実行前に必ず確認してください：

- [ ] バックアップが取得されている
- [ ] ローカルプレビューが正常に動作している
- [ ] すべてのメインファイル（11個）が index.html から遷移可能
- [ ] 本番環境にデプロイする権限がある
- [ ] デプロイスクリプト（deploy_auto_v2.sh）が正常に動作している

---

## 🚀 実行開始の合図

下記の確認をしてから、実行を開始してください：

```
1. ドキュメントを読んで理解した ← ここで確認
2. バックアップを取得した ← ここで確認
3. ローカルプレビューが動作している ← ここで確認
4. デプロイスクリプトが認証済み ← ここで確認

すべてOKなら、以下を実行：
```bash
# Bravo に以下を指示
"Phase C-3 の CSS 適用を開始してください"
```

---

**ステータス**: 準備完了・承認待機
**所有者**: 丹治統（Toru Tanji）
**最終更新**: 2026-02-07
