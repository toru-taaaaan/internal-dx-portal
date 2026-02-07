# 📑 ファイル状態マトリクス - 完全ステータス表

**作成日**: 2026-02-07
**更新日**: 2026-02-07
**目的**: 全52個のHTMLファイルの状態を可視化

---

## エグゼクティブサマリー

```
📊 ファイル統計
├─ 🟢 本番使用中（Active）: 11個
├─ 🟡 検討中（待機中）: 6個
├─ 🔴 削除予定（Legacy）: 35個
└─ 合計: 52個
```

---

## ファイル状態マトリクス

### 🟢 本番使用中（11個）

#### ナビゲーション / エントリーポイント（2個）

| # | ファイル名 | URL パラメータ | 説明 | CSS | 状態 |
|---|----------|-----------------|------|-----|------|
| 1 | `index.html` | なし | プロジェクト一覧・Command Center | portal_nexus | ✅ 現役 |
| 2 | `landing.html` | なし | ポータルホーム・ウェルカムスクリーン | portal_nexus | ✅ 現役 |

#### Phase 1: 現状評価（1個）

| # | ファイル名 | URL パラメータ | 説明 | CSS | 状態 |
|---|----------|-----------------|------|-----|------|
| 3 | `project_15_14.html` | `?page=project_15_14` | インフラ環境の可視化と評価 | unified_design + custom | ✅ 現役 |

#### Phase 2: インフラ刷新（6個）

| # | ファイル名 | URL パラメータ | 説明 | CSS | 状態 |
|---|----------|-----------------|------|-----|------|
| 4 | `project_15_01.html` | `?page=project_15_01` | ADクラウド化比較（IIJ/USEN/LAJ） | unified_design | ✅ 現役・更新完了 |
| 5 | `project_15_02.html` | `?page=project_15_02` | セコム入退室クラウド化（3社比較） | portal_nexus | ⚠️ unified_design 未適用 |
| 6 | `project_15_combined.html` | `?page=project_15_combined` | AD+SECOM統合比較・TCO分析 | portal_nexus | ⚠️ unified_design 未適用 |
| 7 | `project_ad_scenarios.html` | `?page=project_ad_scenarios` | AD移行シナリオ比較（3パターン） | portal_nexus | ⚠️ unified_design 未適用 |
| 8 | `project_ad_matrix.html` | `?page=project_ad_matrix` | 3社の権限・責任分界点比較表 | portal_nexus | ⚠️ unified_design 未適用 |
| 9 | `line_dashboard.html` | `?page=line_dashboard` | SD-WAN vs Vario Secure 比較 | portal_nexus | ⚠️ unified_design 未適用 |

#### Phase 3: AI推進（1個）

| # | ファイル名 | URL パラメータ | 説明 | CSS | 状態 |
|---|----------|-----------------|------|-----|------|
| 10 | `project_15_12.html` | `?page=project_15_12` | AIチャンピオン推進・コミュニティ | portal_nexus | ⚠️ unified_design 未適用 |

#### Phase 4: BuddyNet DX（1個）

| # | ファイル名 | URL パラメータ | 説明 | CSS | 状態 |
|---|----------|-----------------|------|-----|------|
| 11 | `project_bn_report.html` | `?page=project_bn_report` | PL予実・着地予測の自動化レポート | custom (Montserrat) | ⚠️ 要スタイル確認 |

#### 管理・参考ファイル（サイドバー経由）

| # | ファイル名 | URL パラメータ | 説明 | CSS | 状態 |
|---|----------|-----------------|------|-----|------|
| - | `executive_hub.html` | `?page=executive_hub` | 全体課題管理表 | portal_nexus | ✅ 現役 |
| - | `bcp_risk_matrix.html` | `?page=bcp_risk_matrix` | BCPリスク評価マトリクス | portal_nexus | ✅ 現役 |
| - | `evaluation_sheet.html` | `?page=evaluation_sheet` | 人事考課原本 | portal_nexus | ✅ 現役 |
| - | `daily_log.html` | `?page=daily_log` | 活動全史（ログ） | portal_nexus | ✅ 現役 |
| - | `meeting_minutes_20260123.html` | `?page=meeting_minutes_20260123` | 議事録：1/23調査報告会 | portal_nexus | ✅ 現役 |

---

### 🟡 検討中・待機中（6個）

| # | ファイル名 | 説明 | 判定必要 | 備考 |
|---|----------|------|---------|------|
| 1 | `project_15_03.html` | ネットワークインフラ刷新？ | index.html でリンクされているか | 本番で使用中か確認 |
| 2 | `project_15_01_entraid_proposal.html` | Entra ID 提案書 | project_15_01 の参考資料か | 古い提案か確認 |
| 3 | `project_15_12_ishii.html` | 石井様向け相談資料 | 共有を終了したか | 個別配布か確認 |
| 4 | `project_15_12_proposal.html` | AquaVoice提案書 | 最新構成で必要か | 古い提案か確認 |
| 5 | `project_15_12_antigravity.html` | Antigravity導入案内 | 最新構成で必要か | 古い提案か確認 |
| 6 | `project_buddynet.html` | 古い BuddyNet ポータル | project_bn_report が新版か | 置換済みか確認 |

---

### 🔴 削除対象（35個）

#### project_15_02 バージョンファイル（21個）

```
❌ 削除予定
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
project_15_02_v20260121_1550.html (2026-01-21 編集）
project_15_02_v20260121_1600.html
project_15_02_v20260121_1630.html
project_15_02_v20260121_1640.html
project_15_02_backup_*.html (5個)
```

**削除理由**: 最新版は `project_15_02.html`

#### project_15_combined バージョンファイル（12個）

```
❌ 削除予定
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
```

**削除理由**: 最新版は `project_15_combined.html`

