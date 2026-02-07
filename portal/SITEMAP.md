Up: [[00_INDEX]]

# Internal DX Portal サイトマップ（想定）

本番の ROUTE_MAP と index / landing の構成から推測した階層です。  
Drive のフォルダ構成やメニュー整理のたたき台にしてください。

---

## 1. トップ（ゲートウェイ）

| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| ポータルホーム | landing | landing.html |
| プロジェクト一覧 | index / home | index.html |

---

## 2. Core Command & Control（中核・統制）

| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| 全体課題管理表 | executive_hub | executive_hub.html |
| 戦略レポート（AD+SECOM統合比較） | infrastructure_strategy / project_15_combined | project_15_combined.html |

---

## 3. Active Project Docs（進行中プロジェクト）

### Phase 1: Current Assessment
| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| 現状インフラ評価 | project_15_14 | project_15_14.html |

### Phase 2: Infrastructure Refresh
| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| ADクラウド化 | project_15_01 | project_15_01.html |
| セコム入退室クラウド化 | project_15_02 | project_15_02.html |
| ネットワークインフラ刷新 | project_15_03 | project_15_03.html |
| 回線刷新ボード / SD-WAN Map | line_dashboard / project_sd_wan | project_sd_wan.html |
| BCPリスク評価マトリクス | bcp_risk_matrix | bcp_risk_matrix.html |

### Phase 3: AI Transformation
| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| AIチャンピオン推進 | project_15_12 | project_15_12.html |

---

## 4. History & Evaluation（履歴・人事考課）

| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| 人事考課原本 | evaluation_sheet | evaluation_sheet.html |
| 活動全史（Daily Log） | daily_log | daily_log.html |
| 議事録: 1/23 調査報告会 | meeting_minutes_20260123 | meeting_minutes_20260123.html |

---

## 5. 限定公開・ゲスト用（必要に応じて別フォルダ）

| 表示名 | page= | ローカルHTML |
|--------|-------|--------------|
| 石井様向け相談資料 | project_15_12_ishii | project_15_12_ishii.html |
| AquaVoice提案書 | project_15_12_proposal | project_15_12_proposal.html |
| Antigravity導入案内 | project_15_12_antigravity | project_15_12_antigravity.html |
| BuddyNet DX Portal | project_buddynet | project_buddynet.html |

---

## フォルダ構成（Drive 用・Nexus_Portal）

**メインフォルダ名: Nexus_Portal**（新規構成。従来の Clawdbot_Portal_Files とは別）

Google Drive に作成するときは、GAS で `CreateNexusPortalStructure.gs` の `createNexusPortalInDrive()` を実行すると、マイドライブ直下に同じ構成が作られます。

```
Nexus_Portal/
├── 00_Private_Tanji/          # 自分だけ
├── 01_Public/                 # 全員（または共有したい範囲）
│   ├── landing.html           # ポータルホーム（ゲートウェイ）
│   ├── index.html             # プロジェクト一覧（コマンドセンター）
│   ├── executive_hub.html     # 全体課題管理表
│   ├── project_15_combined.html   # 戦略レポート（AD+SECOM統合比較）
│   ├── project_15_14.html     # 現状インフラ評価（Phase 1）
│   ├── project_15_01.html     # ADクラウド化（Phase 2）
│   ├── project_15_02.html     # セコム入退室クラウド化（Phase 2）
│   ├── project_15_03.html     # ネットワークインフラ刷新（Phase 2）
│   ├── project_sd_wan.html    # 回線刷新ボード／SD-WAN Map
│   ├── bcp_risk_matrix.html   # BCPリスク評価マトリクス
│   ├── project_15_12.html     # AIチャンピオン推進（Phase 3）
│   ├── evaluation_sheet.html  # 人事考課原本
│   ├── daily_log.html        # 活動全史（Daily Log）
│   ├── meeting_minutes_20260123.html  # 議事録: 1/23 調査報告会
│   └── assets/
│       └── portal_nexus.css   # 共通スタイル（サイドバー・レイアウト）
├── 02_Shared_AIChampion/      # 例: 石井さんなど
│   ├── project_15_12_ishii.html       # 石井様向け相談資料
│   ├── project_15_12_proposal.html    # AquaVoice提案書
│   └── project_15_12_antigravity.html # Antigravity導入案内
└── 03_Shared_InfoSys/         # 例: 情シス
    └── project_sd_wan.html    # 回線刷新ボード／SD-WAN Map（情シス用コピー）
```

※ 実際の「誰にどのフォルダを見せるか」は丹治さんの運用に合わせて変更してください。

---

## 本番のサイト構成（表示上の階層）

本番URLで見えているページの「サイトとしての階層」です。権限の切り分けではなく、メニュー・表示上の構成です。

| カテゴリ | 表示名 | page= | ローカルHTML |
|----------|--------|-------|--------------|
| トップ | ポータルホーム | landing | landing.html |
| トップ | プロジェクト一覧 | index / home | index.html |
| Core | 全体課題管理表 | executive_hub | executive_hub.html |
| Core | 戦略レポート（AD+SECOM統合比較） | infrastructure_strategy / project_15_combined | project_15_combined.html |
| Phase 1 | 現状インフラ評価 | project_15_14 | project_15_14.html |
| Phase 2 | ADクラウド化 | project_15_01 | project_15_01.html |
| Phase 2 | セコム入退室クラウド化 | project_15_02 | project_15_02.html |
| Phase 2 | ネットワークインフラ刷新 | project_15_03 | project_15_03.html |
| Phase 2 | 回線刷新ボード／SD-WAN Map | line_dashboard / project_sd_wan | project_sd_wan.html |
| Phase 2 | BCPリスク評価マトリクス | bcp_risk_matrix | bcp_risk_matrix.html |
| Phase 3 | AIチャンピオン推進 | project_15_12 | project_15_12.html |
| 履歴・人事 | 人事考課原本 | evaluation_sheet | evaluation_sheet.html |
| 履歴・人事 | 活動全史（Daily Log） | daily_log | daily_log.html |
| 履歴・人事 | 議事録: 1/23 調査報告会 | meeting_minutes_20260123 | meeting_minutes_20260123.html |
| 限定公開 | 石井様向け相談資料 | project_15_12_ishii | project_15_12_ishii.html |
| 限定公開 | AquaVoice提案書 | project_15_12_proposal | project_15_12_proposal.html |
| 限定公開 | Antigravity導入案内 | project_15_12_antigravity | project_15_12_antigravity.html |
| 限定公開 | BuddyNet DX Portal | project_buddynet | project_buddynet.html |
