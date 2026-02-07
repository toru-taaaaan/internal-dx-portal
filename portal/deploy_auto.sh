#!/bin/bash
# push -> version -> redeploy で既存 Web アプリを自動更新
set -e
cd "$(dirname "$0")"
CONFIG="deploy_config.json"

if [ ! -f "$CONFIG" ]; then
  echo "Error: $CONFIG not found"
  exit 1
fi
DEPLOYMENT_ID=$(node -e "console.log(require('./deploy_config.json').deploymentId)")

echo ">> clasp push -f"
npx --yes @google/clasp push -f

echo ">> clasp version"
VOUT=$(npx --yes @google/clasp version "auto-$(date +%Y%m%d-%H%M)" 2>&1)
echo "$VOUT"
VERSION=$(echo "$VOUT" | grep -oE '(Version|version) [0-9]+' | grep -oE '[0-9]+' | tail -1)
if [ -z "$VERSION" ]; then
  VERSION=$(echo "$VOUT" | grep -oE '[0-9]+' | tail -1)
fi
if [ -z "$VERSION" ]; then
  echo "Error: could not parse version from clasp version output"
  exit 1
fi

echo ">> clasp redeploy -V $VERSION -d auto $DEPLOYMENT_ID"
npx --yes @google/clasp redeploy -V "$VERSION" -d "auto" "$DEPLOYMENT_ID"

echo "Done. Web app updated to version $VERSION."
