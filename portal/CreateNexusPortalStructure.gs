/**
 * Nexus_Portal フォルダ構成を Google Drive に一から作成する
 *
 * 実行: createNexusPortalInDrive() を GAS エディタで実行
 * 結果: マイドライブ直下に Nexus_Portal が作成され、その中にサブフォルダができる
 * 作成後はログにフォルダIDを出力するので、必要ならメモして FixStructure 等で使える
 */
function createNexusPortalInDrive() {
  const root = DriveApp.getRootFolder(); // マイドライブ直下
  const mainName = 'Nexus_Portal';

  // 既に同名フォルダがある場合はスキップ or エラー（重複防止）
  const existing = root.getFoldersByName(mainName);
  if (existing.hasNext()) {
    const existingFolder = existing.next();
    Logger.log('既に Nexus_Portal が存在します: %s', existingFolder.getId());
    Logger.log('新規作成をやめる場合はこの関数の実行を止めてください。上書きはしません。');
    return { status: 'already_exists', folderId: existingFolder.getId() };
  }

  const main = root.createFolder(mainName);
  const f00 = main.createFolder('00_Private_Tanji');
  const f01 = main.createFolder('01_Public');
  const f01Assets = f01.createFolder('assets');
  const f02 = main.createFolder('02_Shared_AIChampion');
  const f03 = main.createFolder('03_Shared_InfoSys');

  Logger.log('=== Nexus_Portal 作成完了 ===');
  Logger.log('Nexus_Portal (ルート): %s', main.getId());
  Logger.log('00_Private_Tanji: %s', f00.getId());
  Logger.log('01_Public: %s', f01.getId());
  Logger.log('01_Public/assets: %s', f01Assets.getId());
  Logger.log('02_Shared_AIChampion: %s', f02.getId());
  Logger.log('03_Shared_InfoSys: %s', f03.getId());
  Logger.log('=== 以上をメモして FixStructure や Code.js で使えます ===');

  return {
    status: 'created',
    rootId: main.getId(),
    ids: {
      '00_Private_Tanji': f00.getId(),
      '01_Public': f01.getId(),
      '01_Public/assets': f01Assets.getId(),
      '02_Shared_AIChampion': f02.getId(),
      '03_Shared_InfoSys': f03.getId()
    }
  };
}
