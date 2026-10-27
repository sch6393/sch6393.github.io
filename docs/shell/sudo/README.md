# sudo

## 내용
명령어 앞에 `sudo` 를 붙이게 되면 관리자 권한으로 명령어가 실행됨

!!! note "`/etc/sudoers` 파일에 명시되어 있는 유저만 사용 가능"
    1. root 접속
        ```sh
        su
        ```

    1. sudoer 파일 수정
        ```title="vi /etc/sudoers"
        ...
        ## Allow root to run any commands anywhere
        root    ALL=(ALL)       ALL

        USER    ALL=(ALL)       ALL # 새로 추가
        ```
