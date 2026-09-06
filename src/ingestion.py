from pathlib import Path

repo = Path("vllm")

for path in repo.rglob("*"):
    if path.is_file():
        print(path)
