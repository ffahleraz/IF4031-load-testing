import http from "k6/http";
import { sleep } from "k6";

export let options = {
  stages: [
    // { duration: "10s", target: 100 },
    // { duration: "10s", target: 500 },
    // { duration: "20s", target: 1000 },
    // { duration: "20s", target: 5000 },
    { duration: "1m", target: 10000 },
  ]
};

export default function() {
  http.get("http://localhost:80/500b.html");
  sleep(1);
};