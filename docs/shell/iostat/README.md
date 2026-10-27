# iostat

## 기본 형식
```sh hl_lines="2-10 13-21"
iostat
Linux 6.18.48-107.148.amzn2023.aarch64 (DOCKER-A-SYSTEM)        10/23/26        _aarch64_       (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          13.02    0.00    3.73    0.27    0.63   82.34

Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
nvme0n1           5.67        17.60        33.82         0.00   33663747   64692228          0
nvme1n1           0.81         9.53        54.68         0.00   18238476  104614574          0
nvme2n1          27.79       102.18       345.68         0.00  195475414  661304599          0

iostat -x
Linux 6.18.48-107.148.amzn2023.aarch64 (DOCKER-A-SYSTEM)        10/23/26        _aarch64_       (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          13.02    0.00    3.73    0.27    0.63   82.34

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
nvme0n1          2.46     17.60     0.79  24.44    0.72     7.17    3.21     33.82     1.94  37.65    1.29    10.52    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.01   0.10
nvme1n1          0.14      9.53     0.00   0.01    0.82    67.31    0.67     54.68     0.13  16.27    1.71    82.19    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.01
nvme2n1          1.66    102.18     0.00   0.01    0.98    61.72   26.14    345.68     0.64   2.39    1.04    13.22    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.03   1.51
```

## 확인
항목|의미
-|-
%user, %system|CPU가 사용자 작업 및 커널 작업에 사용된 비율
%iowait|CPU가 I/O 완료를 기다린 시간의 비율
r/s, w/s|초당 읽기, 쓰기 요청 수
rMB/s, wMB/s|초당 읽기, 쓰기 처리량
await|I/O 요청의 평균 처리 시간(ms)
%util|디스크가 I/O 작업을 수행 중이었던 시간의 비율
