from src.models import AnsweredQuestion, MinimalSource
from src.chunkers.markdown_chunker import MarkdownChunker
from src.chunkers.python_chunker import PythonChunker


with open("src/chunkers/markdown_chunker.py", "r") as f:
    content = f.read()


py_test = PythonChunker()
py_test.chunk(content, "./src/chunkers/markdown_chunker.py", 30000)
