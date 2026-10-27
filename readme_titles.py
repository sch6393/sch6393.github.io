
from pathlib import Path
import re

from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Section


def read_first_heading(path):
    """README.md에서 첫 번째 Markdown H1 제목을 읽는다."""
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError):
        return None

    # 코드 블록 안의 # 제목은 무시
    in_code_block = False

    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        match = re.match(r"^\s*#\s+(.+?)\s*#*\s*$", line)
        if match:
            return match.group(1).strip()

    return None


class ReadmeTitlesPlugin(BasePlugin):
    def on_nav(self, nav, config, files):
        self.update_sections(nav.items, config)
        return nav

    def update_sections(self, items, config):
        for item in items:
            if not isinstance(item, Section):
                continue

            # 해당 섹션의 README.md 찾기
            for child in item.children:
                if not hasattr(child, "file") or child.file is None:
                    continue

                src_path = child.file.src_path.replace("\\", "/")

                if Path(src_path).name.lower() == "readme.md":
                    readme_path = Path(config.docs_dir) / src_path
                    title = read_first_heading(readme_path)

                    if title:
                        item.title = title
                    break

            # 하위 폴더도 재귀적으로 처리
            self.update_sections(item.children, config)
