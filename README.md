# IF4031-load-testing

## 1. Nginx Static Web Server

Untuk melakukan load testing, kami menggunakan tool bernama k6. Dengan tool ini,
kami dapat dengan mudah menguji berbagai metrik yang penting seperti requests
per second dan latency. Berikut cara melakukan pengujian:

- File 500b:
```
$ k6 run test-scripts/nginx_500b.js
```

- File 20Kb:
```
$ k6 run test-scripts/nginx_20kb.js
```

## 2. 