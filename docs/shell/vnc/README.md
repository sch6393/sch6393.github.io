# vnc

## 설치
```sh
dnf install tigervnc
```

## vnc 명령어
```sh
# vnc 실행
vncserver

# vnc 리스트 확인
vncserver -list

# vnc 종료
vncserver -kill display_number
```

## GUI 프로그램 실행 시 `No protocol specified` 라는 에러가 발생할 경우
```sh
# root 계정에서 실행해야함
xhost +
# access control disabled, clients can connect from any host
```
