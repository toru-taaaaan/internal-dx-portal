Up: [[00_INDEX]]

# クロードボット用 指示書：GAS ポータル「遷移で白画面・DNS エラー」対応

## 1. 対象プロジェクト

- **GAS Web アプリ**（Internal DX Portal / 統合指揮センター HUB）
- **ルート**: `Internal_DX_Portal/`
- **本番 URL 例**:  
  `https://script.google.com/a/akiba-holdings.co.jp/macros/s/AKfycbzubD24U27_X6_SREm4vqrPl5fVs8fmzvW1pGjaKXzyV1lJ_cVv66akCpvwEJHXO71XFQ/exec`  
  （`?page=index` 等のクエリでページ切り替え）

---

## 2. いま起きていること（再現手順・現象）

1. **ポータルを開く**  
   - 上記 URL、または `?page=index` / `?page=landing` で開く。  
   - 初回表示では問題なく出ることが多い。

2. **リンク・ボタンをクリックして遷移する**  
   - 例：index → ポータルホーム、プロジェクト、AD+SECOM、SD-WAN Map など。
   - **現象 A**: 遷移先が **真っ白** になる。
   - **現象 B**: 遷移先で **「このサイトにアクセスできません」＋ `DNS_PROBE_FINISHED_NXDOMAIN`** が出る。
   - **現象 C**: Google Drive 経由で開いていると **「現在、ファイルを開くことができません」** になることがある。

3. **白画面のときにリロード（F5 / Ctrl+R）する**  
   - **遷移先ではなく、遷移元（前の画面）に戻る** ように見える。

4. **環境**  
   - **Chrome / Edge** の通常ブラウザで発生。  
   - 「普通のブラウザだとだめ」との報告あり。

---

## 3. 既にやったこと（変えずに維持すること）

- **デプロイ**  
  - `deploy_now.ps1` で `clasp push` → `clasp version` → `clasp redeploy` を実行。  
  - 対象は `deploy_config.json` の `deploymentId`。
- **ルーティング**  
  - `doGet` で `e.parameter.page` を見て `resolveRoute` し、`ROUTE_MAP` で `template` / `handler` を決定。
- **index / landing 等**  
  - テンプレート評価を使わず、`serveRawWithCss` で HTML をそのまま返し、CSS のみインライン化。
- **リンク**  
  - `foo.html` → `?page=foo` に書き換え。  
  - 絶対 URL 化のために `ScriptApp.getService().getUrl()` で base を取得し、  
    `href="<base>?page=..."` にしている。  
  - `target="_top"` は **付けていない**（Drive で「ファイルを開けません」になるため外した）。
- **外部依存の削除**  
  - Tailwind CDN・Google Fonts の `<script>` / `<link>` を配信時に除去。  
  - `_generated_css` に Tailwind 相当のユーティリティを追加してレイアウトを維持。
- **SD-WAN / AD+SECOM**  
  - `line_dashboard` → `project_sd_wan`、`infrastructure_strategy` → `project_15_combined` に紐づけ済み。

これらは **既存の挙動・仕様** として触らないこと。

---

## 4. キーファイルと役割

| ファイル | 役割 |
|----------|------|
| `Code.js` | `doGet`、`resolveRoute`、`serveRawWithCss`、`createAccessibleHtml`、`processHtmlContent` など。ルーティング・HTML 生成の中心。 |
| `deploy_now.ps1` | ローカルデプロイ用。`clasp push` → version → redeploy。 |
| `deploy_config.json` | `deploymentId` を保持。デプロイ対象の Web アプリ ID。 |
| `_generated_css.html` | インライン用 CSS。`serveRawWithCss` が `portal_nexus.css` の代わりに差し込む。 |
| `index.html` / `landing.html` | トップ・ナビ等。リンクは `?page=...` 形式。 |

---

## 5. やってほしいこと（優先順）

### 5.1 切り分け（原因の特定）

1. **白画面**  
   - クリック遷移時のみ白いのか、直で `.../exec?page=○○` を開いても白いのかを分ける。  
   - 直で開くと出る → その `page` の生成ロジック or テンプレートの問題。  
   - クリック時のみ → リンクの URL や遷移の仕方（iframe / 別タブ等）の可能性。
