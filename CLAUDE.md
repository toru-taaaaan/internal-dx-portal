# Internal DX Portal

## ファイル配置
- HTMLファイルは `src/` に配置（ルートに置かない）
- deploy.ymlで `src/*` と `assets/` を `_site/` に統合

## Git運用
- コミットメッセージは体言止め（1行）
- Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

## デプロイ
- `git push` → GitHub Actions自動デプロイ（1-3分）
- URL: https://internal-dx-portal-auth.tanjiadm.workers.dev/

## 注意
- トーンマナー・禁止表現・エビデンスルールは MEMORY.md を参照
- 会社名: AKIBAホールディングス（大文字AKIBA、カタカナ「ホ」）
