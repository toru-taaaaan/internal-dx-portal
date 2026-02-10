# 📝 HTML レポート編集ワークフロー

## クイックスタート

### **ステップ 1: ローカルプレビューを開く**
```
ブラウザで開く: http://localhost:8000/?page=project_15_01
```

### **ステップ 2: 編集指示を Bravo に与える**
```
例：
"project_15_01.html の『IIJ の費用概算』セクションを、
以下のメール内容を反映して更新してください：
メール: 2025-12-12_IIJメール_追加見積依頼.md
更新項目: サーバー費用を ¥XXX → ¥YYY に変更"
```

### **ステップ 3: ファイルを確認**
```
Bravo が編集完了 → ブラウザで F5 リロード → 確認
```

### **ステップ 4: 本番環境にデプロイ**
```
Bravo に指示: "deploy_auto.sh で本番にデプロイしてください"
```

---

## 📋 編集テンプレート

Bravo への指示を効率的にするため、このテンプレートを使用してください：

```markdown
## 編集依頼

**対象ファイル**: project_15_01.html
**編集セクション**: [セクション名]
**変更内容**: [変更内容の説明]

### 根拠資料
- ファイル名: [参照ファイル]
- パス: 01_IIJ/04_メール履歴/[ファイル]
- 抜粋: [引用]

### ファクトチェック
- [ ] 金額が合致
- [ ] 日付が合致
- [ ] 仕様が正確

### プレビュー確認
http://localhost:8000/?page=project_15_01
```

---

## 🔐 デプロイ流れ

### **1. 編集完了後**
```bash
cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
./deploy_auto.sh
```

### **2. Google Apps Script が自動で：**
- ファイルを push
- バージョンを作成
- 本番環境にデプロイ

### **3. 確認**
```
https://script.google.com/a/akiba-holdings.co.jp/macros/s/AKfycbzubD24U27_X6_SREm4vqrPl5fVs8fmzvW1pGjaKXzyV1lJ_cVv66akCpvwEJHXO71XFQ/exec?page=project_15_01
```

---

## ⚠️ 注意事項

1. **ローカルと本番は別** - ローカルプレビューで OK でも、本番で表示されないことがあります
2. **Google 認証** - デプロイ時に認証が必要な場合があります（Bravo が対応）
3. **GAS 履歴制限** - 200回以上の履歴は自動削除されます（Bravo が管理）

---

**最終更新**: 2026-02-07
