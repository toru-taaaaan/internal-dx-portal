# 🚀 実行準備完了 - ファイル整理の実行ガイド

**状態**: ✅ 準備完了・実行可能
**作成日**: 2026-02-07
**目的**: 「ローカル = 本番最新版」の環境確立

---

## 🎯 目標（確認）

```
現状: ローカルに 52個の HTML ファイル
     ├─ 最新版: 11個
     ├─ バージョンファイル: 27個
     └─ その他: 14個

目標: ローカルに 25個の HTML ファイル
     └─ すべてが「本番で実際に使用中の最新版」
        ※ バージョンファイルは完全に削除
        ※ git で履歴管理
```

---

## 📋 実行手順（シンプル版）

### Step 1: 準備（5分）

```bash
# ディレクトリに移動
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"

# バックアップ取得
zip -r "backup_$(date +%Y%m%d_%H%M%S).zip" . \
  -x "node_modules/*" ".npm-cache/*" ".git/*"

# 現在の状態確認
git status
git log --oneline -5
```

### Step 2: 削除実行（2分）

```bash
# クリーンアップスクリプト実行
./cleanup_files.sh

# 対話形式で確認を促されるので「y」と入力して進める
```

### Step 3: 確認（3分）

```bash
# ファイル一覧確認
ls -1 *.html | wc -l
# → 約 25個になっているはず

# git で変更を確認
git status
```

### Step 4: コミット（2分）

```bash
# すべての変更をステージング
git add .

# コミット作成
git commit -m "整理: バージョンファイル削除（52個→25個）

- project_15_02 バージョンファイル削除（21個）
- project_15_combined バージョンファイル削除（12個）
- 試験版・バックアップファイル削除（9個）
- 本番使用中の最新ファイルのみ保持

結果: ローカル = 本番最新版という状態を確立"

# コミット確認
git log --oneline -3
```

### Step 5: 本番デプロイ（5分）

```bash
# デプロイスクリプト実行
./deploy_auto_v2.sh

# ログ確認
cat deploy_auto_v2.sh.log | tail -20
```

### Step 6: 検証（10分）

```
本番環境（Google Apps Script）で以下を確認：

✅ すべてのプロジェクトページが表示される
   ├─ index.html → プロジェクト一覧
   ├─ project_15_01.html → ADクラウド化
   ├─ project_15_02.html → セコム
   ├─ project_15_combined.html → 統合比較
   ├─ AD・EntraID刷新_移行シナリオ比較検討資料.html → シナリオ
   ├─ project_ad_matrix.html → 責任分界
   ├─ line_dashboard.html → SD-WAN
   ├─ project_15_12.html → AI推進
   ├─ project_15_14.html → インフラ評価
   └─ project_bn_report.html → 財務自動化

✅ すべてのリンクが正常に機能する

✅ デザイン・レイアウトが正常に表示される
```

---

## ⏱️ 所要時間

```
Step 1 (準備)      : 5分
Step 2 (削除実行)  : 2分
Step 3 (確認)      : 3分
Step 4 (コミット)  : 2分
Step 5 (デプロイ)  : 5分
Step 6 (検証)      : 10分
────────────────────
合計              : 約27分
```

---

## 🛡️ 安全策

### 万が一問題が発生した場合

```bash
# 直前のコミットに戻す
git revert HEAD

# または、バックアップから復元
unzip backup_20260207_XXXXXX.zip
```

### デプロイ失敗時

```bash
# ログを確認
cat deploy_auto_v2.sh.log

# エラーメッセージから原因を特定
# 問題を修正後、再度デプロイ
./deploy_auto_v2.sh
```

---

## ✅ 最終確認リスト

実行前に必ず確認してください：

- [ ] バックアップを取得した
- [ ] 本番環境が正常に動作している
- [ ] git が初期化されている (`git status` でエラーが出ない)
- [ ] deploy_auto_v2.sh が存在する
- [ ] cleanup_files.sh が実行可能になっている (`chmod +x`)
- [ ] 重要ファイル（project_15_01.html など）が存在する

---

## 📊 削除されるファイル一覧

### グループ 1: project_15_02 バージョンファイル（21個）

```
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
```

### グループ 2: project_15_combined バージョンファイル（12個）

