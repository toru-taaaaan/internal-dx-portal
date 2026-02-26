@echo off
cd /d C:\Users\toru.tanji\internal-dx-portal
git add src/compass.md
git commit -m "Compass URL を /compass/ に統一" -m "Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
git push origin main
echo.
echo 完了！Compassページを確認してください。
pause
