# journald

## 기본 형식
```bash
cat /etc/systemd/journald.conf
```

내용상 대부분 기본값이 주석 처리되어 있었다.

특히:

```ini
#SystemMaxUse=
#SystemKeepFree=
#SystemMaxFileSize=
#SystemMaxFiles=100
#MaxRetentionSec=
#MaxFileSec=1month
```

모두 주석 상태이므로 해당 파일에서 명시적으로 로그 보존 기간을 설정한 상태는 아니었다.

중요하게:

```ini
#MaxFileSec=1month
```

도 주석이므로 실제 적용되는 `1month` 설정이 아니다.

---

## 4. systemd journal 실제 설정 확인 방법

전체 설정 및 drop-in까지 확인:

```bash
sudo systemd-analyze cat-config systemd/journald.conf
```

현재 journal 디스크 사용량:

```bash
journalctl --disk-usage
```

가장 오래된 로그 확인:

```bash
journalctl -o short-iso | head -n 1
```

가장 최근 로그 확인:

```bash
journalctl -o short-iso | tail -1
```

---

## 5. 시스템 로그를 14일만 보관하도록 변경

사용자가 시스템 로그를 **14일만 보관하고 그보다 오래된 로그는 자동 삭제**하도록 영구 설정하기로 했다.

기존 `/etc/systemd/journald.conf`를 직접 수정하지 않고 drop-in을 사용하는 방식으로 설정한다.

### 설정 파일 생성

```bash
sudo mkdir -p /etc/systemd/journald.conf.d

sudo tee /etc/systemd/journald.conf.d/retention.conf > /dev/null <<'EOF'
[Journal]
MaxRetentionSec=14day
EOF
```

### 설정 적용

```bash
sudo systemctl restart systemd-journald
```

### 적용 확인

```bash
sudo systemd-analyze cat-config systemd/journald.conf
```

다음 설정이 포함되어 있어야 한다.

```ini
[Journal]
MaxRetentionSec=14day
```

### 현재 journal 용량 확인

```bash
sudo journalctl --disk-usage
```

---

## 6. 기존 오래된 로그 즉시 정리

`MaxRetentionSec=14day` 설정은 앞으로의 보존 정책을 적용하기 위한 것이므로, 기존에 이미 쌓인 14일 초과 로그를 즉시 줄이고 싶으면 한 번 수동 정리한다.

```bash
sudo journalctl --vacuum-time=14d
```

그 후:

```bash
sudo journalctl --disk-usage
```

로 확인한다.

---

## 7. 추가로 논의된 디스크 정리

앞서 루트 디스크 분석에서 다음 영역도 확인됐다.

### DNF 캐시

```text
/var/cache/dnf  약 483M
```

안전한 캐시 정리:

```bash
sudo dnf clean all
```

### systemd journal

기존 journal을 100MB 수준으로 즉시 줄이는 방법으로:

```bash
sudo journalctl --vacuum-size=100M
```

도 논의했다.

단, 최종적으로 사용자가 원하는 정책은 **용량 기준이 아니라 14일 보관**이며, 영구 설정은 다음으로 결정했다.

```ini
[Journal]
MaxRetentionSec=14day
```

---

# 최종 상태

현재 대화에서 확인된 핵심 문제는 다음 두 가지다.

1. SSM Session Manager의 로컬 orchestration 데이터가 약 636MB까지 증가.
2. systemd journal이 약 394MB 사용.

시스템 로그에 대해서는 다음과 같이 영구적으로 14일 보관 정책을 적용한다.

```text
/etc/systemd/journald.conf.d/retention.conf

[Journal]
MaxRetentionSec=14day
```

적용:

```bash
sudo systemctl restart systemd-journald
```

기존 오래된 로그 정리:

```bash
sudo journalctl --vacuum-time=14d
```

확인:

```bash
sudo systemd-analyze cat-config systemd/journald.conf
sudo journalctl --disk-usage
```
