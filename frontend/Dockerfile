FROM node:latest

WORKDIR /code

COPY ["package.json", "package-lock.json*", "./"]

RUN  npm install

COPY . .

EXPOSE 8080

RUN npm run build

CMD ["npm", "start"]