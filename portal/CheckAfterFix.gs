/**
 * フォルダ構造を確認するスクリプト（修正版）
 */
function checkPortalFoldersAfterFix() {
  const folderId = '1p76iAWhh1EUjzo2XEQMh9XseW1oeDgH1';
  
  try {
    const parentFolder = DriveApp.getFolderById(folderId);
    
    Logger.log('=== 修正後のフォルダ構造 ===');
    Logger.log('親フォルダ: ' + parentFolder.getName());
    Logger.log('');
    
    // サブフォルダを列挙
    const subFolders = parentFolder.getFolders();
    
    while (subFolders.hasNext()) {
      const folder = subFolders.next();
      Logger.log('📁 ' + folder.getName() + ' (ID: ' + folder.getId() + ')');
      
      // ファイルを列挙
      const files = folder.getFiles();
      let fileCount = 0;
      while (files.hasNext()) {
        const file = files.next();
        Logger.log('   - ' + file.getName());
        fileCount++;
      }
      
      if (fileCount === 0) {
        Logger.log('   (空のフォルダ)');
      }
      
      Logger.log('');
    }
    
    Logger.log('=== 完了 ===');
    
  } catch (e) {
    Logger.log('エラー: ' + e.toString());
  }
}
