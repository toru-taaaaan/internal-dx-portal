# 🎯 最終的なファイルマッピング - 「これが最新」を明確に

**作成日**: 2026-02-07
**目的**: ローカル = 本番最新版という状態を永遠に保つ

**原則**:
- ✅ ローカルに存在するファイル = 本番で使用中の最新版
- ❌ 古いバージョン・バックアップファイルは削除
- ✅ ファイル名でバージョンが分からなくなるレベルまで整理

---

## 📊 完全なファイルマッピング表

### グループ A: メインナビゲーション（2個） ✅ 最新版

| ファイル名 | 本番環境での役割 | 状態 | 備考 |
|-----------|------------|------|------|
| `index.html` | プロジェクト一覧・Command Center | ✅ 最新版 | 2026-02-07 修正済み |
| `landing.html` | ポータルホーム・ゲートウェイ | ✅ 最新版 | 保持 |

---

### グループ B: Phase 1（1個） ✅ 最新版

| ファイル名 | 本番環境での役割 | 状態 | 備考 |
|-----------|------------|------|------|
| `project_15_14.html` | インフラ環境の可視化と評価 | ✅ 最新版 | Cyberpunk テーマ保持 |

---

### グループ C: Phase 2（6個） ✅ 最新版

| ファイル名 | 本番環境での役割 | 状態 | 削除対象 | 備考 |
|-----------|------------|------|---------|------|
| `project_15_01.html` | ADクラウド化比較 | ✅ 最新版 | - | 2026-02-07 CSS統一完了 |
| `project_15_02.html` | セコム入退室クラウド化 | ✅ 最新版 | - | メインファイル |
| `project_15_03.html` | ネットワークインフラ刷新 | ⚠️ 確認中 | 📋 下記参照 | 本番使用中か確認 |
| `project_15_combined.html` | AD+SECOM統合比較 | ✅ 最新版 | - | メインファイル |
| `AD・EntraID刷新_移行シナリオ比較検討資料.html` | AD移行シナリオ比較 | ✅ 最新版 | - | メインファイル |
| `project_ad_matrix.html` | 3社責任分界点比較 | ✅ 最新版 | - | メインファイル |

---

### グループ D: Phase 2 ネットワーク（1個） ✅ 最新版

| ファイル名 | 本番環境での役割 | 状態 | 備考 |
|-----------|------------|------|------|
| `line_dashboard.html` | SD-WAN Map / 回線刷新ボード | ✅ 最新版 | メインファイル |

---

### グループ E: Phase 3（1個） ✅ 最新版

| ファイル名 | 本番環境での役割 | 状態 | 備考 |
|-----------|------------|------|------|
| `project_15_12.html` | AIチャンピオン推進 | ✅ 最新版 | メインファイル |

---

### グループ F: Phase 4（1個） ✅ 最新版

| ファイル名 | 本番環境での役割 | 状態 | 修正 | 備考 |
|-----------|------------|------|------|------|
| `project_bn_report.html` | PL予実・着地予測自動化 | ✅ 最新版 | 2026-02-07 リンク修正 | メインファイル |

---

### グループ G: 管理・参考ページ（5個） ✅ 最新版

| ファイル名 | 役割 | 状態 | 備考 |
|-----------|------|------|------|
| `executive_hub.html` | 全体課題管理表 | ✅ 最新版 | - |
| `bcp_risk_matrix.html` | BCPリスク評価 | ✅ 最新版 | - |
| `evaluation_sheet.html` | 人事考課原本 | ✅ 最新版 | - |
| `daily_log.html` | 活動全史（ログ） | ✅ 最新版 | - |
| `meeting_minutes_20260123.html` | 議事録: 1/23 | ✅ 最新版 | - |

---

## ❌ 削除対象ファイル一覧（確定版）

### グループ 1: project_15_02 バージョンファイル（21個）

```
❌ 削除
├─ project_15_02_v20260121_1321.html
├─ project_15_02_v20260121_1333.html
├─ project_15_02_v20260121_1337.html
├─ project_15_02_v20260121_1339.html
├─ project_15_02_v20260121_1345.html
├─ project_15_02_v20260121_1350.html
├─ project_15_02_v20260121_1355.html
├─ project_15_02_v20260121_1400.html
├─ project_15_02_v20260121_1410.html
├─ project_15_02_v20260121_1420.html
├─ project_15_02_v20260121_1430.html
├─ project_15_02_v20260121_1440.html
├─ project_15_02_v20260121_1510.html
├─ project_15_02_v20260121_1530.html
├─ project_15_02_v20260121_1540.html
├─ project_15_02_v20260121_1545.html
├─ project_15_02_v20260121_1550.html
├─ project_15_02_v20260121_1600.html
├─ project_15_02_v20260121_1630.html
├─ project_15_02_v20260121_1640.html
└─ （計21個）

✅ 保持
└─ project_15_02.html （最新版のみ）

理由: 古いバージョンファイル。最新版のみ必要。
```

