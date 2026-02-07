# Node.js ランタイム
FROM node:18-slim

# 作業ディレクトリを設定
WORKDIR /app

# package.json をコピー
COPY package*.json ./

# 依存関係をインストール
RUN npm install --production

# アプリケーションコードをコピー
COPY server.js .
COPY portal ./portal

# ポート 8080 を expose
EXPOSE 8080

# アプリケーションを起動
CMD ["npm", "start"]
