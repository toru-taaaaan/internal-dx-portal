Up: [[00_INDEX]]

# SD-WAN 資料の特定とリンク修正メモ

## 1. 正しいSD-WAN資料（HTML）

**対象**: 「SD-WAN vs Vario Secure 拠点間接続比較」の詳しい資料  
**正しいページID**: `project_sd_wan`  
**正しいURL**: `?page=project_sd_wan`

### ローカルにある `project_sd_wan.html` の場所

| パス | 用途 |
|------|------|
| `Internal_DX_Portal\local_preview\project_sd_wan.html` | ローカルプレビュー用 |
| `GAS_Projects\Archive\InternalDXPortal\project_sd_wan.html` | GASアーカイブ（デプロイ元候補） |
| `Internal_DX_Portal\_BACKUP\Internal_DX_Portal_Dev_Archived\project_sd_wan.html` | バックアップ |

### 内容

- D3.js による拠点間トポロジーマップ（現状 vs SD-WAN）
- USEN / Vario Secure と IIJ Omnibus（SD-WAN）の比較表
- コスト・運用・セキュリティの比較
- 「4. 最終結論：それでもSD-WANを選ぶ理由 (Why SD-WAN?)」など、SD-WANに関する詳しい説明

---

## 2. 間違っているリンク

- **誤**: `?page=line_dashboard` （回線ダッシュボード／回線刷新ボード用）
- **正**: `?page=project_sd_wan`

---

## 3. 写真の「SD-WAN Map」ボタンについて

- ラベル: **SD-WAN Map** / **SD-WAN vs Vario Secure 拠点間接続比較マップ**
- このボタンのリンク先を **`?page=project_sd_wan`** にすることが目的。

### ローカルで確認したHTML

- `index_old_backup.html`  
  - 「SD-WAN Map」カード → 既に `?page=project_sd_wan` にリンク済み
- `index.html`  
  - 「SD-WAN Comparison」→ `?page=project_sd_wan`
- `landing.html`  
  - 「SD-WAN Comparison」→ `?page=project_sd_wan`
- `GAS_Projects\Archive\InternalDXPortal\index.html`  
  - PROJECT SD-WAN カード → `?page=project_sd_wan`

いずれも **SD-WAN 系ボタンは `project_sd_wan` を指している**。

---

## 4. `line_dashboard` が使われている箇所（参考）

- `index_hub.html`  
  - 「回線刷新ボード (Network Refresh)」→ `line_dashboard.html`
- `local_preview\index.html`  
  - 上記と同様
- `local_preview\index_hub.html`  
  - 上記と同様

これらは **回線刷新ボード** 用であり、**SD-WAN Map** 用ではない。

---

## 5. 本番で `line_dashboard` になっている場合の対応

1. **デプロイ元のHTMLを特定**  
   - 実際に GAS にデプロイしている `index.html` / `landing.html` などがどれか確認する。
2. **SD-WAN Map カードの `href` を修正**  
   - `?page=line_dashboard` → `?page=project_sd_wan`
3. **`project_sd_wan.html` が GAS に含まれているか確認**  
   - `Code.js` の `ROUTE_MAP` に `project_sd_wan` があり、対応する `project_sd_wan.html` が同じ GAS プロジェクトに存在する必要がある。
4. **clasp push などで再デプロイ**  
   - 修正したHTMLと `project_sd_wan.html` を再デプロイする。

---

## 6. GAS 版管理で project_sd_wan を過去バージョンに戻す

GAS プロジェクトは clasp の **バージョン管理** されている。  
横並び版などを探す場合や、「一個のチャート＋ボタン」版に戻したい場合は、**過去バージョンを pull** すればよい。

### 手順

1. **clasp プロジェクトのルートへ移動**  
   - `Internal_DX_Portal` など、`.clasp.json` があるディレクトリ。

2. **保存済みバージョン一覧を確認**
   ```powershell
   clasp versions
   ```
   - 番号と説明が表示される。戻したい時期のバージョン番号を控える。

3. **そのバージョンの内容をローカルに取得**
   ```powershell
   clasp pull --versionNumber <バージョン番号>
   ```
   - 指定したバージョン時点の GAS ファイルで、ローカルが**上書き**される。

4. **必要なファイルだけ使う**  
   - `project_sd_wan.html` だけ使いたい場合は、pull 後にそのファイルを  
     `local_preview` やデプロイ元にコピーするなどして利用。

### 注意

- `clasp pull` は **[[プロジェクト全体]]** を上書きする。  
  戻す前に `clasp push` で未プッシュの変更がないか確認し、  
  必要なものは別フォルダに退避しておく。
- 組織アカウント（akiba-holdings.co.jp）で `clasp login` 済みであること。

---

## 7. まとめ

- **正しい資料**: `project_sd_wan.html`（`?page=project_sd_wan`）
- **修正すべきリンク**: SD-WAN Map ボタン → `?page=project_sd_wan` に統一
- ローカルでは既に `project_sd_wan` にしているファイルが多いため、**本番デプロイ元**のHTMLを確認・修正するのがポイント。
- **版を戻したいとき**: GAS 側の版管理 → `clasp versions` → `clasp pull --versionNumber N` で過去の `project_sd_wan.html` を取得できる。

---

## 8. 本番ですぐ確認する：GAS 手動反映チェックリスト

`clasp push` が失敗する場合、**GAS エディタで直接編集 → 新バージョンデプロイ** で本番反映する。

### Step 1: Code.js

1. [script.google.com](https://script.google.com) でプロジェクトを開く。
2. 左一覧で **Code.js** を開く。
3. **ROUTE_MAP** の `'project_sd_wan': { ... },` の**直下**に次の 1 行があるか確認：
   ```js
   'line_dashboard': { template: 'project_sd_wan', title: 'SD-WAN Comparison' },
   ```
4. なければ追加して **Ctrl+S** で保存。

### Step 2: project_sd_wan.html（横並び版）

1. 左一覧で **project_sd_wan.html** を開く。
2. 中身を **横並び版** に差し替える。
   - ローカル原稿: `Internal_DX_Portal\project_sd_wan.html` または `_versions\v246\project_sd_wan.html`
   - 全選択 → 削除 → 上記ファイルの内容をコピー＆ペースト。
3. **Ctrl+S** で保存。

### Step 3: 新バージョンでデプロイ

1. 右上 **「デプロイ」** → **「デプロイを管理」**。
2. 本番 Web アプリ（`exec` の URL）の **歯車アイコン「編集」**。
3. **「バージョン」** で **「新バージョン」** を選択。
4. 説明例: `line_dashboard→SD-WAN振り向け + project_sd_wan横並び`
5. **「デプロイ」** をクリック。

### Step 4: 本番で確認

- 次の URL を開く（`?page=line_dashboard` を付ける）:
  ```
  https://script.google.com/a/akiba-holdings.co.jp/macros/s/AKfycbzubD24U27_X6_SREm4vqrPl5fVs8fmzvW1pGjaKXzyV1lJ_cVv66akCpvwEJHXO71XFQ/exec?page=line_dashboard
  ```
- **「SD-WAN 3シナリオ比較」** の横並び図（Current / Future）が表示されれば OK。
- まだ「回線インフラ速度改善ダッシュボード」なら、デプロイのバージョンが古いか、Step 1〜3 のどれかが未反映。