2. **`DNS_PROBE_FINISHED_NXDOMAIN`**  
   - エラーになっている **実際のリクエスト URL** を確認する。  
     - アドレスバーに乗っている URL そのものか、  
     - リンクの `href` が別のドメイン・ typo になっていないか。  
   - `ScriptApp.getService().getUrl()` が空・undefined になって `href="?page=..."` のようになっており、相対 URL がおかしいドメインに解決されていないか。
3. **「リロードすると前の画面に戻る」**  
   - リロード時は **本当に同じ URL の再読込** か、  
   - ヒストリーで「戻る」になっている等、別のナビゲーションになっていないかを分ける。  
   - 同一 URL 再読込で戻るなら、**サーバー側で Referer や何かで出し分けしている**可能性もあるので、`doGet` まわりを疑う。

### 5.2 修正案（切り分け結果に応じて検討）

- **絶対 URL の生成ミス**  
  - `base` が空のときのフォールバック、  
  - `base` の末尾 `?` の有無、  
  - リンク書き換えの正規表現で `base` が正しくはりついているか。
- **`getUrl()` の取り方**  
  - `doGet` で受け取る `ScriptApp.getService().getUrl()` と、  
    `serveRawWithCss` 内で改めて呼ぶ場合で、  
    実行コンテキストが違うと値が変わる可能性がある。  
  - 必要なら `resolveRoute` に `currentUrl` を渡し、`serveRawWithCss` ではそれを使うなど一か所に寄せる。
- **リンクの `target`**  
  - `target="_top"` は一度外している。  
  - Drive 嵌入等の環境を変えずに、別の `target` や `rel` で挙動を変えられないか検討（やりすぎ注意）。
- **iframe 経由での遷移**  
  - GAS の実行環境が iframe の場合、  
    「クリックで遷移すると白／DNS エラー」が iframe 内ナビゲーションに起因していないか。

### 5.3 検証してほしいポイント

- 直アクセス:  
  `.../exec`、`.../exec?page=index`、`.../exec?page=landing`、  
  `?page=line_dashboard`、`?page=project_15_combined` などが **全て** 正常に表示されるか。
- クリック遷移:  
  index → ポータルホーム / プロジェクト / AD+SECOM / SD-WAN 等、  
  主要リンクをクリックした先が **白画面・DNS エラー・Drive エラーにならない**か。
- リロード:  
  「白画面」の状態でリロードしたときに、  
  **同じ page が再度表示されるか**（「前の画面に戻る」にならないか）。

---

## 6. デプロイ手順（変更を反映するとき）

```powershell
cd "c:\Users\toru.tanji\Documents\SecondBrain_Final\Internal_DX_Portal"
.\deploy_now.ps1
```

- 成功すると `clasp version` でバージョンが上がり、  
  `deploy_config.json` の `deploymentId` の Web アプリが更新される。  
- 確認は **本番 URL**（上記 `.../exec`）で、**Ctrl+Shift+R** でスーパーリロードしてから実施すること。

---

## 7. 注意事項

- **`deploy_config.json` の `deploymentId`** は、ユーザーが実際に使っている Web アプリの ID に合わせてある。  
  別の Web アプリに切り替える場合だけ書き換える。通常は変更しない。
- **`target="_top"`** は、Drive で「ファイルを開けません」になるため外してある。  
  再導入する場合は、Drive 経由アクセスでの影響を必ず確認すること。
- **Tailwind CDN / Google Fonts** は、Chrome・Edge でブロックされて白画面要因になり得るため除去済み。  
  復活させる場合は、同様の事象が再発しないか検証すること。

---

## 8. 完了報告に含めること

- どの切り分けで **原因** と判断したか（直アクセス vs クリック、DNS エラー時の実際の URL 等）。
- どのファイルをどう変えたか（該当箇所の抜粋で可）。
- 上記 5.3 の検証結果（直アクセス・クリック遷移・リロード）を簡単にまとめる。

---

以上を読んだうえで、**クリック遷移時の白画面・DNS エラー・「リロードで前の画面に戻る」** を解消する作業を進めてください。
