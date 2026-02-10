Up: [[00_INDEX]]

# Internal DX Portal - 開発用README

## 🚀 ローカル開発環境のセットアップ

### 1. 初回セットアップ

```powershell
.\dev_setup.ps1
```

### 2. ローカルプレビューサーバーの起動

すべてのHTMLファイルを処理してローカルサーバーを起動:

```powershell
.\dev_preview.ps1
```

特定のファイルをプレビュー:

```powershell
.\preview.ps1 project_15_01_entraid_proposal.html
```

### 3. 開発ワークフロー

1. **HTMLファイルを編集**
   - プロジェクトルートのHTMLファイルを直接編集

2. **ローカルでプレビュー**
   ```powershell
   .\preview.ps1 [ファイル名].html
   ```

3. **GASにデプロイ**
   - GitHubにプッシュ（自動デプロイ）
   - または `clasp push` で手動デプロイ

## 📝 ファイル構造

```
Internal_DX_Portal/
├── *.html              # GAS用のHTMLファイル（編集対象）
├── Code.js             # GASバックエンドコード
├── local_preview/      # ローカルプレビュー用（自動生成）
├── dev_setup.ps1       # セットアップスクリプト
├── dev_preview.ps1     # プレビューサーバー起動
└── preview.ps1         # 単一ファイルプレビュー
```

## ⚠️ 注意事項

- GASテンプレート構文（`<?= ?>`など）はローカルプレビュー時に自動的に変換されます
- `local_preview/`ディレクトリは自動生成されるため、手動で編集しないでください
- 本番環境への反映は、GitHubへのプッシュまたは`clasp push`で行います

## 🔧 トラブルシューティング

### Pythonが見つからない
- Python 3.7以上をインストールしてください
- パスが通っているか確認: `python --version`

### ポート8000が使用中
- 別のポートを使用するか、使用中のプロセスを終了してください
- `dev_preview.ps1`の最後の行を編集してポート番号を変更できます