#### インデックス・ナビゲーション（3個）

```
❌ 削除予定
index_old_backup.html (古いバックアップ)
index_new.html (試験版)
index_hub.html (重複?)
```

**削除理由**: 最新版は `index.html`

#### その他ユーティリティ（7個）

```
❌ 削除予定
_generated_css.html (自動生成・不要)
AccessDenied.html (エラーページ・未使用)
action_dashboard.html (古いダッシュボード)
infrastructure_strategy.html (旧構成・未使用)
landing_new_concept.html (試験版 landing)
project.html (古い一覧ページ)
project_management.html (古い管理ツール)
```

**削除理由**: 新しい構成に置換済みまたは未使用

#### SD-WAN 関連（2個）

```
❌ 削除予定
project_sd_wan_backup.html (バックアップ)
project_sd_wan_v1.html (バージョン1)
```

**削除理由**: 最新版は `line_dashboard.html` または `project_sd_wan.html`

---

## デザインシステム適用状況

### CSS ファイル一覧

```
assets/
├─ portal_nexus.css (3.0 KB)
│  └─ 共通レイアウト・サイドバー・基本スタイル
│     ✅ 全ファイルで使用
│
└─ unified_design_system.css (15 KB)
   └─ Navy/Gray/Red 統一デザイン
      ✅ project_15_01.html
      ⏳ project_15_02.html (未適用)
      ⏳ project_15_combined.html (未適用)
      ⏳ project_ad_scenarios.html (未適用)
      ⏳ project_ad_matrix.html (未適用)
      ⏳ line_dashboard.html (未適用)
      ⏳ project_15_12.html (未適用)
      ⚠️ project_bn_report.html (独自スタイル・要検討)
      🔵 project_15_14.html (Cyberpunk テーマ・要検討)
```

---

## ナビゲーション検証

### index.html から遷移可能なページ（9個）

```
✅ Phase 1
├─ ?page=project_15_14 → project_15_14.html ✓ OK

✅ Phase 2 (更新 2026-02-07)
├─ ?page=project_15_01 → project_15_01.html ✓ OK (修正: href="?page=project_15_01")
├─ ?page=project_15_02 → project_15_02.html ✓ OK
├─ ?page=project_15_combined → project_15_combined.html ✓ OK
├─ ?page=project_ad_scenarios → project_ad_scenarios.html ✓ OK
├─ ?page=project_ad_matrix → project_ad_matrix.html ✓ OK
└─ ?page=line_dashboard → line_dashboard.html ✓ OK

✅ Phase 3
├─ ?page=project_15_12 → project_15_12.html ✓ OK

✅ Phase 4 (修正 2026-02-07)
└─ ?page=project_bn_report → project_bn_report.html ✓ OK (修正: href="?page=project_bn_report")
```

### サイドバーから遷移可能なページ（5個）

```
✅ Top Navigation
├─ ?page=landing → landing.html ✓ OK
└─ ?page=index → index.html ✓ OK

✅ Core Management
├─ ?page=executive_hub → executive_hub.html ✓ OK
└─ ?page=evaluation_sheet → evaluation_sheet.html ✓ OK

✅ Logs & History
└─ ?page=daily_log → daily_log.html ✓ OK
```

---

## 実装ステータス

### CSS 統一化（unified_design_system.css の適用）

```
進捗: 1/8 完了 (12.5%)

✅ 完了
├─ project_15_01.html

⏳ 予定中（優先度順）
├─ project_15_02.html (セコム)
├─ project_15_combined.html (統合比較)
├─ project_ad_scenarios.html (シナリオ)
├─ project_ad_matrix.html (責任分界)
├─ line_dashboard.html (SD-WAN)
└─ project_15_12.html (AI)

⚠️ 要判定
├─ project_bn_report.html (独自スタイルを保持するか)
└─ project_15_14.html (Cyberpunk テーマを保持するか)
```

### SVG アイコン標準化

```
✅ 完了したファイル
├─ index.html (20px × 20px, stroke-width 2.5)
├─ project_15_14.html (back-link 修正)

⏳ 確認が必要なファイル
├─ project_15_01.html
├─ project_15_02.html
├─ project_15_combined.html
├─ project_ad_scenarios.html
├─ project_ad_matrix.html
├─ line_dashboard.html
├─ project_15_12.html
└─ project_bn_report.html
```

---

## 次のステップ（優先度別）

### 🔴 今週中に完了（2/7-2/8）

- [ ] 削除対象（35個）の削除を実行
  - Phase 1: 安全な削除（27個）を実行

- [ ] unified_design_system.css を5ファイルに適用
  - project_15_02.html
  - project_15_combined.html
  - project_ad_scenarios.html
  - project_ad_matrix.html
  - line_dashboard.html

### 🟡 来週中に完了（2/10-2/14）

- [ ] project_15_12.html を unified_design で統一
- [ ] project_bn_report.html のスタイル検討
- [ ] project_15_14.html の Cyberpunk テーマ保持判定
- [ ] すべてのページで SVG アイコンを標準化（20px）
- [ ] 全ナビゲーション動作確認（本番環境）

### 🟢 2月中に完了（2/17-2/28）

- [ ] 検討中ファイル（6個）の利用状況確認・判定
- [ ] Phase 2 削除を実行（6個の要確認ファイル）
- [ ] 最終クリーンアップ確認

---

## ファイルサイズ統計

```
全 HTML ファイル: 約 2.5 MB
削除対象: 約 0.8 MB (32%)
残存: 約 1.7 MB (68%)

期待される削除後のサイズ: 約 1.7 MB
```

---

**所有者**: 丹治統（Toru Tanji）
**最終更新**: 2026-02-07
**ステータス**: 準備完了・承認待機
