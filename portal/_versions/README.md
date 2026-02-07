Up: [[00_INDEX]]

# GAS 過去バージョン (clasp pull --versionNumber)

`fetch_gas_versions.ps1` で取得したスナップショットです。

| フォルダ | バージョン | 説明 |
|----------|------------|------|
| **v1** | 1 | Initial Deploy |
| **v30** | 30 | No description |
| **v55** | 55 | Update: 2026-01-18 12:10 |
| **v182** | 182 | Manual deploy via Antigravity |
| **v185** | 185 | Fix SD-WAN Card Removal |
| **v188** | 188 | Restore project pages and remove SD-WAN card |

## project_sd_wan の有無

- **v1, v30, v55**: `project_sd_wan*.html` なし
- **v182, v185, v188**: `project_sd_wan.html` / `project_sd_wan_backup.html` / `project_sd_wan_v1.html` あり

## 追加取得したい場合

```powershell
cd Internal_DX_Portal
# fetch_gas_versions.ps1 の $versions に番号を足して再実行
.\fetch_gas_versions.ps1
```

特定版だけ pull する例:
```powershell
npx clasp pull --versionNumber 185
# 必要なファイルを _versions 等に手動コピー
```
