# 確認用：GAS に push だけする（バージョンは作らない・本番は触らない）
# 使い方: .\push_only.ps1
# 前提: clasp login 済み、このフォルダが clasp プロジェクトルート
# 目的: ローカルの変更を GAS に送り、「テスト用URL」で確認するだけ。本番反映はしない。
# 所要時間: 数十秒〜1分程度（deploy_now.ps1 より短い）

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host ""
Write-Host "  確認用 push（バージョン作成なし・本番はそのまま）" -ForegroundColor Cyan
Write-Host "  Internal_DX_Portal -> GAS に送るだけ" -ForegroundColor Gray
Write-Host ""

Write-Host "  >> clasp push -f" -ForegroundColor Gray
cmd /c "npm exec --yes -- @google/clasp push -f"
if ($LASTEXITCODE -ne 0) {
    Write-Host "  clasp push に失敗しました。" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "  push 完了。テスト用URL（HEAD）で内容を確認してください。" -ForegroundColor Green
Write-Host "  本番に反映するときは deploy_now.ps1 を実行してください。" -ForegroundColor Gray
Write-Host ""
