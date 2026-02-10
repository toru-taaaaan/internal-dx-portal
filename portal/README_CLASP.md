Up: [[00_INDEX]]

# Internal DX Portal - GASローカル開発ガイド

## 🛠️ claspを使ったローカル開発

このプロジェクトは`clasp`（Command Line Apps Script Projects）を使ってローカルで開発できます。

## 📋 前提条件

1. **Node.jsのインストール**
   ```powershell
   node --version  # v14以上を推奨
   ```

2. **claspのインストール**
   ```powershell
   npm install -g @google/clasp
   ```

3. **claspのログイン**
   ```powershell
   clasp login
   ```
   - ブラウザが開いてGoogleアカウントで認証します
   - 組織アカウント（akiba-holdings.co.jp）でログインしてください

## 🚀 開発ワークフロー

### 1. ローカルでファイルを編集

プロジェクトルートのHTMLファイルやCode.jsを直接編集します：

```
Internal_DX_Portal/
├── Code.js                    # GASバックエンドコード
├── *.html                     # HTMLテンプレートファイル
├── appsscript.json           # GAS設定ファイル（必要に応じて）
└── .clasp.json               # clasp設定（既に設定済み）
```

### 2. ローカルでプレビュー（HTMLのみ）

GASテンプレート構文を含むHTMLファイルをローカルで確認：

```powershell
# 単一ファイルをプレビュー
.\preview.ps1 project_15_01_entraid_proposal.html

# または、すべてのファイルを処理してローカルサーバー起動
.\dev_preview.ps1
```

**注意**: ローカルプレビューではGASテンプレート構文（`<?= ?>`など）は変換されますが、完全な動作確認はGAS環境で行う必要があります。

### 3. GASにプッシュ（デプロイ）

変更をGASプロジェクトに反映：

```powershell
# 変更をプッシュ
clasp push

# 強制プッシュ（すべてのファイルを上書き）
clasp push -f
```

### 4. デプロイ（Webアプリとして公開）

新しいバージョンとしてデプロイ：

```powershell
clasp deploy
```

または、既存のデプロイを更新：

```powershell
clasp deploy --version [バージョン番号]
```

## 📝 よく使うclaspコマンド

```powershell
# ログイン状態を確認
clasp login --status

# プロジェクト情報を確認
clasp open

# ファイル一覧を確認
clasp list

# 特定のファイルを開く（GASエディタで）
clasp open --webapp

# ログを確認
clasp logs
```

## 🔄 完全な開発サイクル

1. **ローカルで編集**
   - VSCodeやCursorでHTML/JSファイルを編集

2. **ローカルでプレビュー**（オプション）
   ```powershell
   .\preview.ps1 [ファイル名].html
   ```

3. **GASにプッシュ**
   ```powershell
   clasp push
   ```

4. **GASエディタで確認**
   ```powershell
   clasp open
   ```

5. **Webアプリで動作確認**
   - デプロイURLにアクセスして動作確認

## ⚠️ 重要な注意事項

### .clasp.jsonについて
- `.clasp.json`には`scriptId`が含まれています
- このファイルは`.gitignore`に含まれているため、Gitにはコミットされません
- 各開発者が`clasp clone`でプロジェクトをクローンする必要があります

### ファイルの同期
- `clasp push`は変更されたファイルのみをプッシュします
- すべてのファイルを強制的にプッシュする場合は`clasp push -f`を使用

### GASテンプレート構文
- HTMLファイル内の`<?= ?>`構文はGASサーバー側で処理されます
- ローカルプレビューでは変換されますが、完全な動作確認はGAS環境で行ってください

## 🐛 トラブルシューティング

### clasp loginが失敗する
```powershell
# ログアウトして再ログイン
clasp logout
clasp login
```

### プッシュが失敗する
- `.clasp.json`の`scriptId`が正しいか確認
- `clasp login --status`でログイン状態を確認
- ファイルサイズが大きすぎないか確認（GASには制限があります）

### ローカルプレビューでGAS構文が表示される
- これは正常です。完全な動作確認はGAS環境で行ってください

## 📚 参考リンク

- [clasp公式ドキュメント](https://github.com/google/clasp)
- [Google Apps Script公式ドキュメント](https://developers.google.com/apps-script)
