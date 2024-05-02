FROM node:18-slim

WORKDIR /usr/local/app

COPY . .

RUN npm install

ENV PORT 80
EXPOSE 80

ENTRYPOINT ["node", "server.js"]
