/**
 * フォルダ構造を修正
 */
function fixPortalStructure() {
  // 既存のフォルダを取得
  const folders = {
    private: DriveApp.getFolderById('1eBHNMp0iW-rY8bhZ6GiUaKdFY_5cRWT3'), // 10_Private_Tanji → そのまま使う
    public: DriveApp.getFolderById('1tPzaFDqmnOqiaUU4aadq1DPSlOOHk73y'),  // 01_Public → 削除予定
    nakano: DriveApp.getFolderById('1e95r0BWycx6F7JKQkqMCStJ5EzoTHHzL'), // 03_Restricted_Nakano → 01_Shared_InfoSys に変更
    ishii: DriveApp.getFolderById('1rAsvAyDWhko58SqeNJ2N0KYCmyR2FGg2')    // 02_Restricted_Ishii → 02_Shared_AIChampion に変更
  };
  
  Logger.log('=== フォルダ名変更 ===\n');
  
  // 1. フォルダ名を変更
  try {
    folders.private.setName('00_Private_Tanji');
    Logger.log('✅ 10_Private_Tanji → 00_Private_Tanji');
  } catch (e) {
    Logger.log('⚠️ Private フォルダ名変更エラー: ' + e);
  }
  
  try {
    folders.nakano.setName('01_Shared_InfoSys');
    Logger.log('✅ 03_Restricted_Nakano → 01_Shared_InfoSys');
  } catch (e) {
    Logger.log('⚠️ InfoSys フォルダ名変更エラー: ' + e);
  }
  
  try {
    folders.ishii.setName('02_Shared_AIChampion');
    Logger.log('✅ 02_Restricted_Ishii → 02_Shared_AIChampion');
  } catch (e) {
    Logger.log('⚠️ AIChampion フォルダ名変更エラー: ' + e);
  }
  
  Logger.log('\n=== ファイル移動 ===\n');
  
  // 2. ファイルを適切なフォルダに移動
  const fileMapping = {
    'landing.html': folders.private,        // トップページ → 丹治さんのみ
    'index.html': folders.private,          // プロジェクト一覧 → 丹治さんのみ
    'line_dashboard.html': folders.nakano,  // 回線ダッシュボード → 情報システム部
    'project_sd_wan.html': folders.nakano   // SD-WAN → 情報システム部
  };
  
  for (const [fileName, targetFolder] of Object.entries(fileMapping)) {
    try {
      const files = folders.public.getFilesByName(fileName);
      
      if (files.hasNext()) {
        const file = files.next();
        file.moveTo(targetFolder);
        Logger.log(`✅ ${fileName} → ${targetFolder.getName()}`);
      } else {
        Logger.log(`⚠️ ${fileName} が見つかりません`);
      }
    } catch (e) {
      Logger.log(`❌ ${fileName} 移動エラー: ${e}`);
    }
  }
  
  Logger.log('\n=== 01_Public フォルダの処理 ===');
  
  // 3. 01_Public フォルダの残りファイルを確認
  const remainingFiles = folders.public.getFiles();
  let fileCount = 0;
  
  while (remainingFiles.hasNext()) {
    const file = remainingFiles.next();
    Logger.log(`残っているファイル: ${file.getName()}`);
    fileCount++;
  }
  
  if (fileCount === 0) {
    Logger.log('01_Public フォルダは空です。手動で削除できます。');
  } else {
    Logger.log(`⚠️ 01_Public フォルダにまだ ${fileCount} 個のファイルがあります。`);
  }
  
  Logger.log('\n=== 完了 ===');
  Logger.log('checkPortalFolders() を実行して確認してください。');
  
  return {
    status: 'completed',
    message: 'フォルダ構造を修正しました'
  };
}
