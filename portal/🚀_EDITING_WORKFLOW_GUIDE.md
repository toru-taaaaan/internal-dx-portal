# 🚀 編集ワークフロー完全ガイド - スムーズな編集作業のための下準備

**作成日**: 2026-02-07
**目的**: ローカル編集 → 本番デプロイがストレスなく進む環境の確立
**対象**: 丹治統（編集者）

---

## 🎯 このガイドが解決すること

```
❌ 過去の問題
1. どのローカルファイルが本番と対応しているか不明
2. ローカルで完璧でも、本番で崩れる
3. 編集のたびに試行錯誤

✅ このガイド後
1. 本番URL → ローカルファイルが即座に分かる
2. ローカル編集 = 本番表示が同じ
3. 編集手順が明確で迷わない
```

---

## 📋 本番環境のURL一覧（本番URLからローカルファイルへの対応表）

### エントリーポイント

| 本番URL | ローカルファイル | 説明 |
|--------|-------------|------|
| `https://script.google.com/macros/d/134X5RPr9cSVbuVANw_FZ4amxAUueJGI4IlWF-muk_fXo-BI5LprYNX4K/usercss/...` | `index.html` | プロジェクト一覧（Command Center） |
| `https://...?page=landing` | `landing.html` | ポータルホーム（ウェルカムスクリーン） |

### Phase 1: 現状評価

| 本番URL | ローカルファイル | ファイルサイズ | 更新日 |
|--------|-------------|----------|--------|
| `?page=project_15_14` | `project_15_14.html` | 16 KB | 2026-02-07 |

### Phase 2: インフラ刷新

| 本番URL | ローカルファイル | ファイルサイズ | 更新日 | CSS | 状態 |
|--------|-------------|----------|--------|-----|------|
| `?page=project_15_01` | `project_15_01.html` | 108 KB | 2026-02-07 | ✅ unified | ✅ |
| `?page=project_15_02` | `project_15_02.html` | 52 KB | 2026-02-07 | ⏳ portal_nexus | 要統一 |
| `?page=project_15_combined` | `project_15_combined.html` | 24 KB | 2026-02-07 | ⏳ portal_nexus | 要統一 |
| `?page=project_ad_scenarios` | `project_ad_scenarios.html` | 16 KB | 2026-02-07 | ⏳ portal_nexus | 要統一 |
| `?page=project_ad_matrix` | `project_ad_matrix.html` | 20 KB | 2026-02-07 | ⏳ portal_nexus | 要統一 |
| `?page=line_dashboard` | `line_dashboard.html` | 52 KB | 2026-02-07 | ⏳ portal_nexus | 要統一 |

### Phase 3: AI推進

| 本番URL | ローカルファイル | ファイルサイズ | 更新日 | CSS | 状態 |
|--------|-------------|----------|--------|-----|------|
| `?page=project_15_12` | `project_15_12.html` | 36 KB | 2026-02-07 | ⏳ portal_nexus | 要統一 |

### Phase 4: BuddyNet DX

| 本番URL | ローカルファイル | ファイルサイズ | 更新日 | CSS | 状態 |
|--------|-------------|----------|--------|-----|------|
| `?page=project_bn_report` | `project_bn_report.html` | 36 KB | 2026-02-07 | custom | ✓ |

### 管理・参考ページ

| 本番URL | ローカルファイル | 説明 |
|--------|-------------|------|
| `?page=executive_hub` | `executive_hub.html` | 全体課題管理表 |
| `?page=bcp_risk_matrix` | `bcp_risk_matrix.html` | BCPリスク評価 |
| `?page=evaluation_sheet` | `evaluation_sheet.html` | 人事考課原本 |
| `?page=daily_log` | `daily_log.html` | 活動全史（ログ） |
| `?page=meeting_minutes_20260123` | `meeting_minutes_20260123.html` | 議事録: 1/23 |

---

## ⚡ クイックスタート（これを最初に読んでください）

### 編集したいプロジェクトがある場合

