const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 8080;

// 静的ファイルの提供（assets フォルダのみ）
const portalDir = './portal';
// app.use(express.static(path.join(__dirname, portalDir))); // ← コメントアウト: ルーティングで明示的に処理
app.use('/assets', express.static(path.join(__dirname, portalDir, 'assets')));

// ルーティング: クエリパラメータとパスベース両対応
app.get('/', (req, res) => {
  const page = req.query.page;
  if (page) {
    // ?page=xxx 形式に対応
    // .html が含まれていない場合のみ .html を追加
    const fileName = page.endsWith('.html') ? page : `${page}.html`;
    const filePath = path.join(__dirname, portalDir, fileName);

    // デバッグログ
    console.log(`[QUERY PAGE] page=${page}, fileName=${fileName}, filePath=${filePath}`);

    // セキュリティチェック: パストラバーサル対策
    if (!filePath.startsWith(path.resolve(path.join(__dirname, portalDir)))) {
      console.log(`[SECURITY] Path traversal attempt blocked: ${filePath}`);
      return res.status(403).send('Forbidden');
    }

    if (fs.existsSync(filePath)) {
      console.log(`[SUCCESS] Sending file: ${filePath}`);
      return res.sendFile(filePath);
    } else {
      console.log(`[NOT FOUND] File not found: ${filePath}`);
      return res.status(404).send(`Page not found: ${fileName}`);
    }
  }
  // デフォルト: landing
  console.log(`[DEFAULT] Sending landing.html`);
  res.sendFile(path.join(__dirname, portalDir, 'landing.html'));
});

app.get('/:page', (req, res) => {
  const page = req.params.page;
  // .html が既に含まれている場合はそのまま、含まれていなければ追加
  const fileName = page.endsWith('.html') ? page : `${page}.html`;
  const filePath = path.join(__dirname, portalDir, fileName);

  // セキュリティチェック: パストラバーサル対策
  if (!filePath.startsWith(path.resolve(path.join(__dirname, portalDir)))) {
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
