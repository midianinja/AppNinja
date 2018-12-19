FROM node:10

WORKDIR /usr/src/app

COPY . .

RUN npm install -g expo-cli

RUN npm install

EXPOSE 19000
EXPOSE 19001
EXPOSE 19002

ENTRYPOINT npm start