### グループ 2: project_15_02 バックアップファイル（5個）

```
❌ 削除
├─ project_15_02_backup_20260121_123604.html
├─ project_15_02_backup_downtime_20260121_125351.html
├─ project_15_02_backup_subtitle_20260121_125137.html
├─ project_15_02_before_latest_update_20260121_123842.html
└─ project_15_02_before_merge_20260121_124220.html

✅ 保持
└─ project_15_02.html （最新版のみ）

理由: バックアップファイル。最新版で全て統合済み。
```

### グループ 3: project_15_combined バージョンファイル（12個）

```
❌ 削除
├─ project_15_combined_v20260121_1500.html
├─ project_15_combined_v20260121_1510.html
├─ project_15_combined_v20260121_1520.html
├─ project_15_combined_v20260121_1530.html
├─ project_15_combined_v20260121_1535.html
├─ project_15_combined_v20260121_1540.html
├─ project_15_combined_v20260121_1550.html
├─ project_15_combined_v20260121_1600.html
├─ project_15_combined_v20260121_1605.html
├─ project_15_combined_v20260121_1615.html
├─ project_15_combined_v20260122_1105.html
└─ project_15_combined_v20260122_1120.html

✅ 保持
└─ project_15_combined.html （最新版のみ）

理由: 古いバージョンファイル。最新版のみ必要。
```

### グループ 4: ナビゲーション・インデックス（複数）

```
❌ 削除（本番で使用されていないため）
├─ index_old_backup.html
├─ index_new.html
├─ index_hub.html

✅ 保持
└─ index.html （本番使用中）

理由: 試験版・バックアップ。最新版のみ必要。
```

### グループ 5: その他ユーティリティ

```
❌ 削除（本番で未使用）
├─ _generated_css.html
├─ AccessDenied.html
├─ action_dashboard.html
├─ landing_new_concept.html
├─ infrastructure_strategy.html
├─ project.html
├─ project_management.html
├─ project_sd_wan_backup.html
├─ project_sd_wan_v1.html

理由: 試験版・古い構成・未使用。
```

---

## ⚠️ 確認が必要なファイル（削除判定待機）

### グループ X: 条件付き判定

| ファイル名 | 現状 | 判定必要事項 | 推奨 |
|-----------|------|-----------|------|
| `project_15_03.html` | 12K | 本番環境でリンクされているか | 確認後判定 |
| `project_15_01_entraid_proposal.html` | 7.2K | 参考資料として必要か | 削除推奨 |
| `project_15_12_ishii.html` | 16K | 石井様へ個別配布中か | 削除推奨 |
| `project_15_12_proposal.html` | 5.9K | 最新構成で参考資料として必要か | 削除推奨 |
| `project_15_12_antigravity.html` | 11K | Antigravity 導入説明用か | 削除推奨 |
| `project_15_12_ishii_backup.html` | 7.1K | ishii.html のバックアップか | 削除推奨 |

**判定方法**:
```bash
# 本番環境（Google Apps Script）で各ファイルが
# 実際にリンクされているかを確認
# → リンクなし = 削除可
# → リンク有り = 保持
```

---

## 🎯 削除完了後の最終ファイル構成

### 削除実行後（約25個のみ）

```
社内DXポータル/
├─ 🌐 ナビゲーション（2個）
│  ├─ index.html ✅
│  └─ landing.html ✅
│
├─ 📊 プロジェクトページ（10個）
│  ├─ Phase 1/
│  │  └─ project_15_14.html ✅
│  ├─ Phase 2/
│  │  ├─ project_15_01.html ✅
│  │  ├─ project_15_02.html ✅
│  │  ├─ project_15_03.html ⚠️ (確認待機)
│  │  ├─ project_15_combined.html ✅
│  │  ├─ AD・EntraID刷新_移行シナリオ比較検討資料.html ✅
│  │  ├─ project_ad_matrix.html ✅
│  │  └─ line_dashboard.html ✅
│  ├─ Phase 3/
│  │  └─ project_15_12.html ✅
│  └─ Phase 4/
│     └─ project_bn_report.html ✅
│
├─ 🔧 管理ページ（5個）
│  ├─ executive_hub.html ✅
│  ├─ bcp_risk_matrix.html ✅
│  ├─ evaluation_sheet.html ✅
│  ├─ daily_log.html ✅
│  └─ meeting_minutes_20260123.html ✅
│
├─ 🎨 スタイル（2個）
│  └─ assets/
│     ├─ portal_nexus.css
│     └─ unified_design_system.css
│
└─ 📚 ドキュメント（7個）
   ├─ 🔧_SYSTEM_ARCHITECTURE_v2.md
   ├─ 📋_CLEANUP_PLAN.md
   ├─ 📑_FILE_STATUS_MATRIX.md
   ├─ ✅_ORGANIZATION_CHECKLIST.md
   ├─ 🎯_COMPLETE_INVENTORY.md
   ├─ 📖_DOCUMENTATION_INDEX.md
   └─ 🔄_REVISED_ORGANIZATION_STRATEGY.md
```

