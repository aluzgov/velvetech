FROM node:12-alpine as build

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY ./ /app/

RUN npm run build

FROM nginx:1.15

COPY --from=build /app/dist/ /usr/share/nginx/html
