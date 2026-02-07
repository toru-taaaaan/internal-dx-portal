# 🎯 完全インベントリ - 全52ファイルの徹底整理

**作成日**: 2026-02-07
**目的**: すべてのHTMLファイルを分類・統計し、意思決定を支援

---

## 📊 統計情報

```
総ファイル数: 52個
├─ 🟢 本番使用中: 11個 (21%)
├─ 🟡 検討中: 6個 (12%)
└─ 🔴 削除予定: 35個 (67%)

サイズ統計:
├─ 全体: 約 2.5 MB
├─ 削除予定: 約 0.8 MB (32%)
└─ クリーンアップ後: 約 1.7 MB
```

---

## 📁 ファイル完全リスト（分類別）

### 🟢 セクション 1: ナビゲーション＆ゲートウェイ（2個）

| # | ファイル | URL | 説明 | 優先度 |
|---|---------|-----|------|--------|
| 1 | `index.html` | なし | プロジェクト一覧・Command Center | 🔴 必須 |
| 2 | `landing.html` | なし | ポータルホーム・ウェルカム | 🔴 必須 |

**ステータス**: ✅ 現役・最新版
**所有格**: portal_nexus.css

---

### 🟢 セクション 2: Phase 1 - 現状評価（1個）

| # | ファイル | URL | 説明 | CSS | 優先度 |
|---|---------|-----|------|-----|--------|
| 3 | `project_15_14.html` | `?page=project_15_14` | インフラ環境の可視化と評価 | custom | 🔴 必須 |

**ステータス**: ✅ 現役・Cyberpunk テーマ
**テーマ**: Orbitron (サイバーパンク), cyan/purple

---

### 🟢 セクション 3: Phase 2 - インフラ刷新（6個）

#### Phase 2-A: ADクラウド化関連

| # | ファイル | URL | 説明 | CSS 状態 | 優先度 |
|---|---------|-----|------|---------|--------|
| 4 | `project_15_01.html` | `?page=project_15_01` | ADクラウド化（IIJ/USEN/LAJ） | ✅ unified | 🔴 必須 |
| 5 | `project_ad_scenarios.html` | `?page=project_ad_scenarios` | AD移行シナリオ比較 | ⏳ 未適用 | 🟠 重要 |
| 6 | `project_ad_matrix.html` | `?page=project_ad_matrix` | 3社権限・責任分界点 | ⏳ 未適用 | 🟠 重要 |

#### Phase 2-B: セコムクラウド化

| # | ファイル | URL | 説明 | CSS 状態 | 優先度 |
|---|---------|-----|------|---------|--------|
| 7 | `project_15_02.html` | `?page=project_15_02` | セコム入退室クラウド化 | ⏳ 未適用 | 🔴 必須 |
| 8 | `project_15_combined.html` | `?page=project_15_combined` | AD+SECOM統合比較 | ⏳ 未適用 | 🟠 重要 |

#### Phase 2-C: ネットワーク関連

| # | ファイル | URL | 説明 | CSS 状態 | 優先度 |
|---|---------|-----|------|---------|--------|
| 9 | `line_dashboard.html` | `?page=line_dashboard` | SD-WAN Map | ⏳ 未適用 | 🟠 重要 |

**ステータス**: ✅ すべて現役
**CSS 状態**: 1/6 統一完了 (17%)

---

### 🟢 セクション 4: Phase 3 - AI推進（1個）

| # | ファイル | URL | 説明 | CSS | 優先度 |
|---|---------|-----|------|-----|--------|
| 10 | `project_15_12.html` | `?page=project_15_12` | AIチャンピオン推進 | ⏳ 未適用 | 🟠 重要 |

**ステータス**: ✅ 現役

---

### 🟢 セクション 5: Phase 4 - BuddyNet DX（1個）

| # | ファイル | URL | 説明 | CSS | 優先度 |
|---|---------|-----|------|-----|--------|
| 11 | `project_bn_report.html` | `?page=project_bn_report` | PL予実・着地予測自動化 | custom | 🟠 重要 |

**ステータス**: ✅ 現役
**テーマ**: Blue (Montserrat)

---

### 🟢 セクション 6: 管理・参考ページ（5個）

| # | ファイル | URL | 説明 | CSS | 優先度 |
|---|---------|-----|------|-----|--------|
| - | `executive_hub.html` | `?page=executive_hub` | 全体課題管理表 | portal | ✅ |
| - | `bcp_risk_matrix.html` | `?page=bcp_risk_matrix` | BCPリスク評価 | portal | ✅ |
| - | `evaluation_sheet.html` | `?page=evaluation_sheet` | 人事考課原本 | portal | ✅ |
| - | `daily_log.html` | `?page=daily_log` | 活動全史（ログ） | portal | ✅ |
| - | `meeting_minutes_20260123.html` | `?page=meeting_minutes_20260123` | 議事録: 1/23 | portal | ✅ |

**ステータス**: ✅ すべて現役

---

### 🟡 セクション 7: 検討中（6個）

| # | ファイル | 説明 | 判定内容 | 推奨 |
|---|---------|------|--------|--------|
| A | `project_15_03.html` | ネットワークインフラ刷新？ | index.html でリンクされているか | 要確認 |
| B | `project_15_01_entraid_proposal.html` | Entra ID 提案書 | 参考資料として保持するか | 削除推奨 |
| C | `project_15_12_ishii.html` | 石井様向け相談資料 | 個別配布終了したか | 削除推奨 |
| D | `project_15_12_proposal.html` | AquaVoice提案書 | 最新構成で必要か | 削除推奨 |
| E | `project_15_12_antigravity.html` | Antigravity導入案内 | 最新構成で必要か | 削除推奨 |
| F | `project_buddynet.html` | 古い BuddyNet ポータル | project_bn_report 新版か | 削除推奨 |

