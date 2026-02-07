# 🔄 整理戦略の修正版 - シンプル＆安全アプローチ

**作成日**: 2026-02-07
**変更理由**: ローカルプレビューと本番環境の乖離を避けるため
**原則**: 本番環境（Google Apps Script）を絶対に壊さない

---

## 📋 変更サマリー

### ❌ 削除した仮定
```
❌ ローカルプレビューで ?page= パラメータで各ファイルに遷移できる
   → 実装されていない / 本番環境と異なる
```

### ✅ 新しい原則
```
✅ 本番環境（Google Apps Script）が正常に動作している
✅ ローカルプレビューは「参考・確認用」程度
✅ 本番環境への影響を最小化
```

---

## 🎯 修正後の整理目標

### 実施すべき

```
✅ 1. ファイル分類・統計（どのファイルが本当に必要か把握）
✅ 2. バージョンファイルの削除（27個）
   └─ 最新版のみ保持
✅ 3. CSS の統一（デザイン統一）
✅ 4. SVG アイコンの標準化（サイズ20px統一）
```

### 実施すべきでない

```
❌ ローカルプレビューに ?page= ルーティング機能を追加
   → 本番環境の仕組みを複製するリスク
❌ HTML の構造を大きく変更
   → 本番環境との乖離を避けるため
```

---

## 📊 優先度の再整理

### 🔴 高優先度（今週中）

```
1. バージョンファイルの削除（27個）
   ├─ project_15_02_v*.html （16個）
   ├─ project_15_combined_v*.html （12個）
   └─ その他バージョンファイル

   実行コマンド: 📋_CLEANUP_PLAN.md の Phase 1 を実行

2. CSS 統一化（5ファイル）
   ├─ project_15_02.html
   ├─ project_15_combined.html
   ├─ project_ad_scenarios.html
   ├─ project_ad_matrix.html
   └─ line_dashboard.html

   作業: <link rel="stylesheet" href="assets/unified_design_system.css"> を追加
   テスト: 本番環境で動作確認

3. SVG アイコン標準化
   ├─ サイズ: 20px × 20px
   └─ stroke-width: 2.5

   テスト: 本番環境で表示確認
```

### 🟡 中優先度（来週）

```
1. 検討中ファイルの利用状況確認（6個）
   └─ Phase 2 削除か保持か判定

2. project_15_14.html のテーマ保持判定
   └─ Cyberpunk テーマを統一デザインに変更するか判定

3. project_bn_report.html のスタイル確認
   └─ 独自スタイルを保持するか判定
```

### 🟢 低優先度（必要に応じて）

```
1. ローカルプレビューの改善
   └─ 実装は後回し（本番環境を優先）
```

---

## ✅ 実装チェックリスト（修正版）

### Phase 1: バージョンファイル削除

```
対象: 27個のバージョンファイル
実行: bash コマンド（コピー&ペーストで安全実行）
確認: ファイル数が 52個 → 25個に減少することを確認
```

**実行前に**:
- [ ] バックアップ取得
- [ ] git status で現在の状態確認

**実行**:
```bash
# 📋_CLEANUP_PLAN.md の Phase 1 コマンドを実行
cd "C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル"

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

**確認**:
```bash
# ファイル数確認（25個前後になっているはず）
ls -1 *.html | wc -l
```

---

### Phase 2: CSS 統一化（5ファイル）

**対象ファイル**:
```
1. project_15_02.html
2. project_15_combined.html
3. project_ad_scenarios.html
4. project_ad_matrix.html
5. line_dashboard.html
```

**各ファイルで実施**:

```html
<!-- <head> セクションに以下を追加 -->
<link rel="stylesheet" href="assets/unified_design_system.css">
```

**確認方法**:
```bash
# 本番環境にデプロイ後、見た目を確認
# ブラウザで本番 URL を開く
# → CSS が正常に読み込まれているか確認
# → 色・フォントが統一されているか確認
```

---

### Phase 3: SVG アイコン標準化

**対象ファイル**: 全9個のプロジェクトファイル

**作業**:
```html
<!-- ❌ 現在（不統一） -->
<svg class="w-4 h-4" ...>
<svg style="width: 16px; height: 16px;" ...>

<!-- ✅ 修正後（統一） -->
<svg style="width: 20px; height: 20px;" ...>
  <path stroke-width="2.5" ...>
</svg>
```

**確認方法**:
```bash
# 本番環境で各ページを確認
# → アイコンサイズが一貫しているか確認
```

---

## 🚀 実行順序（推奨）

```
Step 1: バージョンファイル削除（15分）
        ↓ 完了後、git commit

Step 2: 本番環境にデプロイ（5分）
        ↓ 動作確認

Step 3: CSS 統一化（25分）
        ├─ 5ファイルを編集
        └─ 各編集後、本番環境で確認

Step 4: SVG アイコン標準化（30分）
        ├─ 各ファイルのアイコンを検査
        └─ 必要に応じて修正

Step 5: 最終確認（15分）
        ├─ 本番環境で全ページ確認
        └─ デザイン統一を確認

