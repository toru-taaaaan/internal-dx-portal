# 📋 ファイルクリーンアップ計画

**作成日**: 2026-02-07
**対象**: バージョンファイルと重複ファイルの整理

---

## 概要

現在、ディレクトリには**52個のHTMLファイル**が存在しますが、実際には**11個のメインファイル**のみが必要です。

残り41個は、バージョン管理ファイル、バックアップ、提案書などです。

---

## 削除対象ファイル（完全リスト）

### グループ 1: project_15_02 バージョンファイル（16個）

```
❌ 削除対象
project_15_02_v20260121_1321.html
project_15_02_v20260121_1333.html
project_15_02_v20260121_1337.html
project_15_02_v20260121_1339.html
project_15_02_v20260121_1345.html
project_15_02_v20260121_1350.html
project_15_02_v20260121_1355.html
project_15_02_v20260121_1400.html
project_15_02_v20260121_1410.html
project_15_02_v20260121_1420.html
project_15_02_v20260121_1430.html
project_15_02_v20260121_1440.html
project_15_02_v20260121_1510.html
project_15_02_v20260121_1530.html
project_15_02_v20260121_1540.html
project_15_02_v20260121_1545.html

✅ 保持対象
project_15_02.html (最新版・本番使用)
```

### グループ 2: project_15_02 バックアップ（5個）

```
❌ 削除対象
project_15_02_backup_20260121_123604.html
project_15_02_backup_downtime_20260121_125351.html
project_15_02_backup_subtitle_20260121_125137.html
project_15_02_before_latest_update_20260121_123842.html
project_15_02_before_merge_20260121_124220.html

✅ 保持対象
project_15_02.html (最新版・本番使用)
```

### グループ 3: project_15_combined バージョンファイル（11個）

```
❌ 削除対象
project_15_combined_v20260121_1500.html
project_15_combined_v20260121_1510.html
project_15_combined_v20260121_1520.html
project_15_combined_v20260121_1530.html
project_15_combined_v20260121_1535.html
project_15_combined_v20260121_1540.html
project_15_combined_v20260121_1550.html
project_15_combined_v20260121_1600.html
project_15_combined_v20260121_1605.html
project_15_combined_v20260121_1615.html
project_15_combined_v20260122_1105.html
project_15_combined_v20260122_1120.html

✅ 保持対象
project_15_combined.html (最新版・本番使用)
```

### グループ 4: インデックスページバージョン（3個）

```
❌ 削除対象
index_old_backup.html (古いバックアップ)
index_new.html (試験版)
index_hub.html (重複？)

✅ 保持対象
index.html (本番使用)
```

### グループ 5: SD-WAN バージョン（2個）

```
❌ 削除対象
project_sd_wan_backup.html (バックアップ)
project_sd_wan_v1.html (バージョン1)

✅ 保持対象
project_sd_wan.html (本番使用)
line_dashboard.html (公式名)
```

### グループ 6: プロジェクト 15 その他（4個）

```
❌ 検討中 (確認必要)
project_15_03.html (ネットワークインフラ刷新？)
project_15_01_entraid_proposal.html (Entra ID 提案？)

❌ 削除対象
project_15_12_ishii.html (石井様向け・共有終了か確認)
project_15_12_proposal.html (提案書・現在の構成に不要か)
project_15_12_antigravity.html (Antigravity案内・最新版？)
project_buddynet.html (古い BuddyNet ポータル)
```

### グループ 7: その他ユーティリティ（複数）

```
❌ 削除対象
_generated_css.html (自動生成ファイル)
AccessDenied.html (エラーページ)
action_dashboard.html (古いダッシュボード)
infrastructure_strategy.html (まだ使用中？)
landing_new_concept.html (試験版 landing)
project.html (古いプロジェクト一覧)
project_management.html (古い管理ツール)

✅ 保持対象
landing.html (本番使用)
executive_hub.html (全体課題管理表)
bcp_risk_matrix.html (BCP評価)
evaluation_sheet.html (人事考課)
daily_log.html (活動ログ)
meeting_minutes_20260123.html (議事録)
```

---

## 統計

