const http = require("http");
const fs = require("fs");



const send_response = function (request, response) {
  console.log(request.method, request.url);
  
  if (request.url === "/") {
    response.writeHead(200, {
      "Content-Type": "text/html; charset=utf-8"  
    });

    response.end("<h1>/</h1>");
  }
  else if (request.url === "/notahome") {
    response.writeHead(200, {
      "Content-Type": "text/html; charset=utf-8"  
    });

    response.end("<h1>/notahome</h1>");
  }
  else {
    response.end("<h1>Wrong page!</h1>");
  }
};

const start_server = function () {
  const server = http.createServer(send_response);
  console.log("Server started");
  server.listen(3000);
}

start_server();