**判定**: 各自利用状況を確認後、削除判定

---

### 🔴 セクション 8: 削除予定（35個）

#### Group 1: project_15_02 バージョンファイル（21個）

```
削除対象:
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
project_15_02_v20260121_1550.html
project_15_02_v20260121_1600.html
project_15_02_v20260121_1630.html
project_15_02_v20260121_1640.html
project_15_02_backup_20260121_123604.html
project_15_02_backup_downtime_20260121_125351.html
project_15_02_backup_subtitle_20260121_125137.html
project_15_02_before_latest_update_20260121_123842.html
project_15_02_before_merge_20260121_124220.html

理由: 最新版 project_15_02.html に統合済み
```

#### Group 2: project_15_combined バージョンファイル（12個）

```
削除対象:
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

理由: 最新版 project_15_combined.html に統合済み
```

#### Group 3: ナビゲーション・インデックス（3個）

```
削除対象:
index_old_backup.html
index_new.html
index_hub.html

理由: 最新版 index.html に置換済み
```

#### Group 4: SD-WAN 関連（2個）

```
削除対象:
project_sd_wan_backup.html
project_sd_wan_v1.html

理由: 最新版は line_dashboard.html / project_sd_wan.html
```

#### Group 5: その他ユーティリティ（7個）

```
削除対象:
_generated_css.html (自動生成)
AccessDenied.html (エラーページ未使用)
action_dashboard.html (古いダッシュボード)
infrastructure_strategy.html (旧構成)
landing_new_concept.html (試験版)
project.html (古い一覧)
project_management.html (古い管理ツール)

理由: 新構成に置換済み、または未使用
```

**ステータス**: 削除承認待機

---

## 🔄 推奨されたアクション

### 今すぐ実行（本日）

```
✅ 完了
├─ Phase 4 リンク修正（index.html）
├─ システムアーキテクチャドキュメント作成
├─ ファイルマトリクス作成
└─ チェックリスト作成

⏳ 承認待機
└─ バージョンファイル削除（27個）
```

### 今週中に実行

```
🔴 必須
├─ unified_design_system.css を5ファイルに適用
│  ├─ project_15_02.html
│  ├─ project_15_combined.html
│  ├─ project_ad_scenarios.html
│  ├─ project_ad_matrix.html
│  └─ line_dashboard.html
│
└─ SVG アイコン標準化（全9ファイル）
   └─ 20px × 20px, stroke-width 2.5
```

### 来週中に実行

```
🟡 重要
├─ project_15_14 / project_bn_report テーマ判定
├─ 検討中ファイル（6個）の利用状況確認
├─ Phase 2 削除実行
└─ ローカルプレビュー全検証
```

---

## 💾 ファイルサイズ詳細

```
現在の構成:
├─ メインファイル（11個）: 約 1.7 MB
├─ バージョンファイル（27個）: 約 0.6 MB
├─ その他（14個）: 約 0.2 MB
└─ 合計: 約 2.5 MB

クリーンアップ後:
├─ メインファイル（11個）: 約 1.7 MB
├─ 検討中（6個）: 約 0.15 MB （削除予定）
└─ 合計: 約 1.85 MB

削減量: 約 0.65 MB (26% 削減)
```

---

## 🎯 最終目標状態

```
理想的なファイル構成:

社内DXポータル/
├─ 📚 Documentation/ (6個の MD)
├─ 🌐 Navigation/ (2個)
│  ├─ index.html
│  └─ landing.html
├─ 📊 Projects/ (9個)
│  ├─ Phase1/ (1個)
│  ├─ Phase2/ (6個)
│  ├─ Phase3/ (1個)
│  └─ Phase4/ (1個)
├─ 🔧 Admin/ (5個)
│  ├─ executive_hub.html
│  ├─ bcp_risk_matrix.html
│  ├─ evaluation_sheet.html
│  ├─ daily_log.html
│  └─ meeting_minutes_20260123.html
├─ 🎨 Assets/
│  ├─ portal_nexus.css
│  └─ unified_design_system.css
└─ 🔧 Scripts/
   └─ deploy_auto_v2.sh

合計: 約 30ファイル（現在の58%）
```

---

## ✅ 確認項目

実行前に以下を確認してください：

```
[ ] 本ドキュメントをすべて読んだ
[ ] バックアップを取得した
[ ] ローカルプレビューが正常に動作している
[ ] すべてのナビゲーションリンクが `?page=` で統一されていることを確認した
[ ] デプロイスクリプトが認証済みである
[ ] 各ファイルの利用状況を確認した（必要に応じて）
[ ] 削除対象ファイルが完全な重複であることを確認した
```

---

## 📞 質問と回答

### Q1: なぜこんなにバージョンファイルが多いのか？

**A**: 編集過程で各編集毎に新しいバージョンを保存していた。現在は最新版のみが必要。

### Q2: project_15_03.html は何か？

**A**: ネットワークインフラ刷新プロジェクト。現在 index.html でリンクされていないので、不要かもしれない。要確認。

### Q3: Cyberpunk テーマ（project_15_14）を変更すべきか？

**A**: 独特な設計として保持するか、統一デザインに変更するかは丹治さんの判断次第。

### Q4:削除後に復元できるか？

**A**: はい。Git で管理されていれば過去のコミットから復元可能。またはバックアップから復元可能。

---

**所有者**: 丹治統（Toru Tanji）
**状態**: 準備完了・承認待機
**最終更新**: 2026-02-07
**バージョン**: 1.0
