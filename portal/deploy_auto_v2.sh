#!/bin/bash

################################################################################
# Google Apps Script 自動デプロイスクリプト v2.0
# 改善: エラーハンドリング、ログ出力、認証キャッシュ活用
################################################################################

set -e

# 色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# スクリプト情報
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/deploy_log_$(date +%Y%m%d_%H%M%S).txt"
CONFIG_FILE="$SCRIPT_DIR/deploy_config.json"

echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}Google Apps Script デプロイ開始${NC}"
echo -e "${BLUE}================================${NC}"
echo ""

# ログ関数
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# エラーハンドリング
error_exit() {
  echo -e "${RED}エラー: $1${NC}" | tee -a "$LOG_FILE"
  exit 1
}

# Step 1: 設定ファイル確認
log "Step 1: 設定ファイルを確認中..."
if [ ! -f "$CONFIG_FILE" ]; then
  error_exit "エラー: $CONFIG_FILE が見つかりません"
fi

DEPLOYMENT_ID=$(node -e "console.log(require('./deploy_config.json').deploymentId)" 2>/dev/null) || \
  error_exit "deploy_config.json からDeployment IDの読み込みに失敗"

log "✓ Deployment ID: $DEPLOYMENT_ID"
log ""

# Step 2: ファイルをpush
log "Step 2: Google Apps Script にファイルを送信中..."
log "実行: npx @google/clasp push -f"

if npx --yes @google/clasp push -f 2>&1 | tee -a "$LOG_FILE"; then
  log "✓ Push 成功"
else
  error_exit "Push に失敗しました"
fi
log ""

# Step 3: バージョン作成
log "Step 3: バージョンを作成中..."
VERSION_NAME="auto-$(date +%Y%m%d-%H%M%S)"
log "実行: npx @google/clasp version '$VERSION_NAME'"

VOUT=$(npx --yes @google/clasp version "$VERSION_NAME" 2>&1)
echo "$VOUT" | tee -a "$LOG_FILE"

# バージョン番号を抽出
VERSION=$(echo "$VOUT" | grep -oE '(Version|version) [0-9]+' | grep -oE '[0-9]+' | tail -1)
if [ -z "$VERSION" ]; then
  VERSION=$(echo "$VOUT" | grep -oE '[0-9]+' | tail -1)
fi

if [ -z "$VERSION" ]; then
  error_exit "バージョン番号の抽出に失敗しました。Google認証が必要かもしれません。\n\n以下を実行してください:\nclasp login"
fi

log "✓ バージョン作成完了: Ver.$VERSION"
log ""

# Step 4: 本番環境にデプロイ
log "Step 4: 本番環境にデプロイ中..."
log "実行: npx @google/clasp redeploy -V $VERSION -d 'auto' $DEPLOYMENT_ID"

if npx --yes @google/clasp redeploy -V "$VERSION" -d "auto" "$DEPLOYMENT_ID" 2>&1 | tee -a "$LOG_FILE"; then
  log "✓ デプロイ成功"
else
  error_exit "デプロイに失敗しました"
fi

log ""
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}✓ デプロイ完了!${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
log "バージョン: $VERSION"
log "デプロイID: $DEPLOYMENT_ID"
log "ログファイル: $LOG_FILE"
echo ""
echo -e "${BLUE}本番環境URL:${NC}"
echo "https://script.google.com/a/akiba-holdings.co.jp/macros/s/$DEPLOYMENT_ID/exec?page=project_15_01"
echo ""

exit 0
