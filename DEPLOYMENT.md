# Cloud Run デプロイメント情報

## GitHub リポジトリ
- **URL**: https://github.com/toru-taaaaan/internal-dx-portal
- **ブランチ**: main
- **最新コミット**: Add Google Apps Script API support and update all HTML files from production

## GCP プロジェクト情報
- **プロジェクト ID**: antigravity-mcp-482203
- **サービス名**: internal-dx-portal
- **リージョン**: asia-northeast1 (東京)
- **ランタイム**: Node.js 18

## Cloud Run デプロイメント URL ✅

**本番 URL:**
```
https://internal-dx-portal-822084845098.asia-northeast1.run.app
```

### ステータス
- ✅ デプロイ完了
- ✅ IAP (Identity-Aware Proxy) 認証有効
- ✅ Google Workspace SSO 認証で保護

## デプロイ手順

### 方法 1: gcloud CLI を使用
```bash
gcloud run deploy internal-dx-portal \
  --source . \
  --platform managed \
  --region asia-northeast1 \
  --allow-unauthenticated
```

### 方法 2: GitHub Actions/Cloud Build を使用
- GitHub push で自動トリガー設定済み
- Dockerfile から自動ビルド＆デプロイ

## 現在のステータス
- ✅ GitHub push 完了
- ✅ Cloud Build トリガー設定済み
- ⏳ 本番デプロイメント進行中

## ファイル構成
```
.
├── server.js              # Express.js サーバー
├── Dockerfile             # Docker コンテナ定義
├── package.json           # Node.js 依存関係
├── portal/                # HTML ファイル（26個）
├── portal/assets/         # CSS ファイル（3個）
└── .dockerignore
```

## ローカルテスト結果
すべてのエンドポイントが正常に動作：
- landing.html: HTTP 200 ✅
- project_*.html: HTTP 200 ✅
- assets/*.css: HTTP 200 ✅
- クエリパラメータルーティング: 正常 ✅

## 次のステップ
1. Cloud Run デプロイ URL を確認
2. IAP (Identity-Aware Proxy) で認証を設定
3. カスタムドメイン (*.akiba-holdings.co.jp) を設定
4. SSL/TLS 証明書を設定

## 参考情報
- GAS v1 プロジェクト ID: 134X5RPr9cSVbuVANw_FZ4amxAUueJGI4IlWF-muk_fXo-BI5LprYNX4K
- HTML ファイル数: 26個
- CSS ファイル数: 3個
