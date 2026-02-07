# Internal DX Portal - ローカル開発用リンク変換スクリプト
# GASのROUTE_MAPに基づいて、ローカル用のリンクに変換します

# GASのROUTE_MAPに対応するマッピング
# Code.jsのROUTE_MAPを参照して作成（完全一致）
$script:ROUTE_MAP = @{
    'home' = 'index.html'
    'landing' = 'landing.html'
    'project_15_12_ishii' = 'project_15_12_ishii.html'
    'project_15_12_proposal' = 'project_15_12_proposal.html'
    'project_15_12_antigravity' = 'project_15_12_antigravity.html'
    'project_buddynet' = 'project_buddynet.html'
    'project_sd_wan' = 'project_sd_wan.html'
    'project_15.12_AIチャンピオン推進' = 'project_15_12.html'
    'project_15.14_現状インフラ評価' = 'project_15_14.html'
    'project_15.01_ADクラウド化' = 'project_15_01.html'
    'project_15.02_セコム入退室クラウド化' = 'project_15_02.html'
    'project_15.03_ネットワークインフラ刷新' = 'project_15_03.html'
    # 新規追加
    'project_15.01_entraid_proposal' = 'project_15_01_entraid_proposal.html'
    # index.htmlで使用されているページID
    'executive_hub' = 'executive_hub.html'
    'infrastructure_strategy' = 'infrastructure_strategy.html'
    'line_dashboard' = 'line_dashboard.html'
    'bcp_risk_matrix' = 'bcp_risk_matrix.html'
    'project_ad_scenarios' = 'project_ad_scenarios.html'
    'project_ad_matrix' = 'project_ad_matrix.html'
    'evaluation_sheet' = 'evaluation_sheet.html'
    'daily_log' = 'daily_log.html'
    'meeting_minutes_20260123' = 'meeting_minutes_20260123.html'
    'project_ad_scenarios' = 'project_ad_scenarios.html'
    'project_ad_matrix' = 'project_ad_matrix.html'
}

# ページIDからHTMLファイル名に変換する関数
function Convert-PageIdToHtml {
    param([string]$pageId)
    
    # ROUTE_MAPに存在する場合はそれを使用
    if ($script:ROUTE_MAP.ContainsKey($pageId)) {
        return $script:ROUTE_MAP[$pageId]
    }
    
    # 動的ルーティング: project_15.XX や project_15_XX の形式
    if ($pageId -match '^project_15[._](\d+)') {
        $num = $matches[1]
        # 既存のファイル名パターンに合わせる
        $candidates = @(
            "project_15_$num.html",
            "project_15.$num.html"
        )
        # 実際に存在するファイルを確認
        foreach ($candidate in $candidates) {
            if (Test-Path $candidate) {
                return $candidate
            }
        }
    }
    
    # デフォルト: pageIdをそのままHTMLファイル名として使用
    if ($pageId -notmatch '\.html$') {
        return "$pageId.html"
    }
    return $pageId
}

# GASテンプレート構文をローカル用に変換する関数（改善版）
function Convert-GasTemplateForLocal {
    param([string]$content)
    
    # <? var url = ScriptApp.getService().getUrl(); ?> を削除
    $content = $content -replace '<\? var url = ScriptApp\.getService\(\)\.getUrl\(\); \?>', ''
    
    # 重要: href="..."内の<?=url?>?page=xxx の形式を処理
    # href="<?=url?>?page=xxx" を href="xxx.html" に変換
    $content = $content -replace 'href="<\?=\s*url\s*\?>\s*\?page=([^"]+)"', {
        param($match)
        try {
            $pageId = $match.Groups[1].Value
            $htmlFile = Convert-PageIdToHtml -pageId $pageId
            return "href=`"$htmlFile`""
        } catch {
            return 'href="#"'
        }
    }
    
    # <?=url?>?page=xxx の形式を処理（href="..."の外側にある場合）
    $content = $content -replace '<\?=\s*url\s*\?>\s*\?page=([^"&>\s]+)', {
        param($match)
        try {
            $pageId = $match.Groups[1].Value
            $htmlFile = Convert-PageIdToHtml -pageId $pageId
            return $htmlFile
        } catch {
            return '#'
        }
    }
    
    # <?=url?> 単体を削除（空リンクになるのを防ぐ）
    # 注意: これは上記の処理の後で実行する必要がある
    $content = $content -replace '<\?=\s*url\s*\?>', ''
    
    # その他のGAS構文をコメントアウト（<?=url?>?page=xxx以外）
    # ただし、既に処理済みのものは除外
    $content = $content -replace '<\?[^=][^>]*\?>', '<!-- GAS template removed for local preview -->'
    
    # .htmlという空のリンクを修正（href=".html"を削除または修正）
    # これは変換エラーを防ぐため
    $content = $content -replace 'href="\.html"', 'href="#"'
    
    return $content
}

# エクスポート
Export-ModuleMember -Function Convert-GasTemplateForLocal, Convert-PageIdToHtml