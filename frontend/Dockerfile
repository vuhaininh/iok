FROM node:14.3-alpine3.10
WORKDIR /app
COPY ./package.json .
RUN npm install
ENV PATH /app/node_modules/.bin:$PATH

WORKDIR /app/frontend