```
Step 1: 本番URLを確認
   例: https://.../?page=project_15_02

Step 2: 対応するローカルファイルを確認
   上記表から: project_15_02.html

Step 3: ローカルファイルを編集
   code project_15_02.html

Step 4: ブラウザで確認（2つの方法）

   方法A: ローカルHTMLを直接開く
   └─ file:///C:/Users/toru.tanji/Obsidian/SecondBrain_Final/.../project_15_02.html

   方法B: http-server で確認
   └─ npx http-server -p 8000 -g
      その後、ブラウザで project_15_02.html を確認

Step 5: デザイン確認（重要！）
   └─ ローカルでの表示 = 本番での表示か確認
   └─ CSS が正しく読み込まれているか確認

Step 6: 本番にデプロイ
   ./deploy_auto_v2.sh

Step 7: 本番環境で確認
   本番URL を開いて、表示が正しいか確認
```

---

## 🎨 デザイン崩れを防ぐための重要事項

### CSS 統一の現状

```
✅ 完全に統一されたファイル
├─ project_15_01.html (unified_design_system.css + portal_nexus.css)
└─ project_15_14.html (custom Cyberpunk theme)

⏳ 統一が必要なファイル（5個）
├─ project_15_02.html
├─ project_15_combined.html
├─ project_ad_scenarios.html
├─ project_ad_matrix.html
├─ line_dashboard.html

✅ その他（独自スタイル）
├─ project_bn_report.html (Montserrat Blue theme)
└─ その他管理ページ
```

### デザイン確認チェックリスト

```
編集後、本番デプロイ前に確認すること：

ローカルプレビュー:
☑ CSS が読み込まれている（色・フォント・レイアウト）
☑ SVG アイコンが正常に表示されている（サイズ20px）
☑ テーブルがきちんと表示されている
☑ 色が意図通りになっている
☑ フォントサイズが一貫している

本番確認:
☑ 本番URLを開く
☑ ローカルと同じように表示されている
☑ リンクが正常に動作している
☑ デザインが崩れていない
```

---

## 📁 ローカルファイル検索ガイド

### 方法 1: 対応表を使う（最速）

```
本番URL: ?page=project_15_02
→ 対応表を見る: project_15_02.html
→ ファイルを開く
```

**使う表**: 上記の「本番環境のURL一覧」セクション

### 方法 2: ファイル名で検索

```bash
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"

# ファイル名で検索
ls project_15_*.html

# 特定の内容を検索
grep -l "ADクラウド化" *.html
```

### 方法 3: ファイル一覧（ローカル全ファイル）

```
26個のローカルファイル:

メインプロジェクト:
1. project_15_01.html (108 KB) - ADクラウド化
2. project_15_02.html (52 KB) - セコム入退室
3. project_15_03.html (12 KB) - ネットワークインフラ
4. project_15_12.html (36 KB) - AIチャンピオン推進
5. project_15_14.html (16 KB) - インフラ評価
6. project_15_combined.html (24 KB) - AD+SECOM統合
7. project_ad_scenarios.html (16 KB) - ADシナリオ比較
8. project_ad_matrix.html (20 KB) - 3社責任分界
9. project_bn_report.html (36 KB) - 財務自動化
10. project_sd_wan.html (52 KB) - SD-WAN Map
11. project_buddynet.html (8 KB) - BuddyNet ポータル
12. project_15_01_entraid_proposal.html (7.2 KB) - Entra ID提案
13. project_15_12_antigravity.html (12 KB) - Antigravity

管理・ナビゲーション:
14. index.html (12 KB) - プロジェクト一覧
15. landing.html (12 KB) - ポータルホーム
16. executive_hub.html (36 KB) - 全体課題管理表
17. bcp_risk_matrix.html (12 KB) - BCP評価
18. evaluation_sheet.html (40 KB) - 人事考課
19. daily_log.html (24 KB) - 活動全史
20. meeting_minutes_20260123.html (16 KB) - 議事録

その他:
21. project_15_12_ishii.html (16 KB) - 石井様向け
22. project_15_12_proposal.html (8 KB) - AquaVoice提案
23. project_15_12_ishii_backup.html (8 KB) - ishii.html バックアップ
24. mission_ledger.html (8 KB) - ミッション台帳
25. SITEMAP.html (24 KB) - サイトマップ
26. task_tracker.html (16 KB) - タスク追跡
```

---

## 🔧 編集ワークフロー（詳細版）

### 前提条件

```
ローカル環境が整っていること:
✅ Node.js がインストールされている
✅ clasp が認証済み
✅ deploy_auto_v2.sh が実行可能
✅ assets/ フォルダに CSS ファイルが存在
```

### ワークフロー全体

