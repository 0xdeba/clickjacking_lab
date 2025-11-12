FROM node:alpine
WORKDIR /app
COPY . .
RUN npm install -g http-server
EXPOSE 4000
CMD ["http-server", "-p", "4000"]