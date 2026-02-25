---
title: Compass ナレッジベース
layout: report
subtitle: ベンダー情報・プロジェクト状況の総合案内
permalink: /compass.html
---

> **運用原則: エビデンスはVendorsで保管、Projectsで調理**
>
> 各ベンダーからの生データ（メール・見積書・議事録）は Vendors に集約。
> プロジェクト単位の比較・判断は Projects で整理する。

---

## Projects — 判断の地図

| # | プロジェクト | ステータス | 関連ベンダー | 備考 |
|---|-------------|-----------|-------------|------|
| 01 | **AD移行** | 3社比較検討中 | IIJ / USEN / LinkAtJapan | ポータル [AD-001](/ADクラウド移行_3社比較・導入計画.html) に比較資料あり |
| 02 | **NW・セキュリティ刷新** | VarioSecure全拠点残存決定（2/24）| Cato(SCSK) / IIJ / VarioSecure | 太田部長の来期予算取り向け |
| 03 | **入退室管理** | 2社比較・検討中 | ALLIGATE(アート) / BitKey(bitlock PRO) | [比較表](https://docs.google.com/spreadsheets/d/1gFg8q2rGX3XnAzoO3daoQ7M-pEMjnJrELtVMlYwG1gc/edit) |
| 04 | **勤怠管理** | 未着手 | — | 入退室管理と連携予定 |

---

## Vendors — 事実の倉庫

### 01. ALLIGATE（株式会社アート）— 入退室管理

| 項目 | 内容 |
|------|------|
| 担当 | 丸亀麻綾 / 山川深 |
| 対象 | SECOM → ALLIGATE Lock Pro リプレース（8拠点21扉） |
| 初期費用 | **¥2,180,000**（税抜）|
| 月額費用 | **¥315,000/月**（税抜・Lock Pro 21扉・特別値引適用）|
| ステータス | 見積受領済（2/24）、SLA回答待ち |
| 注意 | 見積有効期間30日（〜3/26頃）、最低利用2年、和歌山の静脈認証は非対応 |

### 02. Cato Cloud（SCSK）— NW・セキュリティ

| 項目 | 内容 |
|------|------|
| 担当 | 角田（SCSK）|
| 対象 | SASE/SD-WAN導入 |
| 概算費用 | 200名: ¥5,000,000/年、100名: ¥4,000,000/年、Socket追加: ¥800,000/年 |
| ステータス | Q1(Socket構成費用)・Q2(50名以下)回答待ち、ベストプラクティスMTG候補日提案中 |
| 注意 | Q3(Mix案)はVarioSecure残存により取下げ済 |

### 03. IIJ — NW・セキュリティ / AD移行

| 項目 | 内容 |
|------|------|
| 担当 | 梅原佑太朗 |
| NW | FW: ¥227,000/月、リモート: ¥73,200/月 |
| AD | IIJディレクトリサービス（PaaS型）初期¥325,000、SLA 99.99% |
| ステータス | Mix案問い合わせ済（2/23）→ VarioSecure残存により要見直し |

### 04. LinkAtJapan — AD移行

| 項目 | 内容 |
|------|------|
| 担当 | 澤口 |
| 対象 | Azure IaaS型 AD移行（Managed Service for Azure）|
| SI費用 | ¥1,305,000（初期構築）|
| 月額 | アシストプラン ¥50,000 / アシストプラスプラン ¥68,000 |
| ステータス | 提案済み・SLO回答済（2/17）|

### 05. USEN ICT Solutions — ISP・VarioSecure / AD移行

| 項目 | 内容 |
|------|------|
| 担当 | 西川（ISP）/ 内田（AD）|
| AD | AWS IaaS型、移行費 ¥400,000 + 旧AD降格 ¥100,000 |
| ステータス | **メール未回答3件**（2/9, 2/13, 2/17送信分）|
| 緊急 | **和歌山VarioSecure更新期限 2/28** — 西川氏に確認中 |

### 06. VarioSecure — 既存WAN

| 項目 | 内容 |
|------|------|
| 契約元 | USEN ICT Solutions |
| 方針 | **全拠点残存決定**（2/24 塩田部長判断）|
| 拠点 | 築地・多摩・橋本・大阪・京橋・鬼怒川・名古屋・福岡・和歌山 |
| 緊急 | **和歌山更新期限 2/28** |

### 07. BitKey（株式会社ビットキー）— 入退室管理

| 項目 | 内容 |
|------|------|
| 担当 | 川越 順平 |
| 製品 | bitlock PRO（クラウド型入退室管理） |
| 対象 | SECOM セサモTRII → bitlock PRO リプレース（8拠点21扉） |
| ユーザー数 | 524名（FeliCaカード登録者）|
| ステータス | **見積待ち**（2/20 MTG実施、資料確認中） |
| 重要 | **設置方式は固定設置型（配線工事型）必須** ← 設備管理上の制約 |

---

## 直近の注意事項

| 期限 | 内容 | 対応者 |
|------|------|--------|
| **2/28** | VarioSecure和歌山 更新期限 | USEN西川 → 未回答 |
| **〜3/26** | ALLIGATE見積 有効期限（30日間） | 社内検討 |
| 回答待ち | BitKey見積・提案書受領 | ビットキー川越 |
| 回答待ち | BitKey技術仕様確認（FeliCa・CSV・SLA等） | ビットキー川越 |
| 回答待ち | Cato Q1・Q2 + MTG日程調整 | SCSK角田 |
| 回答待ち | ALLIGATE SLA | アート側確認中 |
| 要対応 | IIJ Mix案の取下げ or 質問変更 | 丹治 → IIJ梅原 |
| 要対応 | USEN未回答メール3件（2/9, 2/13, 2/17） | 丹治 → USEN西川 |

---

## Google Drive — Compass フォルダ

詳細なエビデンス（メール原本・見積書PDF・議事録等）は Google Drive の `000_Compass` フォルダに保管。

```
000_Compass/
  Vendors/             ← ベンダー別の生データ
    01_ALLIGATE_Art/   ← emails/ docs/ (見積PDF・Q&A Excel)
    02_Cato_SCSK/      ← emails/ (11通)
    03_IIJ/
    04_LinkAtJapan/
    05_USEN/
    06_VarioSecure/
  Projects/            ← プロジェクト別の横串ビュー
    01_AD_Migration/
    02_NW_Security/
    03_Access_Control/
    04_Attendance/
```

---

*最終更新: 2026-02-25*