```
┌─────────────────────────────────────┐
│ 1. 編集対象を特定する                 │
│    本番URL → ローカルファイル         │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 2. ローカルファイルを編集              │
│    （コンテンツ、数字、リンク等）      │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 3. ローカルで確認                     │
│    HTML を直接開く / http-server     │
│    CSS が正しく読み込まれているか    │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 4. デザイン確認                       │
│    意図通りの表示か確認              │
│    デザイン崩れがないか確認          │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 5. 本番環境にデプロイ                 │
│    ./deploy_auto_v2.sh              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 6. 本番環境で確認                     │
│    本番URL を開く                    │
│    ローカルと同じ表示か確認          │
│    リンク・機能が正常か確認          │
└─────────────────────────────────────┘
```

### 具体例：project_15_02.html を編集する場合

```bash
# Step 1: 対応表から確認
# 本番URL: ?page=project_15_02
# ローカルファイル: project_15_02.html ✓

# Step 2: ファイルを編集
code project_15_02.html

# Step 3a: ローカルで確認（方法A - 直接開く）
# ブラウザで以下を開く:
# file:///C:/Users/toru.tanji/Obsidian/SecondBrain_Final/.../project_15_02.html

# Step 3b: または http-server を使う
npx http-server -p 8000 -g
# ブラウザで http://localhost:8000/project_15_02.html を開く

# Step 4: デザイン確認チェック
# □ CSS が読み込まれている
# □ SVG アイコンが正常
# □ レイアウトが崩れていない
# → すべて OK なら次へ

# Step 5: デプロイ
./deploy_auto_v2.sh

# Step 6: 本番環境で確認
# 本番URL を開く
# https://script.google.com/macros/d/134X5RPr9cSVbuVANw_FZ4amxAUueJGI4IlWF-muk_fXo-BI5LprYNX4K/usercss
# → ?page=project_15_02 を追加して確認
```

---

## 🛡️ デザイン崩れを防ぐためのチェック項目

### ローカルプレビュー時

```
CSS 確認:
☑ <link rel="stylesheet" href="assets/portal_nexus.css"> がある
☑ <link rel="stylesheet" href="assets/unified_design_system.css"> がある (必要なファイルの場合)
☑ ブラウザの開発者ツール (F12) で CSS が読み込まれている
☑ ネットワークタブで 404 エラーがない

デザイン確認:
☑ 色が正しい (Navy #1e293b, Red #dc2626 など)
☑ フォントが正しい (Inter, Noto Sans JP など)
☑ SVG アイコンサイズが 20px × 20px
☑ テーブルレイアウトが崩れていない
☑ レスポンシブデザインが機能している（ウィンドウ幅を変更）
```

### 本番デプロイ後

```
本番確認:
☑ 本番URL を開く
☑ ローカルと同じレイアウトで表示されている
☑ 色・フォント・サイズが同じ
☑ ボタン・リンクがクリック可能
☑ デザインが崩れていない
☑ 画像が表示されている

問題が発生した場合:
□ ブラウザキャッシュをクリア (Ctrl+Shift+Delete)
□ Google Apps Script を再デプロイ
□ ローカルファイルが正しく保存されているか確認
```

---

## 💾 デプロイスクリプト（deploy_auto_v2.sh）について

### 何をするか

```
1. ローカルのすべてのファイルを Google Apps Script にアップロード
2. Google Apps Script のウェブアプリをデプロイ
3. 本番環境を更新

実行時間: 約5分
```

### 実行方法

```bash
# コマンドラインから実行
./deploy_auto_v2.sh

# または
bash deploy_auto_v2.sh

# ログを確認
cat deploy_auto_v2.sh.log | tail -20
```

### デプロイに失敗した場合

```bash
# 認証を確認
clasp status

# 認証情報を更新
clasp login

# もう一度デプロイ
./deploy_auto_v2.sh

# それでも失敗した場合は、
# .clasp.json の scriptId が正しいか確認
cat .clasp.json
```

---

## 📊 CSS 統一の進捗と対応

### 現状

