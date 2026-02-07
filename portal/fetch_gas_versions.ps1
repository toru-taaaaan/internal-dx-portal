# GAS 過去バージョンを取得し _versions に保存する
# 使い方: .\fetch_gas_versions.ps1
# 前提: cd Internal_DX_Portal で clasp login 済み

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$versions = @( 185, 187, 188, 224, 229, 246 )

$outDir = Join-Path $scriptDir "_versions"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

foreach ($v in $versions) {
    Write-Host "`n--- Pulling version $v ---" -ForegroundColor Cyan
    try {
        npx clasp pull --versionNumber $v 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "exit $LASTEXITCODE" }
    } catch {
        Write-Host "  clasp pull v$v failed, skipping." -ForegroundColor Yellow
        continue
    }

    $vDir = Join-Path $outDir "v$v"
    if (Test-Path $vDir) { Remove-Item $vDir -Recurse -Force }
    New-Item -ItemType Directory -Path $vDir | Out-Null

    @("Code.js", "appsscript.json") | ForEach-Object {
        if (Test-Path $_) { Copy-Item $_ -Destination $vDir -Force }
    }
    Get-ChildItem -Filter "*.html" | ForEach-Object {
        Copy-Item $_.FullName -Destination $vDir -Force
    }
    if (Test-Path "assets") {
        $a = Join-Path $vDir "assets"
        if (-not (Test-Path $a)) { New-Item -ItemType Directory -Path $a | Out-Null }
        Copy-Item "assets\*" -Destination $a -Recurse -Force -ErrorAction SilentlyContinue
    }

    Write-Host "  Saved to _versions\v$v" -ForegroundColor Green
}

Write-Host "`n--- Restoring latest (HEAD) ---" -ForegroundColor Cyan
npx clasp pull 2>&1 | Out-Null
Write-Host "Done. Check _versions\v1, v30, v55, v182, v185, v188" -ForegroundColor Green
