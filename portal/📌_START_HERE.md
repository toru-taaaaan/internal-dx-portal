# 📌 プロジェクト 15 - 編集開始ガイド

**環境整備完了日**: 2026-02-07
**環境**: Bravo（仕事用PC）
**目標**: 6つの HTML レポート完成（今週中）

---

## 🎉 環境は完全に整いました

### ✅ すべての準備が整った項目

```
✓ 資料の一元管理
  → 00_RESOURCE_INDEX.md を参照して、すべての関連資料にアクセス可能

✓ Google Apps Script デプロイの自動化
  → clasp が認証済み、毎回認証不要

✓ ローカルプレビュー環境
  → http://localhost:8000 で各ページをリアルタイム確認可能

✓ ファクトチェックシステム
  → チェックリストに沿って、メール・資料を確認して編集

✓ 編集ワークフロー
  → 編集指示 → Bravo が実行 → プレビュー → デプロイ の流れ確立
```

---

## 🚀 今すぐ始める（3ステップ）

### **Step 1: ローカルプレビューを起動**

```bash
cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
npx http-server -p 8000 -g
```

**ブラウザで開く:**
```
http://localhost:8000/?page=project_15_01
```

### **Step 2: 編集指示を Bravo に与える**

例:
```
Bravo、project_15_01.html を編集してください。

「IIJ 年間費用：¥XXX」という行を、
以下のメール内容に更新してください：

メール: 2025-12-12_IIJメール_追加見積依頼.md
該当部分: 「...見積額は¥YYY となります」

その他の見積数字も同じメールで確認して
反映させてください。
```

### **Step 3: 確認してデプロイ**

```bash
# ブラウザで F5 リロード → 変更確認
# 納得したら本番にデプロイ

cd C:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル
./deploy_auto_v2.sh
```

---

## 📂 重要なファイル

| ファイル | 説明 | 用途 |
|---|---|---|
| `00_RESOURCE_INDEX.md` | 全資料の場所ガイド | 資料を探す時に参照 |
| `✅_ENVIRONMENT_SETUP_CHECKLIST.md` | 環境整備の詳細 | トラブル時に参照 |
| `deploy_auto_v2.sh` | 改善版デプロイスクリプト | 本番環境に反映 |
| `🎯_COMPREHENSIVE_PROJECT_ANALYSIS.md` | 6つのHTMLの詳細分析 | 編集方針を決める時に参照 |

---

## 📋 これから編集する 6 つのプロジェクト

### **優先度別（推奨）**

```
🔥 高優先度（重要）
└─ project_15_01.html (AD Cloud Lift)
   └─ project_15_02.html (Secom Cloud)
   └─ project_15_combined.html (統合比較)

⚡ 中優先度
└─ project_ad_scenarios.html (シナリオ比較)
└─ project_ad_matrix.html (責任分界)

💡 低優先度
└─ line_dashboard.html (SD-WAN Map)
```

---

## 🎯 今週の目標

```
月〜金: 各プロジェクトを 1 つずつ編集・完成
土: 最終レビューと本番環境への一括デプロイ
日: 動作確認と調整
```

---

## ⚠️ 編集時の約束

### ハルシネーション防止のため
- ✅ **すべての数字・日付・人名は、メール・見積書で必ず確認**
- ✅ **参照したメールファイル名を明記**
- ✅ **チェックリストを使用**

### 環境を壊さないため
- ✅ **編集前にローカルプレビューで確認**
- ✅ **納得したら本番デプロイ**
- ✅ **デプロイ後に本番環境でも確認**

---

## 📞 問題が発生した場合

```
1. 認証エラー
   → clasp login を実行

2. ローカルプレビューが更新されない
   → http-server を再起動 & ブラウザキャッシュクリア

3. デプロイに失敗
   → deploy_auto_v2.sh のログを確認
   → エラーメッセージを Bravo に報告
```

---

## ✅ 編集開始前の最終確認

```bash
# 1. プレビューが動作するか確認
curl http://localhost:8000/?page=project_15_01

# 2. clasp が認証済みか確認
clasp status

# 3. デプロイスクリプトが実行可能か確認
ls -la deploy_auto_v2.sh
```

---

## 🎉 準備完了！

**すべての環境が整いました。**

どのプロジェクトから編集を開始しますか？

- [ ] project_15_01.html (AD Cloud Lift)
- [ ] project_15_02.html (Secom Cloud)
- [ ] project_15_combined.html (統合比較)
- [ ] project_ad_scenarios.html (シナリオ)
- [ ] project_ad_matrix.html (責任分界)
- [ ] line_dashboard.html (SD-WAN Map)

**指示をください！** 🚀

---

**Bravo より**: 環境整備が完全に終わったので、あとは編集するだけです。スムーズに進むはずです。頑張ってください！

