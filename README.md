# IF4031 PAT: Event-Driven Web-Server Performance Testing
13516107 - Senapati Sang Diwangkara
13516??? - Faza Fahleraz
13516??? - Dion Saputra

## Metode Pengujian
* Kami memilih `pyuv` (libuv binding untuk Python) untuk low-level library dan `node.js` untuk high-level library. 
* Ketiga webserver (nginx, node, pyuv) dibenchmark secara local menggunakan tools:
  * ApacheBench (untuk simulasi beban C10K dan penghitungan RPS) dg command
  * [mem_usage_ui](https://github.com/parikls/mem_usage_ui) (untuk monitor memory usage)
* Komputer yang digunakan untuk benchmark mempunyai environment sebagai berikut
  * Intel i5-3317U (4-core @ 1.7 GHz)
  * 8GB RAM
  * Arch Linux
* Pengujian dilakukan 5 kali dan diambil rata-rata datanya
  * Masing-masing pengujian dilakukan dengan 80k request dengan 10k concurrency
  * Command yg digunakan adalah `ab -n 80000 -c 10000 <webserver-endpoint>`
* Setiap pengujian, webserver direstart


## Hasil eksperimen
### nginx 1.16.1
* nginx yg digunakan diinstall dari package manager Arch Linux (pacman) dengan menggunakan command `sudo pacman -S nginx-stable`
* Sebelum melakukan testing, copy isi folder `test-pages` ke folder `/usr/share/nginx/html/`
* Run server dengan cara me-run `sudo systemctl start nginx`. Secara default, server akan listen di port **80**
#### 500b
Mean RPS            : 15789.24, 15481.22, 15474.36, 15823.97, 15798.94
Mean latency (ms)   : 68, 70, 70, 68, 68
Peak memory (MB)    : 5, 5, 5, 5, 5

#### 20kb
Mean RPS            : 15217.48, 14980.58, 15195.16, 15161.49, 15205.60
Mean latency (ms)   : 71, 72, 71, 71, 71
Peak memory (MB)    : 5, 5, 5, 5, 5


### node 12.9.1
* node.js yg digunakan diinstall dari package manager Arch Linux (pacman) dengan menggunakan command `sudo pacman -S nodejs`
* Sebelum melakukan testing, ubah variable `page_500b` dan `page_20kb` di dalam file `nodejs/app.js` menjadi direktori file yang ingin ditest
* Run server dengan cara me-run `node directory/to/app.js`. Secara default, server akan listen di port **3000**
#### 500b
Mean RPS            : 3800.95, 3620.76, 3776.75, 3819.18, 3856.17
Mean latency (ms)   : 694, 746, 795, 776, 717
Peak memory (MB)    : 114, 112, 118, 109, 108

#### 20kb
Mean RPS            : 3343.42, 3571.94, 3369.71, 3275.40, 3513.96
Mean latency (ms)   : 752, 645, 838, 772, 684
Peak memory (MB)    : 176, 160, 180, 180, 160


### pyuv 1.40, python 3.6
* library pyuv yg digunakan diinstall dari pip dengan menggunakan command `pip install pyuv`
* Sebelum melakukan testing, ubah variable `file_dir` di dalam file `pyuv/pyuv_server.py` menjadi direktori file yang ingin ditest
* Run server dengan cara me-run `python directory/to/pyuv_server.py`. Secara default, server akan listen di port **1234**
#### 500b
Mean RPS            : 11092.57, 11003.84, 10875.02, 10827.93, 11028.24
Mean latency (ms)   : 819, 818, 826, 831, 827
Peak memory (MB)    : 10, 10, 10, 10, 10

#### 20kb
Mean RPS            : 10511.63, 10841.21, 10515.37, 10440.68, 10614.40
Mean latency (ms)   : 866, 841, 847, 858, 847
Peak memory (MB)    : 10, 10, 10, 10, 10

## Kesimpulan
RPS yg didapat untuk beban C10K yg didapat di masing-masing server adalah sebagai berikut:
|      |  nginx   |  node   |   pyuv   |
|:----:|----------|---------|----------|
| 500b | 15673.55 | 3774.76 | 10965.52 |
| 20kb | 15152.06 | 3414.89 | 10584.66 |