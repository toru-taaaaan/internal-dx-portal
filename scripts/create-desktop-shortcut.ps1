# Claude Code - Portal 起動ショートカット作成

$DesktopPath = [Environment]::GetFolderPath("Desktop")
$ShortcutPath = "$DesktopPath\Claude Code - Portal.lnk"
$TargetPath = "C:\Windows\System32\cmd.exe"
$Arguments = "/c `"cd C:\Users\toru.tanji\Projects\portal && claude`""

$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $TargetPath
$Shortcut.Arguments = $Arguments
$Shortcut.WorkingDirectory = "C:\Users\toru.tanji\Projects\portal"
$Shortcut.Description = "Claude Code - Portal プロジェクト起動"
$Shortcut.Save()

Write-Host "✅ デスクトップにショートカット作成完了"
Write-Host "   場所: $ShortcutPath"