```
✅ 完全統一: 1ファイル
├─ project_15_01.html
└─ CSS: unified_design_system.css + portal_nexus.css

⏳ 統一予定: 5ファイル
├─ project_15_02.html
├─ project_15_combined.html
├─ project_ad_scenarios.html
├─ project_ad_matrix.html
└─ line_dashboard.html
└─ 追加する CSS: <link rel="stylesheet" href="assets/unified_design_system.css">

✅ 独自テーマ: 2ファイル
├─ project_15_14.html (Cyberpunk theme - Orbitron, cyan/purple)
├─ project_bn_report.html (Blue theme - Montserrat)
└─ カスタマイズ: 変更なし
```

### CSS 統一のメリット

```
✅ デザイン一貫性の向上
✅ メンテナンスの効率化
✅ 本番環境での表示が安定
✅ 新規ファイル追加時の対応が簡単
```

---

## ✅ 準備完了チェックリスト

### ローカル環境

- [x] ファイルが 26個に整理された
- [x] バージョンファイルが削除されている
- [x] メインファイルがすべて保持されている
- [x] バックアップが取得されている

### 本番環境

- [ ] 本番環境が正常に動作しているか確認
- [ ] すべてのプロジェクトページが表示されるか確認
- [ ] リンクが正常に機能しているか確認

### デプロイ環境

- [x] clasp が認証済み
- [x] deploy_auto_v2.sh が実行可能
- [x] .clasp.json が正しく設定されている

### 編集準備

- [ ] 本番URL ↔ ローカルファイル対応表を確認
- [ ] CSS の統一状況を理解
- [ ] デザイン確認チェックリストを保存

---

## 🚀 編集開始までの流れ

### 1. 本ガイドを読んで理解する（5分）

```
このドキュメントで編集ワークフローを理解
```

### 2. 本番環境で動作確認（5分）

```
https://... で本番環境がすべて動作しているか確認
```

### 3. ローカルファイルの確認（2分）

```
26個のファイルがローカルに存在することを確認
ls -1 *.html | wc -l
→ 26 が出力されるはず
```

### 4. http-server を準備（1分）

```bash
# http-server をグローバルインストール（初回のみ）
npm install -g http-server

# またはプロジェクトフォルダで
npx http-server -p 8000 -g
```

### 5. 編集開始

```
対応表を見ながら：
本番URL → ローカルファイル → 編集 → デプロイ
```

---

## 📞 よくある質問（Q&A）

### Q1: どのファイルを編集すればいい？

**A:** 対応表を見てください。本番URLが分かれば、ローカルファイルは一意に決まります。

### Q2: デザイン崩れが怖い

**A:** チェックリストに従えば大丈夫です。本番デプロイ前に必ずローカルで確認。

### Q3: ローカルプレビューと本番が違う表示になる

**A:** 以下を確認してください：
```
1. CSS が正しく読み込まれているか (F12 で確認)
2. assets フォルダが存在するか
3. ファイルパスが正しいか
```

### Q4: デプロイに失敗した

**A:**
```bash
clasp login  # 再認証
./deploy_auto_v2.sh  # 再デプロイ
```

### Q5: 古いバージョンに戻したい

**A:** バックアップから復元してください
```bash
unzip backup_20260207_184520.zip
```

---

## 🎯 今からやること

### 今すぐ（5分）

```
1. このドキュメントの対応表を確認
2. 本番URL を開いて、すべてが動作しているか確認
3. ローカルファイルが 26個あるか確認
```

### 次（編集開始まで）

```
1. http-server を起動
2. ローカルファイルを1つ開いて、CSS が読み込まれているか確認
3. 対応表を参考に、本番URL → ローカルファイルのマッピングを理解
```

### 編集開始時

```
1. 対応表で編集対象ファイルを確認
2. ファイルを編集
3. ローカルプレビューで確認
4. デザイン確認チェックリストを実行
5. deploy_auto_v2.sh でデプロイ
6. 本番環境で確認
```

---

## 🎉 これであなたの悩みが解決される

```
✅ ローカルファイル検索性
   └─ 対応表があるから即座に見つかる

✅ デザイン崩れの防止
   └─ ローカルで CSS 確認 → デプロイ → 本番確認で防止

✅ 編集ワークフローの明確化
   └─ ステップバイステップのガイドがある

✅ ストレスの大幅削減
   └─ 何をしていいか迷わない
```

---

**所有者**: 丹治統（Toru Tanji）
**作成日**: 2026-02-07
**ステータス**: ✅ 準備完了
**次アクション**: 上記の「今からやること」を実行

🚀 **スムーズな編集環境、準備完了です！**
