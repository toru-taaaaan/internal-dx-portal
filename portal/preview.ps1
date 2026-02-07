# Internal DX Portal - 単一ファイルプレビュー
# 使用方法: .\preview.ps1 project_15_01_entraid_proposal.html

param(
    [Parameter(Mandatory=$true)]
    [string]$File
)

Write-Host "👁️  ファイルプレビュー: $File" -ForegroundColor Cyan
Write-Host ""

# ファイルの存在確認
if (-not (Test-Path $File)) {
    Write-Host "❌ ファイルが見つかりません: $File" -ForegroundColor Red
    exit 1
}

# リンク変換モジュールをインポート
$modulePath = Join-Path $PSScriptRoot "Convert-Links.psm1"
if (Test-Path $modulePath) {
    Import-Module $modulePath -Force
} else {
    Write-Host "⚠ Convert-Links.psm1 が見つかりません。基本的な変換を使用します。" -ForegroundColor Yellow
}

# GASテンプレート構文をローカル用に変換
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

# 一時ディレクトリの作成
$tempDir = "local_preview"
if (-not (Test-Path $tempDir)) {
    New-Item -ItemType Directory -Path $tempDir | Out-Null
}

# HTMLファイルを処理
$content = Get-Content -Path $File -Raw -Encoding UTF8
$processedContent = Convert-GasTemplate -content $content

$fileName = Split-Path -Leaf $File
$outputPath = Join-Path $tempDir $fileName

$processedContent | Out-File -FilePath $outputPath -Encoding UTF8 -NoNewline

# ファイルが正しく作成されたか確認
if (-not (Test-Path $outputPath)) {
    Write-Host "❌ ファイルの作成に失敗しました: $outputPath" -ForegroundColor Red
    exit 1
}

Write-Host "✓ ファイルを処理しました: $outputPath" -ForegroundColor Green
Write-Host ""

# ブラウザで開く（エラーハンドリング付き）
try {
    # 絶対パスを取得
    $absolutePath = (Resolve-Path $outputPath).Path
    $fileUri = "file:///$($absolutePath -replace '\\', '/')"
    
    Write-Host "📂 ファイルパス: $absolutePath" -ForegroundColor Gray
    
    # より安全な方法でブラウザを開く
    $browser = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe' -ErrorAction SilentlyContinue
    if ($browser) {
        Start-Process -FilePath $browser.'(default)' -ArgumentList $fileUri -ErrorAction SilentlyContinue
    } else {
        # デフォルトブラウザを使用
        Start-Process $fileUri -ErrorAction SilentlyContinue
    }
    Write-Host "✓ ブラウザで開きました" -ForegroundColor Green
} catch {
    Write-Host "⚠ ブラウザの自動起動に失敗しました" -ForegroundColor Yellow
    Write-Host "   手動で以下のファイルを開いてください:" -ForegroundColor Cyan
    Write-Host "   $absolutePath" -ForegroundColor White
    Write-Host "   または、以下のURLをブラウザに貼り付けてください:" -ForegroundColor Cyan
    Write-Host "   $fileUri" -ForegroundColor White
}

Write-Host ""
Write-Host "💡 ヒント: ファイルを編集したら、再度このスクリプトを実行してください" -ForegroundColor Gray