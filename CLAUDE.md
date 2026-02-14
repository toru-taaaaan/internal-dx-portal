# AKIBAホールディングス DXポータル

## プロジェクト概要
社内向けDXポータルサイト
完成資料: 11ファイル（全HTML）

## 会社名表記ルール
- 正式名称: AKIBAホールディングス
- ❌NG表記: アキバ、akiba、秋葉
- 必ず「AKIBA」は大文字、「ホ」はカタカナ

## トーンマナー（超重要）

### 禁止表現
- 絵文字: 💡（セクションタイトル以外は禁止）
- カタカナ: 可視化、戦略的、インサイト、シームレス、ボトルネック
- 誇張: 圧倒的、莫大、唯一、根本から、革新的
- 比喩: 牙を剥き、ホテル/マンション/コンシェルジュ

### 推奨表現
- 体言止め: 「～されます」→「～する」「～予定」
- 簡潔・中立・事実ベース
- 対象読者: 50-60代の部長クラス

## ファイル配置ルール
- HTMLファイルはルートと portal/ の両方に配置
- Cloudflare Workers対応のため

## Git運用
- コミットメッセージ: 簡潔に（1行）
- Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> を必ず付ける

## デプロイ
- git push で自動デプロイ（GitHub Actions）
- URL: https://internal-dx-portal-auth.tanjiadm.workers.dev/
- 確認: 1-3分待ってブラウザで開く

## 作業の流れ
1. 禁止ワードチェック（最優先）
2. 修正
3. git add .
4. git commit -m "メッセージ"
5. git push

## 完成資料リスト（全11ファイル）
1. SECOM入退室クラウド化_導入検討資料.html
2. AD・SECOM同時依頼_コスト最適化分析.html
3. ADクラウド化_3社権限・責任分界点.html
4. ADクラウド移行_3社比較・導入計画.html
5. bcp_risk_matrix.html
6. sdwan_scope_definition.html
7. Phase2_刷新戦略・工程統合ボード.html
8. Phase2_全体工程・タスク管理表.html
9. SD-WAN刷新_3社4シナリオ比較検討資料.html
10. AD・EntraID刷新_移行シナリオ比較検討資料.html
11. Phase2_刷新戦略ボード_地図と物語.html

## エビデンス管理
- 場所: .claude/projects/C--Users-toru-tanji/memory/AD_3社比較_エビデンス一覧.md

## 未確認事項（ベンダー問い合わせ中）
1. USEN: 緊急パッチ対応詳細
2. Link-At-Japan: SLA（稼働率保証）
3. Cato: Azure/AWSへのSocket設置方法
4. IIJ/Cato: モバイルアクセスライセンス形態
