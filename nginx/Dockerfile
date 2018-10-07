# Stage 1 build react-app
FROM node:10-alpine as build-deps
WORKDIR /src

## Copy files defining dependency first
COPY src/react-client/package.json  .
COPY src/react-client/package-lock.json  .
RUN npm i

## Then copy over the rest of directory and build
COPY src/react-client/ .
RUN npm run build

# Stage 2
FROM nginx:1.15.0

COPY nginx/nginx.conf   /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build-deps /src/build /static
