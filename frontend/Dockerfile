FROM node:18.17.1-alpine3.18

WORKDIR /frontend

ENV PATH /node_modules/.bin:$PATH

COPY package.json .

COPY src src

COPY public public

RUN npm -g install npm@latest --silent

EXPOSE 3000

# CMD npm run start
