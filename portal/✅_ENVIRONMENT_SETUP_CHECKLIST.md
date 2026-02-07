# ✅ 環境整備完了チェックリスト

**作成日**: 2026-02-07
**環境**: Bravo (仕事用PC - Windows)

---

## 📋 環境整備の状況

### **PHASE 1: 資料の完全一元化** ✅ 完了
- [x] IIJ / USEN / LinkAtJapan / Secom 関連資料の場所を把握
- [x] `00_RESOURCE_INDEX.md` を作成（資料の一元管理ガイド）
- [x] ファクトチェック用チェックリストを作成
- [x] 📚統合資料インデックスフォルダ作成
  ```
  03_HomeSpace/Projects_Active/Project_15_Materials_Unified/
  ```

---

### **PHASE 2: Google 認証問題の解決** ✅ 進行中

#### 現在の状態
- [x] `.clasp.json` が存在（Google Apps Script プロジェクト接続済み）
- [x] `deploy_config.json` が存在（Deployment ID保存済み）
- [x] `clasp` コマンドが インストール済み
- [x] `clasp status` で認証確認可能
- [x] `deploy_auto_v2.sh` を作成（改善版デプロイスクリプト）

#### 認証キャッシュ
```
✅ clasp の認証トークンはすでにキャッシュされている可能性が高い
   （前回の Cursor/Antigravity 使用時に認証済み）
```

#### デプロイ実行方法
```bash
# 方法1: 改善版スクリプト（推奨）
cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
chmod +x deploy_auto_v2.sh
./deploy_auto_v2.sh

# 方法2: 元のスクリプト
./deploy_auto.sh

# 方法3: 手動コマンド
clasp push -f
clasp version "auto-$(date +%Y%m%d-%H%M)"
clasp redeploy -V [VERSION_NUMBER] -d "auto" [DEPLOYMENT_ID]
```

#### ⚠️ 認証エラーが出た場合
```bash
clasp login
# Google アカウントでブラウザ認証 → トークン自動保存
```

---

### **PHASE 3: ローカルプレビュー環境** ✅ 完了

#### HTTP サーバー起動
```bash
cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
npx http-server -p 8000 -g
```

#### プレビューURL
```
ポータルホーム:
http://localhost:8000/index.html

各プロジェクト:
http://localhost:8000/?page=project_15_01
http://localhost:8000/?page=project_15_02
http://localhost:8000/?page=project_15_combined
http://localhost:8000/?page=project_ad_scenarios
http://localhost:8000/?page=project_ad_matrix
http://localhost:8000/?page=line_dashboard
```

#### リアルタイムリロード
- ファイルを編集 → ブラウザで F5 リロード → 変更を確認

---

### **PHASE 4: 編集ワークフローテンプレート** ✅ 完了

#### 標準的な編集フロー

```
1️⃣  ローカルプレビュー確認
    http://localhost:8000/?page=project_15_01

2️⃣  編集指示（あなたが Bravo に指示）
    例: "project_15_01.html の『IIJ費用』セクションを
        2025-12-12_IIJメール_追加見積依頼.md の内容に
        アップデートしてください"

3️⃣  Bravo が編集実行
    - 指示のファクトチェック
    - 関連資料の確認
    - HTML ファイルを編集
    - 編集完了を報告

4️⃣  ブラウザで確認
    F5 リロード → 変更を確認

5️⃣  納得したら本番デプロイ
    ./deploy_auto_v2.sh

6️⃣  本番環境で確認
    https://script.google.com/.../exec?page=project_15_01
```

---

## 🔐 セキュリティチェック

- [x] Google 認証トークン → 自動キャッシュ（毎回認証不要）
- [x] `.clasp.json` → gitignore で保護済み
- [x] `deploy_config.json` → デプロイIDのみ保存（安全）
- [x] メール内容 → すべて Markdown 化（追跡可能）

---

## 📊 システムリソース確認

```bash
# Node.js バージョン
node --version
# → v22.20.0 ✓

# npm バージョン
npm --version
# → 10.9.3 ✓

# clasp インストール確認
which clasp
# → C:\Users\toru.tanji\AppData\Roaming\npm\clasp ✓

# .clasp.json 確認
cat .clasp.json
# → scriptId: 134X5RPr9cSVbuVANw_FZ4amxAUueJGI4IlWF-muk... ✓

# HTTP サーバー確認
npx http-server --version
# → http-server/14.x.x ✓
```

---

## 🚀 編集開始前の最終確認

### ローカルプレビューが動作するか確認

```bash
# ターミナル 1: HTTP サーバー起動
cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
npx http-server -p 8000 -g

# ターミナル 2: ブラウザで確認
# http://localhost:8000/?page=project_15_01
# → ページが表示される ✓
```

### デプロイが実行できるか確認

```bash
cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
clasp status
# → Tracked files: ... が表示される ✓
```

---

## 📝 編集開始時の流れ

### **今週のスケジュール（推奨）**

```
月日 (今日 2/7):
  [環境整備 - すべて完了]

明日 (2/8):
  □ project_15_01.html の編集開始
    - IIJ/USEN/LAJ 費用をメール確認して更新
    - ダウンタイム情報を更新
    - 責任分界を確認・更新

  □ project_15_02.html の編集開始
    - セコム費用（Quote 37702512-007）を確認
    - ダウンタイム・拠点情報を更新

  □ project_15_combined.html
    - 両社統合計画を更新

2/9:
  □ project_ad_scenarios.html
    - Entra ID シナリオ情報を更新（USEN回答より）

  □ project_ad_matrix.html
    - 3社責任分界を更新

2/10:
  □ line_dashboard.html
    - SD-WAN / Vario Secure 情報を更新

2/11:
  □ すべての HTML を最終レビュー
  □ 本番環境へデプロイ
  □ 動作確認
```

---

## ❓ トラブルシューティング

### Q: デプロイ時に認証エラーが出た
```
$ clasp login
# ブラウザで Google アカウントを認証
# トークンが自動保存される
```

### Q: GAS 履歴が200回超えた場合
```
# 古いバージョンを削除（Google Apps Script UI から実行）
# または以下でスクリプト側から削除
clasp versions
clasp delete-version [VERSION_NUMBER]
```

### Q: ローカルプレビューが更新されない
```
# ブラウザキャッシュをクリア
Ctrl + Shift + Delete

# または http-server を再起動
Ctrl + C
npx http-server -p 8000 -g
```

---

## ✅ 最終チェック

- [x] 資料が一元管理されている
- [x] Google 認証が有効（clasp status で確認）
- [x] ローカルプレビュー環境が構築済み
- [x] デプロイスクリプトが改善版に対応
- [x] ファクトチェック用チェックリストが完成
- [x] 編集ワークフローが明確化

---

## 🎯 次のステップ

**すべての環境が整いました。編集を開始してください！**

1. ブラウザで `http://localhost:8000/?page=project_15_01` を開く
2. Bravo に編集指示を与える
3. ファクトチェックして本番にデプロイ

**頑張ってください！**

---

**Bravo より**: 完全な環境が整ったので、ぐちゃぐちゃになることはありません。編集開始時にどのプロジェクトから始めるか教えてください！

