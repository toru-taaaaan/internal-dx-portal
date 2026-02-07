#!/bin/bash

# 🎯 社内DXポータル - ファイルクリーンアップスクリプト
# 作成日: 2026-02-07
# 目的: 不要なバージョンファイルを削除し、
#      「ローカル = 本番最新版」という状態を確立する

set -e  # エラーで停止

echo "=========================================="
echo "🎯 ファイルクリーンアップ - 開始"
echo "=========================================="
echo ""

# 現在のファイル数を表示
BEFORE=$(ls -1 *.html 2>/dev/null | wc -l)
echo "📊 処理前のファイル数: $BEFORE個"
echo ""

# 削除対象ファイルのプレビュー
echo "❌ 削除対象ファイル:"
echo ""

echo "1️⃣  project_15_02 バージョンファイル（21個）"
ls -1 project_15_02_v20260121_*.html 2>/dev/null | wc -l | xargs echo "   削除予定:"
ls -1 project_15_02_backup_*.html 2>/dev/null | wc -l | xargs echo "   削除予定:"
ls -1 project_15_02_before_*.html 2>/dev/null | wc -l | xargs echo "   削除予定:"

echo ""
echo "2️⃣  project_15_combined バージョンファイル（12個）"
ls -1 project_15_combined_v20260121_*.html 2>/dev/null | wc -l | xargs echo "   削除予定:"
ls -1 project_15_combined_v20260122_*.html 2>/dev/null | wc -l | xargs echo "   削除予定:"

echo ""
echo "3️⃣  その他不要ファイル"
for file in index_old_backup.html index_new.html index_hub.html \
            _generated_css.html AccessDenied.html action_dashboard.html \
            landing_new_concept.html infrastructure_strategy.html \
            project.html project_management.html \
            project_sd_wan_backup.html project_sd_wan_v1.html; do
  if [ -f "$file" ]; then
    echo "   - $file"
  fi
done

echo ""
echo "=========================================="
echo "⚠️  確認"
echo "=========================================="
echo ""
echo "以上のファイルを削除します。よろしいですか？"
echo "(Ctrl+C で中断、Enter で継続)"
echo ""

read -p "続行しますか? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "❌ キャンセルしました。"
  exit 1
fi

echo ""
echo "=========================================="
echo "🗑️  削除を開始します..."
echo "=========================================="
echo ""

# project_15_02 削除
echo "🔄 project_15_02 バージョンファイルを削除中..."
rm -f project_15_02_v20260121_*.html
rm -f project_15_02_backup_*.html
rm -f project_15_02_before_*.html
echo "✅ project_15_02 削除完了"

# project_15_combined 削除
echo "🔄 project_15_combined バージョンファイルを削除中..."
rm -f project_15_combined_v20260121_*.html
rm -f project_15_combined_v20260122_*.html
echo "✅ project_15_combined 削除完了"

# その他削除
echo "🔄 その他不要ファイルを削除中..."
rm -f index_old_backup.html
rm -f index_new.html
rm -f index_hub.html
rm -f _generated_css.html
rm -f AccessDenied.html
rm -f action_dashboard.html
rm -f landing_new_concept.html
rm -f infrastructure_strategy.html
rm -f project.html
rm -f project_management.html
rm -f project_sd_wan_backup.html
rm -f project_sd_wan_v1.html
echo "✅ その他ファイル削除完了"

echo ""
echo "=========================================="
echo "✅ 削除完了"
echo "=========================================="
echo ""

# 削除後のファイル数を表示
AFTER=$(ls -1 *.html 2>/dev/null | wc -l)
DELETED=$((BEFORE - AFTER))

echo "📊 処理後のファイル数: $AFTER個"
echo "📉 削除したファイル: $DELETED個"
echo ""

# 最新ファイルが残っているか確認
echo "✅ 重要ファイルの確認:"
for file in index.html landing.html \
            project_15_01.html project_15_02.html project_15_combined.html \
            project_15_14.html project_15_12.html project_bn_report.html; do
  if [ -f "$file" ]; then
    echo "   ✅ $file"
  else
    echo "   ❌ $file （見つかりません！）"
  fi
done

echo ""
echo "=========================================="
echo "🎯 次のステップ:"
echo "=========================================="
echo ""
echo "1. git status で変更を確認"
echo "2. git add . && git commit -m '整理: バージョンファイル削除'"
echo "3. ./deploy_auto_v2.sh で本番環境にデプロイ"
echo "4. 本番環境ですべてのページが正常に表示されることを確認"
echo ""
echo "✅ クリーンアップスクリプト終了"
