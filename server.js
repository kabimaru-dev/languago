const http = require("http");

const send_response = function (request, response) {
  response.end("Hello, World!");
};

const start_server = function () {
  const server = http.createServer(send_response);
  console.log("Server started");
  server.listen(3000);
}

start_server();