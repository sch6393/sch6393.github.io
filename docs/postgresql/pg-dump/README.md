# pg_dump

### 
PostgreSQL 백업은 목적에 따라 크게 **논리 백업(logical backup)**과 **물리 백업(physical backup)**으로 나뉩니다.

## 1. 특정 데이터베이스 백업 (`pg_dump`) - 가장 일반적

### SQL 파일로 백업

```bash
pg_dump -U postgres -d mydb > mydb.sql
```

복원:

```bash
psql -U postgres -d mydb < mydb.sql
```

---

### Custom 형식으로 백업 (권장)

압축이 가능하고 선택 복원이 가능합니다.

```bash
pg_dump -U postgres -d mydb -Fc -f mydb.dump
```

복원:

```bash
createdb -U postgres newdb

pg_restore -U postgres -d newdb mydb.dump
```

---

## 2. 모든 데이터베이스 백업 (`pg_dumpall`)

클러스터 전체(데이터베이스, 사용자, 권한 등)를 백업합니다.

```bash
pg_dumpall -U postgres > all.sql
```

복원:

```bash
psql -U postgres -f all.sql
```

---

## 3. 물리 백업 (`pg_basebackup`)

운영 서버 전체를 그대로 백업할 때 사용합니다.

```bash
pg_basebackup \
  -U replication_user \
  -D /backup/postgresql \
  -Fp \
  -Xs \
  -P
```

주요 특징

* WAL 포함
* 장애 복구용
* 복제 서버 구축에도 사용

---

## 4. Docker에서 백업

컨테이너 이름이 `postgres`인 경우

```bash
docker exec postgres pg_dump -U postgres mydb > mydb.sql
```

복원

```bash
cat mydb.sql | docker exec -i postgres psql -U postgres mydb
```

---

## 5. 자동 백업 (Linux cron)

매일 새벽 2시 백업

```cron
0 2 * * * pg_dump -U postgres mydb > /backup/mydb_$(date +\%F).sql
```

또는 gzip으로 압축

```bash
pg_dump -U postgres mydb | gzip > mydb_$(date +%F).sql.gz
```

복원

```bash
gunzip -c mydb_2026-07-29.sql.gz | psql -U postgres mydb
```

---

## 6. 백업 시 자주 사용하는 옵션

| 옵션    | 설명            |
| ----- | ------------- |
| `-U`  | 사용자           |
| `-h`  | 호스트           |
| `-p`  | 포트            |
| `-d`  | 데이터베이스        |
| `-Fc` | Custom 형식(권장) |
| `-Ft` | Tar 형식        |
| `-Fp` | Plain SQL     |
| `-f`  | 출력 파일         |
| `-v`  | 진행 상황 출력      |

예시:

```bash
pg_dump \
  -h localhost \
  -p 5432 \
  -U postgres \
  -Fc \
  -f backup.dump \
  mydb
```

## 어떤 방법을 선택해야 할까?

* **단일 데이터베이스 백업/복원** → `pg_dump -Fc` (가장 권장)
* **사용자, 권한까지 포함한 전체 서버 백업** → `pg_dumpall`
* **운영 서버 장애 복구 및 복제** → `pg_basebackup`
* **Docker 환경** → `docker exec`와 `pg_dump` 조합

`pg_dump -Fc` 형식은 압축 효율이 좋고 원하는 테이블만 선택적으로 복원할 수 있어 일반적인 운영 환경에서 가장 많이 사용됩니다.
