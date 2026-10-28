# GitHub Pages 배포 가이드 (MkDocs)

이 저장소는 MkDocs(Material 테마)로 문서 사이트를 만들고, GitHub Actions로 GitHub Pages에 배포합니다.

| 항목 | 값 |
| --- | --- |
| 사이트 URL | <https://sch6393.github.io/> |
| 배포 워크플로 | `.github/workflows/deploy.yml` |
| MkDocs 설정 | `mkdocs.yml` |
| 원본 문서 | `docs/` |
| 로컬 전용 플러그인 | `readme_titles.py`, `setup.py` (`readme-titles`) |
| 트리거 | `main` 브랜치 push, 수동 실행(`workflow_dispatch`) |

## 1. 동작 방식

```text
push (main)
  └─ build job
       ├─ Python 설정 + pip install mkdocs-material, pip install .
       ├─ mkdocs build  → site/
       └─ site/ 를 Pages 아티팩트로 업로드
  └─ deploy job (needs: build)
       └─ actions/deploy-pages 로 GitHub Pages에 게시
```

기존의 `mkdocs gh-deploy` 방식과 달리 `gh-pages` 브랜치를 만들지 않고,
빌드 결과물(site/)을 아티팩트로 업로드해 Pages 런타임에 그대로 게시합니다.

## 2. 최초 1회 설정 (수동)

1. 저장소 **Settings → Pages** 로 이동합니다.
2. **Build and deployment → Source** 를 `GitHub Actions` 로 선택합니다.
   (현재 이 저장소는 Pages가 아직 활성화되지 않은 상태입니다.)
3. **Settings → Actions → General → Workflow permissions** 에서
   `Read and write permissions` 를 선택합니다.
   - 아티팩트 배포만 사용한다면 워크플로에 선언된 `pages: write`, `id-token: write` 로 충분하지만,
     아래 6절의 `gh-deploy` 대안은 `contents: write` 가 필요합니다.
4. `main` 브랜치에 push 하거나 **Actions → Deploy MkDocs to GitHub Pages → Run workflow** 로 첫 배포를 실행합니다.
5. 배포가 끝나면 `https://sch6393.github.io/` 에서 확인합니다.

## 3. 워크플로 요약

- `permissions`: `contents: read`, `pages: write`, `id-token: write`
  (OIDC로 Pages에 배포하기 위한 최소 권한)
- `concurrency`: `group: pages`, `cancel-in-progress: false`
  (동시 배포 충돌 방지, 진행 중인 배포는 취소하지 않음)
- `environment: github-pages`: Actions 실행 로그에 배포 URL이 표시됩니다.

## 4. 로컬에서 미리보기

```powershell
python -m pip install mkdocs-material
python -m pip install .
python -m mkdocs serve
```

- <http://127.0.0.1:8000/> 에서 확인합니다. 문서를 수정하면 자동으로 다시 빌드됩니다.
- `readme-titles` 플러그인은 이 저장소의 `setup.py`로 설치되는 로컬 패키지이므로
  `pip install .` 을 빠뜨리면 빌드가 실패합니다.
- 빌드 결과만 확인하려면 `python -m mkdocs build` 를 실행합니다. 결과는 `site/` 에 생성됩니다.

## 5. 문제 해결

| 증상 | 원인 / 해결 |
| --- | --- |
| 사이트가 404 | **Settings → Pages → Source** 가 `GitHub Actions` 인지 확인 |
| `Unrecognised plugin 'readme-titles'` | 워크플로에서 `pip install .` 이 빠짐 |
| 배포 단계에서 `Resource not accessible by integration` | **Workflow permissions** 를 `Read and write permissions` 로 변경 |
| 배포가 계속 `queued` | 동일 `concurrency` 그룹의 이전 실행이 진행 중인지 확인 |
| `mkdocs build --strict` 실패 | 현재 `docs/` 에 앵커(`#...`)가 깨진 링크가 다수 있어 strict 모드는 실패합니다. 워크플로는 일반 빌드를 사용합니다. |

## 6. 대안: `gh-pages` 브랜치로 배포

브랜치 기반 배포가 필요하면 워크플로의 Deploy 단계를 아래처럼 바꾸고,
**Settings → Pages → Source** 를 `Deploy from a branch` → `gh-pages` / `(root)` 로 설정합니다.

```yaml
permissions:
  contents: write

# ... build 단계 생략 ...
      - name: Deploy
        run: mkdocs gh-deploy --force
```
