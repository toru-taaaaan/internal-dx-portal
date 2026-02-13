# Internal DX Portal Project

## プロジェクト概要
AKIBAホールディングス社内DXポータルサイト
AD移行、SECOM移行、SD-WAN刷新等の比較検討資料（HTML形式）

---

## 📁 ディレクトリ構造

```
portal/
├── src/            # HTMLファイル（開発成果物）
├── assets/         # 静的ファイル（CSS, JS, 画像）
├── docs/           # 開発ドキュメント
├── scripts/        # 自動化スクリプト
├── .github/        # CI/CD設定
└── .claude/        # このファイル
```

---

## 🚫 禁止ワード

### 絵文字
- ❌ 💡（セクションタイトルの絵文字はOK）

### カタカナ
- ❌ 可視化 → ⭕ 表示、確認
- ❌ 戦略的 → 削除
- ❌ インサイト → 削除
- ❌ シームレス → 削除
- ❌ ボトルネック → 削除

### 誇張表現
- ❌ 圧倒的、莫大、唯一、根本から、革新的

### 比喩
- ❌ 牙を剥き
- ❌ ホテル/マンション/コンシェルジュ → お任せ型/分離型/並走型

---

## ✅ 推奨表現

### 体言止め
- ❌ 「～されます」
- ⭕ 「～する」「～予定」

### 簡潔
- ⭕ 「初期比較」のみ
- ❌ 「課題を確認します」→ 削除

### 中立
- ❌ 「業界最安級」→ 削除

---

## 🎯 トーンマナー

### 対象読者
- 50-60代の部長クラス
- 地味で無難なビジネス文書
- 事実ベースで淡々と

### 避けるべき態度
- 上から目線
- AI臭さ
- 攻撃的表現

---

## 🚀 デプロイ

### 自動デプロイ
```bash
# src/ 内のHTMLを編集
git add src/
git commit -m "Update XXX資料"
git push

# → GitHub Actions自動デプロイ（1-3分）
# → https://internal-dx-portal-auth.tanjiadm.workers.dev/
```

### 重要なルール
- HTMLファイルは必ず `src/` 内に配置
- ルートディレクトリにHTMLファイルを置かない
- コミットメッセージは体言止め

---

## 📊 エビデンス管理

エビデンス一覧は以下で管理:
```
~/.claude/projects/C--Users-toru-tanji-Projects-portal/memory/AD_3社比較_エビデンス一覧.md
```

---

## 🔗 関連リポジトリ

- **portal** (このリポジトリ): HTMLポータルサイト
- **dotfiles**: 設定管理（会社・自宅・VPS共通）
- **shared-workspace**: ファイル共有（会社⇔自宅）
- **claude-code-memory**: AI作業履歴

---

## 📞 連絡先

- GitHub: https://github.com/toru-taaaaan/internal-dx-portal
- Email: tanjiadm@gmail.com