合計: 約90分
```

---

## ⚠️ 本番環境を守るための約束

実施時に以下を守ってください：

```
✅ 必須
├─ 削除前に必ずバックアップを取得する
├─ 1つの変更ごとに本番環境で動作確認する
├─ CSS 追加時に他の CSS と競合していないか確認する
├─ SVG 修正時に HTML 構造は変更しない
└─ 疑問があれば、修正前に確認する

❌ 禁止
├─ HTML の大きな構造変更
├─ 本番環境にデプロイせずに大量変更
├─ 古いバージョンファイルを参考にして編集
└─ CSS の大幅削除・置き換え
```

---

## 📝 各ステップの詳細手順

### ステップ 1: バージョンファイル削除

**理由**: ディスク使用量削減、混乱防止

**対象**: 27個のバージョンファイル

**実行**:
```bash
# 一括削除コマンドを実行
rm -f project_15_02_v*.html
rm -f project_15_02_backup_*.html
rm -f project_15_02_before_*.html
rm -f project_15_combined_v*.html
```

**確認**:
```bash
# ファイル数確認
ls -1 *.html | wc -l
# → 25個前後になっているはず（現在 52個）
```

---

### ステップ 2: CSS 統一化

**理由**: デザイン統一、保守性向上

**対象ファイル** (5個):
1. project_15_02.html
2. project_15_combined.html
3. project_ad_scenarios.html
4. project_ad_matrix.html
5. line_dashboard.html

**各ファイルで実施**:

```bash
# project_15_02.html を例に

1. ファイルを開く
   code project_15_02.html

2. <head> セクションを見つける

3. 以下を <head> に追加
   <link rel="stylesheet" href="assets/unified_design_system.css">

4. 保存

5. 本番環境にデプロイ
   ./deploy_auto_v2.sh

6. ブラウザで確認
   → 色やフォントが変わっていないか確認
   → 意図しない変更がないか確認
```

---

### ステップ 3: SVG アイコン標準化

**理由**: 一貫性のあるUI

**対象**: 全9個のプロジェクトファイル

**手順**:

```bash
# 各ファイルで SVG を検査
grep -n "<svg" project_15_01.html
grep -n "<svg" project_15_02.html
# ... など

# サイズを確認して 20px に統一
# stroke-width を 2.5 に統一
```

---

## 📊 期待される効果

```
削除後:
├─ ファイル数: 52個 → 25個 (52%削減)
├─ ディスク容量: 約 0.65 MB 削減
└─ 管理負荷: 大幅削減

CSS 統一後:
├─ デザイン一貫性: 向上
├─ 保守性: 向上
└─ 「プロフェッショナル」な印象: 向上

SVG 標準化後:
├─ UI 一貫性: 向上
└─ ユーザー体験: 向上
```

---

## 🛡️ 安全策

### バックアップ

```bash
# 実行前に必ず取得
zip -r "backup_2026-02-07.zip" . \
  -x "node_modules/*" ".npm-cache/*" ".git/*"
```

### 段階的実行

```bash
# 1つずつ確認しながら進める
# 問題があったら即座にロールバック

git add .
git commit -m "Phase 1: Delete version files"
./deploy_auto_v2.sh  # 本番にデプロイ
# ブラウザで確認
# 問題なければ次に進む
```

### ロールバック方法

```bash
# 問題が発生した場合
git revert <commit-hash>  # 前のコミットに戻す
./deploy_auto_v2.sh      # 本番環境も戻す
```

---

## ✅ 最終チェックリスト

実行前に必ず確認してください：

- [ ] バックアップを取得した
- [ ] git status で現在の状態を確認した
- [ ] 本番環境が正常に動作していることを確認した
- [ ] デプロイスクリプト (deploy_auto_v2.sh) が認証済み
- [ ] 削除対象ファイルを最終確認した
- [ ] 各 CSS ファイルが assets フォルダに存在することを確認した

---

## 🎯 成功の定義

整理が成功したと言えるのは：

```
✅ 1. バージョンファイルが削除された（27個）
✅ 2. CSS が 5 ファイルに追加された
✅ 3. SVG アイコンが標準化された
✅ 4. 本番環境で全ページが正常に動作している
✅ 5. デザインが統一されている
✅ 6. 誤削除や破損がない
```

---

## 📞 問題が発生した場合

```
問題: CSS が反映されない
→ 確認: assets フォルダのパス、ブラウザキャッシュをクリア

問題: アイコンが表示されない
→ 確認: SVG パスが正しいか、style 属性を確認

問題: 本番環境が崩れた
→ 解決: git revert + deploy_auto_v2.sh で即座にロールバック
```

---

**この修正版アプローチは**:
- ✅ 本番環境を守る
- ✅ 段階的で安全
- ✅ 各ステップで確認できる
- ✅ 問題発生時にロールバック可能
- ✅ シンプルで分かりやすい

**これで不安を解消して、進めましょう。**

---

**所有者**: 丹治統（Toru Tanji）
**バージョン**: 修正版 2.0
**ステータス**: 準備完了・承認待機
**日時**: 2026-02-07
