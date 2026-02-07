Up: [[00_INDEX]]

# Nexus_Portal（Google Drive 用フォルダ構成）

Internal DX Portal の **Drive 配信用** フォルダ構成です。  
メインフォルダ名は **Nexus_Portal**（従来の Clawdbot_Portal_Files とは別の新規構成）。

## 構成

```
Nexus_Portal/
├── 00_Private_Tanji/          # 自分だけ
├── 01_Public/                 # 全員（または共有したい範囲）
│   └── assets/                # 共通CSSなど
├── 02_Shared_AIChampion/      # 例: 石井さんなど
└── 03_Shared_InfoSys/         # 例: 情シス
```

## 各フォルダに置く HTML（計画）

- **00_Private_Tanji**: 個人用・下書き（必要に応じて）
- **01_Public**: landing, index, executive_hub, project_15_*.html, evaluation_sheet, daily_log, meeting_minutes_*.html, assets/portal_nexus.css
- **02_Shared_AIChampion**: project_15_12_ishii, project_15_12_proposal, project_15_12_antigravity
- **03_Shared_InfoSys**: project_sd_wan.html（情シス用コピーなど）

## Google Drive に作成する方法

### 推奨：AI が貫通で実行（手を出さない）

- 「Drive に Nexus_Portal を作って」と依頼すると、AI が `clasp push` → `clasp run createNexusPortalInDrive` を実行する。
- **1回だけ** GAS で「デプロイ → 新しいデプロイ → API Executable」をデプロイしておくと、以降は AI だけで完了する。  
  手順: プロジェクト直下の `.agent/AIがDriveにNexus_Portalを作る手順.md` を参照。

### 手動で実行する場合

1. GAS エディタで `CreateNexusPortalStructure.gs` の `createNexusPortalInDrive()` を実行する  
2. マイドライブ直下に **Nexus_Portal** が作成され、その中に上記サブフォルダができる  
3. 作成後、各フォルダの「共有」設定で閲覧者を設定する

詳細はプロジェクト直下の [[SITEMAP]].md / [[SITEMAP]].html を参照。
