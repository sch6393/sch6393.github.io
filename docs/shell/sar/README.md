# sar

## 기본 형식
```sh hl_lines="2-9"
sar
Linux 6.18.48-107.148.amzn2023.aarch64 (DOCKER-A-SYSTEM)        10/23/26        _aarch64_       (4 CPU)

00:00:02        CPU     %user     %nice   %system   %iowait    %steal     %idle
00:10:46        all     15.14      0.00      3.88      0.32      0.79     79.86
00:20:46        all     14.55      0.00      3.80      0.31      0.69     80.65
00:30:46        all     14.75      0.00      3.80      0.29      0.70     80.46
00:40:46        all     14.73      0.00      3.80      0.29      0.62     80.57
...
```

## 계산
`%user`가 높다면 CPU, `%iowait`가 높다면 I/O의 부하가 있음

I/O에 대한 더 자세한 내용 ➞ [iostat](../iostat/README.md)

## 옵션
|옵션|설명|
|-|-|
|`-A`|상세 정보|
|`-b`|I/O 상태 정보|
|`-B`|페이징 통계 정보|
|`-d`|디스크 작업 확인|
|`-q`|대기열 작업 확인|
|`-r`|메모리와 스왑 공간의 상태|
|`-v`|커널 테이블과 파일에서의 [inode](../../linux/inode/README.md) 상태|
|`-w`|시스템의 Switching 상태|
|`-W`|시스템의 Swapping 상태|
