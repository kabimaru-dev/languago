const http = require("http");

const send_response = function (request, response) {
  console.log(request.method, request.url);

  if (request.url === "/") {
    response.end("/");
  }
  else if (request.url === "/home") {
    response.end("/home");
  }
  else {
    response.end("Wrong page!");
  }
};

const start_server = function () {
  const server = http.createServer(send_response);
  console.log("Server started");
  server.listen(3000);
}

start_server();