# vi

## 문자 치환 명령어
```sh
# abc를 def로 치환
:%s/abc/def

# 대소문자 구분 없이 치환
:%s/abc/def/i

# 맨 앞의 해당되는 단어만 치환 (ex. abcabcabc ➞ defabcabc)
:%s/abc/def/g
```

## 파일 내용 전체 삭제
```sh
ggdG
```

## 한 줄 삭제
```sh
dd
```
