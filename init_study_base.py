from pathlib import Path

# 만들 최상위 폴더 이름
base_dir = Path("study_base")

# 생성할 폴더 목록
folders = [
    "codewars/easy",
    "codewars/medium",
    "leetcode/easy",
    "leetcode/medium",
    "leetcode/hard",
    "codeforces/div3",
    "codeforces/div2",
    "hackerrank/basic",
    "hackerrank/data_structures",
    "logs",
]

# 생성할 기본 파일 내용
files = {
    "README.md": """# study_base

알고리즘 / 디버깅 / 문제풀이 기록용 저장소

## 폴더 구조
- codewars
- leetcode
- codeforces
- hackerrank
- logs
""",
    "logs/bug_cases.md": """# Bug Cases

## Bug Case #001
- 문제:
- 증상:
- 원인:
- 내 잘못된 가정:
- 깨진 입력:
- 수정 내용:
""",
    "logs/patterns.md": """# Patterns

## Hash Map
- 설명:

## Sliding Window
- 설명:
""",
}

# 폴더 생성
for folder in folders:
    path = base_dir / folder
    path.mkdir(parents=True, exist_ok=True)

# 파일 생성
for file_path, content in files.items():
    full_path = base_dir / file_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    if not full_path.exists():
        full_path.write_text(content, encoding="utf-8")

print(f"'{base_dir}' 구조 생성 완료")