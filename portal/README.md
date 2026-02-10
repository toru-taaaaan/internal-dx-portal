Up: [[00_INDEX]]

# Internal DX Portal - クイックスタートガイド

## 🚀 5分で始めるローカル開発

### 1. セットアップ（初回のみ）

```powershell
# Node.jsとclaspがインストールされているか確認
node --version
clasp --version

# インストールされていない場合
npm install -g @google/clasp

# claspにログイン（初回のみ）
clasp login
```

### 2. HTMLファイルを編集

プロジェクトルートのHTMLファイルを編集：

```powershell
# 例: 新しいHTMLファイルを作成
code project_15_01_entraid_proposal.html
```

### 3. ローカルでプレビュー（オプション）

```powershell
# 単一ファイルをプレビュー
.\preview.ps1 project_15_01_entraid_proposal.html
```

### 4. GASにプッシュ

```powershell
# 変更をGASプロジェクトに反映
clasp push
```

### 5. 動作確認

```powershell
# GASエディタで開く
clasp open

# または、WebアプリのURLに直接アクセス
# https://script.google.com/a/akiba-holdings.co.jp/macros/s/...
```

## 📖 詳細なドキュメント

- **GASローカル開発**: [README_CLASP.md]([[README_CLASP]].md)
- **開発環境**: [README_DEV.md]([[README_DEV]].md)
