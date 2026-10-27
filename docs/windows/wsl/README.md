# WSL (Windows Subsystem for Linux)

## 조건
1. 윈도우 10 (Ver.2004 이상), 윈도우 11
1. Power Shell 관리자 권한

## 설치
1. `wsl --install`
    ```ps1 hl_lines="2-15"
    PS C:\Windows\system32> wsl --install
    ダウンロード中: Linux 用 Windows サブシステム 2.6.3
    インストール中: Linux 用 Windows サブシステム 2.6.3
    Linux 用 Windows サブシステム 2.6.3 はインストールされました。
    Windows オプション コンポーネントをインストールしています: VirtualMachinePlatform

    展開イメージのサービスと管理ツール
    バージョン: 10.0.26100.5074

    イメージのバージョン: 10.0.26200.8117

    機能を有効にしています
    [==========================100.0%==========================]
    操作は正常に完了しました。
    要求された操作は正常に終了しました。変更を有効にするには、システムを再起動する必要があります。
    ```

1. 설치할 폴더 생성 후 이미지 임포트
    ```ps1
    mkdir C:\wsl\rocky

    wsl --import rocky C:\wsl\rocky C:\wsl\image\Rocky-10-WSL-Base.latest.x86_64.wsl
    ```

## 실행
```ps1
wsl -d rocky
```

## 리스트 확인
```ps1 hl_lines="3-4"
wsl -l -v

  NAME     STATE           VERSION
* rocky    Stopped         2
```

## 익스포트, 임포트
```ps1
# 익스포트
wsl --export NAME C:\wsl\export\exp_rocky_yyyymmdd

# 임포트
wsl --import NAME C:\wsl\NAME C:\wsl\export\exp_rocky_yyyymmdd
```

## 정지
```ps1
wsl --terminate NAME
```

## 삭제
```ps1
wsl --unregister NAME
```
