const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 8080;

// 静的ファイルの提供（HTML, CSS, JS など）
const portalDir = './portal';
app.use(express.static(path.join(__dirname, portalDir)));
app.use('/assets', express.static(path.join(__dirname, portalDir, 'assets')));

// ルーティング: HTML ファイルを提供
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, portalDir, 'landing.html'));
});

app.get('/:page', (req, res) => {
  const page = req.params.page;
  const filePath = path.join(__dirname, portalDir, `${page}.html`);

  // セキュリティチェック: パストラバーサル対策
  if (!filePath.startsWith(path.join(__dirname, portalDir))) {
    return res.status(403).send('Forbidden');
  }

  // ファイルが存在するか確認
  if (fs.existsSync(filePath)) {
    res.sendFile(filePath);
  } else {
    res.status(404).send('Page not found');
  }
});

// ヘルスチェック
app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

// エラーハンドラ
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Internal Server Error');
});

app.listen(PORT, () => {
  console.log(`Internal DX Portal listening on port ${PORT}`);
});
