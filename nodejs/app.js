const http = require("http");
const fs = require("fs");
const hostname = "127.0.0.1";
const port = 3000;
const page_20kb = "../test-pages/20kb.html";
const page_500b = "../test-pages/500b.html";

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });
  if (req.url === "/20kb") {
    fs.readFile(page_20kb, null, function(error, data) {
      if (error) {
        res.writeHead(404);
        res.write("Not Found");
      } else {
        res.write(data);
      }
    });
  } else if (req.url === "/500b") {
    fs.readFile(page_500b, null, function(error, data) {
      if (error) {
        res.writeHead(404);
        res.write("Not Found");
      } else {
        res.write(data);
      }
    });
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}`);
});