**総ファイル数**: 52個 → 25個 (52%削減)

---

## ✅ 実行チェックリスト

### 実行前（必須確認）

- [ ] バックアップを取得した
  ```bash
  zip -r backup_2026-02-07.zip . \
    -x "node_modules/*" ".npm-cache/*"
  ```

- [ ] git status で現在の状態を確認した
  ```bash
  git status
  ```

- [ ] 本番環境が正常に動作している
  - 本番 URL を開いて、全ページが表示されることを確認

- [ ] 削除対象ファイルが完全な重複であることを再確認した

### 実行手順

#### Step 1: 確認が必要なファイルの判定

```bash
# project_15_03.html の使用状況を確認
# 本番環境でリンクされているか確認
# → リンク有り：保持
# → リンク無し：削除

# その他の判定ファイルについても同様に確認
```

**確認結果**: `project_15_03.html` は保持/削除？

#### Step 2: 削除実行

```bash
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"

# project_15_02 バージョンファイル削除（21個）
rm -f project_15_02_v20260121_*.html
rm -f project_15_02_backup_*.html
rm -f project_15_02_before_*.html

# project_15_combined バージョンファイル削除（12個）
rm -f project_15_combined_v20260121_*.html
rm -f project_15_combined_v20260122_*.html

# その他ファイル削除
rm -f index_old_backup.html
rm -f index_new.html
rm -f index_hub.html
rm -f _generated_css.html
rm -f AccessDenied.html
rm -f action_dashboard.html
rm -f landing_new_concept.html
rm -f infrastructure_strategy.html
rm -f project.html
rm -f project_management.html
rm -f project_sd_wan_backup.html
rm -f project_sd_wan_v1.html
```

#### Step 3: 確認

```bash
# ファイル数確認（約25個になっているはず）
ls -1 *.html | wc -l

# 削除したファイルが本当に消えたか確認
git status
```

#### Step 4: git コミット

```bash
git add .
git commit -m "整理: 52個 → 25個（バージョンファイル・重複削除）

- project_15_02 バージョンファイル削除（21個）
- project_15_combined バージョンファイル削除（12個）
- 試験版・バックアップファイル削除（9個）
- 本番使用中の最新ファイルのみ保持

結果: ローカル = 本番最新版という状態を確立"
```

#### Step 5: 本番環境にデプロイ

```bash
./deploy_auto_v2.sh
```

#### Step 6: 本番環境で確認

```
本番 URL を開いて：
✅ すべてのプロジェクトページが表示される
✅ リンクが正常に機能している
✅ デザインが正常に表示されている
```

---

## 🎯 成功の定義

整理が成功したと言えるのは：

```
✅ ローカルの HTML ファイルが 25 個になった
✅ バージョンファイルが完全に削除された
✅ 本番環境で全ページが正常に動作している
✅ 「ローカルのファイル = 本番最新版」が明確になった
✅ 今後、新しいバージョンファイルが生成されないシステムになった
```

---

## 📝 今後の運用ルール

整理後は、以下の運用ルールを守ってください：

```
✅ 必須ルール

1. ファイル編集時
   └─ メインファイル（project_15_01.html など）のみを編集
      └─ バージョン番号を付けない

2. バックアップが必要な場合
   └─ git で管理（ファイル名では管理しない）
      ```bash
      git add .
      git commit -m "project_15_01: コンテンツ更新"
      ```

3. 古い版に戻したい場合
   └─ git revert または git checkout を使用
      ```bash
      git log --oneline  # コミット履歴表示
      git checkout <hash> -- project_15_01.html  # 特定版を復元
      ```

4. 定期的な確認
   └─ 月1回程度、ローカル = 本番かを確認
```

---

## 🏁 最終チェック

この整理が完了すると：

```
📊 統計
├─ ファイル数: 52個 → 25個 (52%削減)
├─ ディスク容量: 約 0.65 MB 削減
└─ 管理複雑度: 大幅削減

🎯 目標達成
├─ ✅ ローカル = 本番最新版が常に明確
├─ ✅ 古いバージョンが混在しない
├─ ✅ 編集時に「どの版を使うべきか」で迷わない
└─ ✅ チームメンバーも状況が一目瞭然

🚀 運用効率
├─ 編集速度: 向上（最新版探しの時間削減）
├─ エラー率: 低減（古い版で編集する事故削減）
└─ 保守性: 向上（シンプルで分かりやすい）
```

---

**所有者**: 丹治統（Toru Tanji）
**作成日**: 2026-02-07
**ステータス**: 実行準備完了・確認待機
**次アクション**: `project_15_03.html` の利用状況確認 → 削除実行
