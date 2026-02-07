# Internal DX Portal - ローカル開発環境セットアップスクリプト
# 使用方法: .\dev_setup.ps1

Write-Host "🚀 Internal DX Portal ローカル開発環境セットアップ" -ForegroundColor Cyan
Write-Host ""

# 1. ローカルプレビュー用ディレクトリの作成
$localDir = "local_preview"
if (Test-Path $localDir) {
    Write-Host "✓ local_preview ディレクトリは既に存在します" -ForegroundColor Green
} else {
    New-Item -ItemType Directory -Path $localDir | Out-Null
    Write-Host "✓ local_preview ディレクトリを作成しました" -ForegroundColor Green
}

# 2. Pythonの確認
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python が見つかりました: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "⚠ Python が見つかりません。Python 3.7以上が必要です。" -ForegroundColor Yellow
    Write-Host "  https://www.python.org/downloads/ からインストールしてください" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "セットアップ完了！" -ForegroundColor Green
Write-Host ""
Write-Host "次のコマンドでローカル開発を開始できます:" -ForegroundColor Cyan
Write-Host "  .\dev_preview.ps1" -ForegroundColor White
Write-Host ""