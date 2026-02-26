#!/usr/bin/env pwsh

# Compass URL修正をコミット・プッシュ
Write-Host "🚀 Compassコミット・プッシュ開始..." -ForegroundColor Cyan

# 現在のディレクトリを確認
$currentPath = Get-Location
Write-Host "📁 作業ディレクトリ: $currentPath" -ForegroundColor Gray

# git add
Write-Host "📝 git add 実行中..." -ForegroundColor Yellow
git add src/compass.md
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ git add 完了" -ForegroundColor Green
} else {
    Write-Host "❌ git add 失敗" -ForegroundColor Red
    exit 1
}

# git commit
Write-Host "💾 git commit 実行中..." -ForegroundColor Yellow
git commit -m "Compass URL を /compass/ に統一 (permalink修正)" -m "Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ git commit 完了" -ForegroundColor Green
} else {
    Write-Host "❌ git commit 失敗" -ForegroundColor Red
    exit 1
}

# git push
Write-Host "🌐 git push 実行中..." -ForegroundColor Yellow
git push
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ git push 完了" -ForegroundColor Green
    Write-Host "" -ForegroundColor Cyan
    Write-Host "🎉 成功！ 1-3分でCompassページが復活します。" -ForegroundColor Cyan
    Write-Host "   URL: https://internal-dx-portal-auth.tanjiadm.workers.dev/compass/" -ForegroundColor Cyan
} else {
    Write-Host "❌ git push 失敗" -ForegroundColor Red
    exit 1
}
