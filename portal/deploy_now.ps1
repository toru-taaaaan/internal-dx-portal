# GAS 本番へ即時デプロイ (Auto-Rotation & Deploy)
# 使い方: .\deploy_now.ps1
# 機能:
# 1. バージョン数が上限に近い場合、古いバージョンを自動削除
# 2. clasp push -f
# 3. clasp version
# 4. clasp redeploy

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# --- Configuration ---
$MAX_VERSIONS = 150        # Keep buffer below 200
$DELETE_COUNT = 20         # How many to delete when limit hit
$CLASP_JSON = ".clasp.json"
$CLASPRC_JSON = "$env:USERPROFILE\.clasprc.json"

# --- Helper Functions ---
function Get-AccessToken {
    if (-not (Test-Path $CLASPRC_JSON)) { throw ".clasprc.json not found at $CLASPRC_JSON" }
    $creds = Get-Content $CLASPRC_JSON -Raw | ConvertFrom-Json
    $token = $creds.tokens.default
    
    # Check expiry (epoch ms)
    $now = (Get-Date).ToUniversalTime()
    $epoch = Get-Date "1970-01-01 00:00:00Z"
    $expiry = $epoch.AddMilliseconds($token.expiry_date)
    
    if ($now -gt $expiry.AddMinutes(-5)) {
        Write-Host "  Refreshing OAuth Token..." -ForegroundColor Yellow
        $body = @{
            client_id     = $token.client_id
            client_secret = $token.client_secret
            refresh_token = $token.refresh_token
            grant_type    = "refresh_token"
        }
        try {
            $response = Invoke-RestMethod -Uri "https://oauth2.googleapis.com/token" -Method Post -Body $body
            return $response.access_token
        } catch {
            Write-Host "  Failed to refresh token: $_" -ForegroundColor Red
            throw $_
        }
    }
    return $token.access_token
}

function Rotate-Versions {
    param($scriptId, $token)
    
    $headers = @{ Authorization = "Bearer $token" }
    $listUrl = "https://script.googleapis.com/v1/projects/$scriptId/versions"
    
    try {
        $versions = (Invoke-RestMethod -Uri $listUrl -Method Get -Headers $headers).versions
    } catch {
        Write-Host "  Failed to list versions: $_" -ForegroundColor Red
        return
    }
    
    $count = $versions.Count
    Write-Host "  Current Version Count: $count" -ForegroundColor Cyan
    
    if ($count -ge $MAX_VERSIONS) {
        # Sort by versionNumber (ascending) to find oldest
        $sorted = $versions | Sort-Object versionNumber
        $toDelete = $sorted | Select-Object -First $DELETE_COUNT
        
        Write-Host "  Deleting $($toDelete.Count) old versions to clear space..." -ForegroundColor Yellow
        
        foreach ($v in $toDelete) {
            $delUrl = "https://script.googleapis.com/v1/projects/$scriptId/versions/$($v.versionNumber)"
            try {
                Invoke-RestMethod -Uri $delUrl -Method Delete -Headers $headers
                Write-Host "    Deleted version $($v.versionNumber)" -ForegroundColor DarkGray
            } catch {
                Write-Host "    Failed to delete $($v.versionNumber): $_" -ForegroundColor Red
            }
        }
    }
}

# --- Main Logic ---

# 1. Read Config
if (-not (Test-Path $CLASP_JSON)) { throw ".clasp.json not found." }
$claspConfig = Get-Content $CLASP_JSON -Raw | ConvertFrom-Json
$scriptId = $claspConfig.scriptId

$deployConfigPath = Join-Path $scriptDir "deploy_config.json"
if (-not (Test-Path $deployConfigPath)) { throw "deploy_config.json not found." }
$deployConfig = Get-Content $deployConfigPath -Raw | ConvertFrom-Json
$deploymentId = $deployConfig.deploymentId

Write-Host ""
Write-Host "  GAS Deploy Manager (Auto-Rotation)" -ForegroundColor Cyan
Write-Host "  Target: $scriptId" -ForegroundColor Gray
Write-Host ""

# 2. Rotate Versions
try {
    $token = Get-AccessToken
    Rotate-Versions -scriptId $scriptId -token $token
} catch {
    Write-Host "  Warning: Version rotation failed. Proceeding with deployment..." -ForegroundColor Yellow
}

# 3. Push
Write-Host "  >> clasp push -f" -ForegroundColor Gray
cmd /c "npm exec --yes -- @google/clasp push -f"
if ($LASTEXITCODE -ne 0) { exit 1 }

# 4. Version
$desc = "auto-$(Get-Date -Format 'yyyyMMdd-HHmm')"
Write-Host "  >> clasp version `"$desc`"" -ForegroundColor Gray
$vOut = cmd /c "npm exec --yes -- @google/clasp version $desc 2>&1" | Out-String
Write-Host $vOut
$ms = [regex]::Matches($vOut, '\d+')
$version = if ($ms.Count -gt 0) { $ms[-1].Value } else { $null }

if (-not $version) {
    Write-Host "  Failed to create version." -ForegroundColor Red
    exit 1
}

# 5. Redeploy
Write-Host "  >> clasp redeploy -V $version -d auto $deploymentId" -ForegroundColor Gray
cmd /c "npm exec --yes -- @google/clasp redeploy -V $version -d auto $deploymentId"
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host ""
Write-Host "  Deployment Complete (v$version)" -ForegroundColor Green
