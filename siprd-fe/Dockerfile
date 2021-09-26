FROM node:lts-alpine as builder

WORKDIR /app

COPY package*.json ./
# I don't know why, but for some reason 
# npm versions above 6 will fail npm install
RUN npm install -g npm@6
RUN npm install --save

COPY . .

EXPOSE 8080