```
現在のファイル数: 52個（HTML）
削除対象: 41個
保持対象: 11個

削除内訳:
├─ バージョンファイル: 27個
├─ バックアップファイル: 5個
├─ 重複・古いファイル: 6個
└─ 検討中（確認必要）: 3個
```

---

## クリーンアップの実行方法

### Phase 1: 安全な削除（完全に重複なファイル）

```bash
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"

# project_15_02 のバージョンファイルを削除
rm -f project_15_02_v20260121_*.html
rm -f project_15_02_backup_*.html
rm -f project_15_02_before_*.html

# project_15_combined のバージョンファイルを削除
rm -f project_15_combined_v20260121_*.html
rm -f project_15_combined_v20260122_*.html

# SD-WAN バージョンファイルを削除
rm -f project_sd_wan_backup.html
rm -f project_sd_wan_v1.html

# インデックスバックアップを削除
rm -f index_old_backup.html
rm -f index_new.html
rm -f index_hub.html

# その他
rm -f _generated_css.html
rm -f AccessDenied.html
rm -f action_dashboard.html
rm -f project.html
rm -f project_management.html
rm -f landing_new_concept.html
```

### Phase 2: 条件付き削除（要確認）

```bash
# 削除前に確認が必要なファイル:

# 1. project_15_03.html - 使用中か確認
#    index.html でリンクされているか確認

# 2. project_15_01_entraid_proposal.html - 提案書として必要か確認
#    project_15_01.html で参照されているか確認

# 3. project_15_12_ishii.html - 石井様に配布中か確認

# 4. project_15_12_proposal.html - 現在の構成で必要か確認

# 5. project_15_12_antigravity.html - まだ使用しているか確認

# 6. project_buddynet.html - 古い BuddyNet ポータルか確認
#    project_bn_report.html が新版か確認
```

---

## 推奨スケジュール

```
🔴 今週（2/7-2/8）
└─ Phase 1 の安全な削除を実行（27個のバージョンファイル）

🟡 来週（2/10-2/14）
└─ Phase 2 で要確認ファイルの利用状況を確認・判断

🟢 2月中に完了
└─ 最終確認後、整理完了
```

---

## クリーンアップ後のディレクトリ構造（理想形）

```
社内DXポータル/
├─ 📚 ドキュメント
│  ├─ 🔧_SYSTEM_ARCHITECTURE_v2.md (このドキュメント)
│  ├─ 📋_CLEANUP_PLAN.md (このファイル)
│  ├─ 📌_START_HERE.md
│  ├─ 🎯_COMPREHENSIVE_PROJECT_ANALYSIS.md
│  ├─ 00_RESOURCE_INDEX.md
│  ├─ ✅_ENVIRONMENT_SETUP_CHECKLIST.md
│  ├─ SITEMAP.md
│  └─ ... その他 MD ファイル
│
├─ 🌐 メインナビゲーション
│  ├─ index.html (プロジェクト一覧)
│  └─ landing.html (ポータルホーム)
│
├─ 📊 コンテンツ
│  ├─ Phase 1/
│  │  └─ project_15_14.html
│  │
│  ├─ Phase 2/
│  │  ├─ project_15_01.html
│  │  ├─ project_15_02.html
│  │  ├─ project_15_combined.html
│  │  ├─ project_ad_scenarios.html
│  │  ├─ project_ad_matrix.html
│  │  └─ line_dashboard.html
│  │
│  ├─ Phase 3/
│  │  └─ project_15_12.html
│  │
│  ├─ Phase 4/
│  │  └─ project_bn_report.html
│  │
│  └─ 管理ページ/
│     ├─ executive_hub.html
│     ├─ bcp_risk_matrix.html
│     ├─ evaluation_sheet.html
│     ├─ daily_log.html
│     └─ meeting_minutes_20260123.html
│
├─ 🎨 スタイル
│  └─ assets/
│     ├─ portal_nexus.css
│     └─ unified_design_system.css
│
└─ 🔧 ユーティリティ
   ├─ deploy_auto_v2.sh
   ├─ deploy_auto_v2.sh.log
   └─ ... その他スクリプト
```

---

**状態**: 準備完了
**次のステップ**: Bravo の承認後、Phase 1 削除を実行
