const { execSync } = require('child_process');
const path = require('path');

const repoPath = 'C:\\Users\\toru.tanji\\internal-dx-portal';
process.chdir(repoPath);

try {
  console.log('📝 git add 実行中...');
  execSync('git add src/compass.md', { encoding: 'utf-8' });
  console.log('✅ git add 完了');

  console.log('💾 git commit 実行中...');
  execSync('git commit -m "Compass URL を /compass/ に統一"', { encoding: 'utf-8' });
  console.log('✅ git commit 完了');

  console.log('🌐 git push 実行中...');
  execSync('git push origin main', { encoding: 'utf-8' });
  console.log('✅ git push 完了');

  console.log('\n🎉 成功！ Compassページが復活します。');
  console.log('   URL: https://internal-dx-portal-auth.tanjiadm.workers.dev/compass/');
} catch (error) {
  console.error('❌ エラー:', error.message);
  process.exit(1);
}
