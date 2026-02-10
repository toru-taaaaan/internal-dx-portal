Up: [[00_INDEX]]

# Internal DX Portal - ローカルHTMLファイル一覧

## 📁 GAS Webアプリに対応するローカルHTMLファイル

以下のURLパラメータに対応するローカルHTMLファイルがあります：

| URLパラメータ | ローカルHTMLファイル | 説明 |
|------------|------------------|------|
| `?page=landing` | `landing.html` | エントリーページ（ゲートウェイ） |
| `?page=home` | `index.html` | コマンドセンター（メインダッシュボード） |
| `?page=project_15.01_ADクラウド化` | `project_15_01.html` | ADクラウド化プロジェクト |
| `?page=project_15.02_セコム入退室クラウド化` | `project_15_02.html` | セコム入退室クラウド化プロジェクト |
| `?page=project_15.03_ネットワークインフラ刷新` | `project_15_03.html` | ネットワークインフラ刷新プロジェクト |
| `?page=project_15.01_entraid_proposal` | `project_15_01_entraid_proposal.html` | EntraID移行提案（新規） |

## 🚀 ローカルでプレビューする方法

### 方法1: 単一ファイルをプレビュー
```powershell
.\preview.ps1 landing.html
.\preview.ps1 index.html
.\preview.ps1 project_15_01_entraid_proposal.html
```

### 方法2: すべてのHTMLファイルを処理してローカルサーバー起動
```powershell
.\dev_preview.ps1
```
その後、ブラウザで `http://localhost:8000/landing.html` にアクセス

## 📝 ファイルの場所

- **プロジェクトルート**: `Internal_DX_Portal/*.html` - GASにプッシュするファイル
- **バックアップ**: `Internal_DX_Portal/_BACKUP/Internal_DX_Portal_Dev_Archived/*.html` - 過去のバージョン
- **ローカルプレビュー**: `Internal_DX_Portal/local_preview/*.html` - 自動生成（GAS構文を変換済み）

## ⚠️ 注意事項

- プロジェクトルートのHTMLファイルはGASテンプレート構文（`<?= ?>`）を含みます
- ローカルプレビュー用のファイルは`preview.ps1`や`dev_preview.ps1`で自動生成されます
- GASにプッシュする際は、プロジェクトルートのファイルを`clasp push`でアップロードします
