Up: [[00_INDEX]]

# Internal DX Portal - ローカル開発ワークフロー

## 🎯 目標

ローカルでHTMLファイルを頻繁に編集・更新し、変更が固まったら本番（GAS）にアップロードする。ローカルでのリンク遷移を本番環境でも再現する。

## 📝 開発フロー

### 1. ローカルでHTMLファイルを編集

プロジェクトルートのHTMLファイルを直接編集：

```powershell
# 例: landing.html を編集
code landing.html
```

**重要**: HTMLファイル内のリンクは、GAS形式（`<?=url?>?page=xxx`）で記述してください。

例：
```html
<a href="<?=url?>?page=home">ホームへ</a>
<a href="<?=url?>?page=project_15.01_ADクラウド化">ADクラウド化プロジェクト</a>
```

### 2. ローカルでプレビュー（リンク遷移を確認）

```powershell
# すべてのHTMLファイルを処理してローカルサーバー起動
.\dev_preview.ps1
```

または、単一ファイルをプレビュー：

```powershell
.\preview.ps1 landing.html
```

**動作**:
- `<?=url?>?page=home` → `index.html` に自動変換
- `<?=url?>?page=landing` → `landing.html` に自動変換
- `<?=url?>?page=project_15.01_ADクラウド化` → `project_15_01.html` に自動変換

ローカルサーバー（`http://localhost:8000`）で、リンクをクリックして遷移を確認できます。

### 3. 変更が固まったら本番にアップロード

```powershell
# GASにプッシュ
clasp push
```

**重要**: ローカルで確認したリンク遷移が、そのまま本番環境でも動作します。

## 🔗 リンクの書き方

### ✅ 正しい書き方（推奨）

```html
<!-- GAS形式で記述 -->
<a href="<?=url?>?page=home">ホーム</a>
<a href="<?=url?>?page=project_15.01_ADクラウド化">ADクラウド化</a>
```

### ❌ 間違った書き方

```html
<!-- ローカル用のリンクを直接書かない -->
<a href="index.html">ホーム</a>  <!-- これは本番で動作しません -->
```

## 📋 ページIDとHTMLファイル名のマッピング

`Convert-Links.psm1` に定義されています。新しいページを追加する場合は、このファイルを更新してください：

| ページID | HTMLファイル名 |
|---------|--------------|
| `home` | `index.html` |
| `landing` | `landing.html` |
| `project_15.01_ADクラウド化` | `project_15_01.html` |
| `project_15.01_entraid_proposal` | `project_15_01_entraid_proposal.html` |

## ⚠️ 注意事項

1. **GAS形式で記述**: HTMLファイルは常にGAS形式（`<?=url?>?page=xxx`）で記述してください
2. **ローカルプレビュー**: `preview.ps1`や`dev_preview.ps1`が自動的にローカル用に変換します
3. **本番環境**: GASにプッシュすると、そのまま`<?=url?>?page=xxx`形式で動作します
4. **リンクの一貫性**: ローカルと本番で同じリンク構造が維持されます

## 🐛 トラブルシューティング

### リンクが正しく変換されない

1. `Convert-Links.psm1`にページIDとHTMLファイル名のマッピングを追加
2. HTMLファイル内のリンクが`<?=url?>?page=xxx`形式になっているか確認

### ローカルでリンクをクリックしても遷移しない

1. 対応するHTMLファイルが`local_preview/`ディレクトリに存在するか確認
2. ローカルサーバーが起動しているか確認（`http://localhost:8000`）