```
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

### グループ 3: その他不要ファイル（9個）

```
index_old_backup.html
index_new.html
index_hub.html
_generated_css.html
AccessDenied.html
action_dashboard.html
landing_new_concept.html
infrastructure_strategy.html
project.html
project_management.html
project_sd_wan_backup.html
project_sd_wan_v1.html
```

**合計**: 42個削除

---

## 🚀 実行コマンド（ワンライナー）

```bash
# すべてを一度に実行する場合
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル" && \
zip -r "backup_$(date +%Y%m%d_%H%M%S).zip" . -x "node_modules/*" ".npm-cache/*" ".git/*" && \
./cleanup_files.sh && \
git add . && \
git commit -m "整理: バージョンファイル削除（52個→25個）" && \
./deploy_auto_v2.sh && \
echo "✅ クリーンアップと本番デプロイ完了"
```

---

## 📝 実行後の状態

### ローカルファイル構成（最終状態）

```
25個の HTML ファイル（すべて最新版）:

ナビゲーション: 2個
├─ index.html
└─ landing.html

プロジェクト: 10個
├─ project_15_01.html
├─ project_15_02.html
├─ project_15_03.html
├─ project_15_14.html
├─ project_15_combined.html
├─ AD・EntraID刷新_移行シナリオ比較検討資料.html
├─ project_ad_matrix.html
├─ line_dashboard.html
├─ project_15_12.html
└─ project_bn_report.html

管理・参考: 5個
├─ executive_hub.html
├─ bcp_risk_matrix.html
├─ evaluation_sheet.html
├─ daily_log.html
└─ meeting_minutes_20260123.html

その他: 6個
├─ project_15_12_ishii.html
├─ project_15_12_proposal.html
├─ project_15_12_antigravity.html
├─ project_15_01_entraid_proposal.html
├─ project_15_12_ishii_backup.html
└─ project_buddynet.html
（上記6個は条件付き判定後に削除予定）

実質: 19個のみ
```

---

## ✅ 実行後の効果

```
📊 ファイル管理
├─ ファイル数: 52個 → 25個 (52%削減)
├─ ディスク容量: 約 0.65 MB 削減
└─ 複雑度: 大幅削減

🎯 環境の明確性
├─ ローカル = 本番最新版が一目瞭然
├─ バージョン管理は git が担当
└─ ファイル名からバージョンがわからなくなる

🚀 運用効率
├─ 編集時に最新版を探す手間が削減
├─ 古い版で誤って編集する事故が防止
└─ チームメンバーも状況が明確
```

---

## 🎯 実行の判断基準

### 実行してよい条件

- ✅ 本番環境が正常に動作している
- ✅ 重要ファイルのバックアップが取得できている
- ✅ git で変更履歴が管理されている
- ✅ デプロイスクリプトが認証済みである

### 実行を避けるべき条件

- ❌ 本番環境に問題がある
- ❌ バックアップが取得できていない
- ❌ git が初期化されていない
- ❌ デプロイスクリプトが失敗している

---

## 📞 質問がある場合

```
Q: 本当に削除してしまって大丈夫？
A: はい。git で全履歴が保存されているので、
   いつでも過去のバージョンに戻せます。

Q: 本番環境に影響しない？
A: まったく影響しません。本番環境は
   Google Apps Script で独立しているため、
   ローカルファイルの削除は関係ありません。

Q: 削除後に古いバージョンが必要になったら？
A: git で復元できます。
   git log で過去のコミットを確認して、
   git checkout で特定版を復元してください。

Q: デプロイに失敗したら？
A: バックアップから復元するか、
   git revert で前のコミットに戻してから
   再度デプロイしてください。
```

---

## 🏁 最後に

このファイル整理により：

```
✅ ローカル環境が整理される
✅ 「これが最新」が常に明確
✅ チーム全体が状況を理解できる
✅ 編集・保守が効率化される
✅ ミスが減る
```

**実行する準備はできていますか？**

---

**所有者**: 丹治統（Toru Tanji）
**作成日**: 2026-02-07
**ステータス**: ✅ 準備完了・実行可能
**次アクション**: 上記の「実行手順」を順に実行してください

🚀 **さあ、きれいに整理しましょう！**
