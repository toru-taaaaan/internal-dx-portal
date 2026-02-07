# Internal DX Portal - ローカルプレビューサーバー
# 使用方法: .\dev_preview.ps1 [ファイル名]

param(
    [string]$File = ""
)

Write-Host "🌐 Internal DX Portal ローカルプレビューサーバー" -ForegroundColor Cyan
Write-Host ""

# 現在のディレクトリを取得
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# リンク変換モジュールをインポート
$modulePath = Join-Path $scriptDir "Convert-Links.psm1"
if (Test-Path $modulePath) {
    Import-Module $modulePath -Force
} else {
    Write-Host "⚠ Convert-Links.psm1 が見つかりません。基本的な変換を使用します。" -ForegroundColor Yellow
}

# GASテンプレート構文をローカル用に変換する関数
function Convert-GasTemplate {
    param([string]$content)
    
    if (Get-Command Convert-GasTemplateForLocal -ErrorAction SilentlyContinue) {
        return Convert-GasTemplateForLocal -content $content
    }
    
    # フォールバック: 基本的な変換
    # <? var url = ScriptApp.getService().getUrl(); ?> を削除
    $content = $content -replace '<\? var url = ScriptApp\.getService\(\)\.getUrl\(\); \?>', ''
    
    # <?=url?>?page=xxx を適切なHTMLファイル名に変換
    # 重要: 先に<?=url?>?page=xxxの形式を処理
    $content = $content -replace '<\?=\s*url\s*\?>\s*\?page=([^"&>\s]+)', {
        param($match)
        $pageId = $match.Groups[1].Value
        # 基本的なマッピング
        $mapping = @{
            'home' = 'index.html'
            'landing' = 'landing.html'
            'project_15.01_ADクラウド化' = 'project_15_01.html'
            'project_15.01_entraid_proposal' = 'project_15_01_entraid_proposal.html'
        }
        if ($mapping.ContainsKey($pageId)) {
            return $mapping[$pageId]
        }
        # デフォルト: pageId.html
        return "$pageId.html"
    }
    
    # <?=url?> 単体を削除
    $content = $content -replace '<\?=url\?>', ''
    
    # その他のGAS構文をコメントアウト
    $content = $content -replace '<\?[^>]*\?>', '<!-- GAS template removed for local preview -->'
    
    return $content
}

# HTMLファイルを処理してローカルプレビュー用に変換
function Process-HtmlFile {
    param([string]$filePath)
    
    $content = Get-Content -Path $filePath -Raw -Encoding UTF8
    $processedContent = Convert-GasTemplate -content $content
    
    $fileName = Split-Path -Leaf $filePath
    $outputPath = Join-Path "local_preview" $fileName
    
    $processedContent | Out-File -FilePath $outputPath -Encoding UTF8 -NoNewline
    Write-Host "✓ 処理完了: $fileName -> local_preview/$fileName" -ForegroundColor Green
    
    return $outputPath
}

# local_previewディレクトリを作成
if (-not (Test-Path "local_preview")) {
    New-Item -ItemType Directory -Path "local_preview" | Out-Null
    Write-Host "✓ local_previewディレクトリを作成しました" -ForegroundColor Green
}

# assetsディレクトリをコピー
if (Test-Path "assets") {
    if (Test-Path "local_preview\assets") {
        Remove-Item "local_preview\assets" -Recurse -Force
    }
    Copy-Item -Path "assets" -Destination "local_preview\assets" -Recurse -Force
    Write-Host "✓ assetsディレクトリをコピーしました" -ForegroundColor Green
}

# すべてのHTMLファイルを処理
Write-Host "📝 HTMLファイルを処理中..." -ForegroundColor Yellow
Get-ChildItem -Path "." -Filter "*.html" | Where-Object { $_.Name -notlike "*backup*" } | ForEach-Object {
    Process-HtmlFile -filePath $_.FullName
}

Write-Host ""

# 指定されたファイルがあれば、それを開く
$targetFile = ""
if ($File -ne "") {
    $targetFile = Join-Path "local_preview" $File
    if (-not (Test-Path $targetFile)) {
        Write-Host "⚠ ファイルが見つかりません: $targetFile" -ForegroundColor Yellow
        $targetFile = ""
    }
}

# Python HTTPサーバーを起動
Write-Host "🚀 ローカルサーバーを起動中..." -ForegroundColor Yellow
Write-Host "   URL: http://localhost:8000" -ForegroundColor Cyan
Write-Host "   停止するには Ctrl+C を押してください" -ForegroundColor Gray
Write-Host ""

if ($targetFile -ne "") {
    # 指定されたファイルをブラウザで開く（エラーハンドリング付き）
    Start-Sleep -Seconds 2
    $url = "http://localhost:8000/$($File)"
    try {
        # より安全な方法でブラウザを開く
        $browser = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe' -ErrorAction SilentlyContinue
        if ($browser) {
            Start-Process -FilePath $browser.'(default)' -ArgumentList $url -ErrorAction SilentlyContinue
        } else {
            # デフォルトブラウザを使用
            Start-Process $url -ErrorAction SilentlyContinue
        }
        Write-Host "✓ ブラウザで開きました: $url" -ForegroundColor Green
        Write-Host "   手動で開く場合: $url" -ForegroundColor Gray
    } catch {
        Write-Host "⚠ ブラウザの自動起動に失敗しました" -ForegroundColor Yellow
        Write-Host "   手動で以下のURLを開いてください: $url" -ForegroundColor Cyan
    }
    Write-Host ""
}

# Python HTTPサーバーを起動（local_previewディレクトリで）
Set-Location "local_preview"
python -m http.server 8000