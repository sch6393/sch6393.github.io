# git

## git config
```
git config user.name "Son ChangHan"
git config user.email sch6393@gmail.com

git config --global user.name "Son ChangHan"     # 전역 설정
git config --global user.email sch6393@gmail.com # 전역 설정

git config --global commit.template .gitmessage.txt

# 파일, 폴더 이름의 대소문자를 구분하도록 함
git config --global core.ignorecase
```

## [gitmessage.txt](./gitmessage.txt.md)

## git commit
```
git add .
git commmit -m "Modify"
git push origin main

# 동기화
git pull
```

## git branch
```
git branch
git checkout branch_name
git merge branch_name
```

## git CRLF, LF
명령어|설명
-|-
`git config –global core.autocrlf true`|커밋할 시 CRLF ➞ LF, 체크아웃 시 LF ➞ CRLF (윈도우 전용)
`git config –global core.autocrlf input`|커밋할 시 CRLF ➞ LF, (리눅스, 맥)
`git config –global core.autocrlf false`|자동변환 없음 (기본 값)

## git remote
```
git remote set-url origin https://github.com/sch6393/sch.git
```

## git unset
```
# 로컬 언셋
git config --local --unset credential.helper

# 글로벌 언셋
git config --global --unset credential.helper

# 시스템 언셋 
git config --system --unset credential.helper
```
