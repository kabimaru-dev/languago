const http = require("http");
const fs = require("fs");
const axios = require("axios");



const send_response = function (request, response) {
  console.log(request.method, request.url);
    
  if (request.url === "/translate") {
    let body = "";

    // request.on("data", chunk => body += chunk);
    request.on("data", function(chunk) {
      body += chunk;
    });

    request.on('end', function() {
      let data = JSON.parse(body);

      axios.post("http://localhost:5000/translate", {
        q: data.q,
        source: "en",
        target: data.target,
        format: "text"
      }).then(function(axiosResp) {

        response.writeHead(200, {
          "Content-Type": "application/json"
        });

        response.end(JSON.stringify(axiosResp.data));
      }).catch(function(error) {
        response.writeHead(500, {
          "Content-Type": "application/json"
        });

        response.end(JSON.stringify({ error: error.message }));
      });
    });
  }  
  else if (request.url === "/") {
    const page = fs.readFileSync("./views/public/index.html", "utf8");

    response.writeHead(200, {
      "Content-Type": "text/html; charset=utf-8"  
    });

    response.end(page);
  }
  else if (request.url === "/notahome") {
    const page = fs.readFileSync("./views/App.js", "utf8");

    response.writeHead(200, {
      "Content-Type": "text/html; charset=utf-8"  
    });

    response.end(page);
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

// const databaseUrl = "postgres://admin:password@10.0.0.4/app";

// router.post("/users", userController.create);