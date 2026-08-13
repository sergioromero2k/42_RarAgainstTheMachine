from src.chunkers.base_chunker import BaseChunker
from src.models import MinimalSource
from typing import List
import ast


class PythonChunker(BaseChunker):
    """"""

    def __init__(self, minimum_threshold: int = 100, overlap_size: int = 200):
        super().__init__(minimum_threshold, overlap_size)

    def chunk(
            self,
            content: str,
            file_path: str, max_chunk_size: int) -> List[MinimalSource]:

        if not content or not content.strip():
            return []

        lines = content.split('\n')
        pos_start_line = []
        pos = 0

        for line in lines:
            pos_start_line.append(pos)
            pos += len(line) + 1

        try:
            tree = ast.parse(content)
            for nodo in ast.walk(tree):
                if isinstance(nodo, (ast.FunctionDef, ast.ClassDef)):
                    start_char = pos_start_line[nodo.lineno - 1]
                    if nodo.end_lineno < len(pos_start_line):
                        fin_char = pos_start_line[nodo.end_lineno]
                    else:
                        fin_char = len(content)

                    text_function = content[start_char:fin_char]
                    if len(text_function) > max_chunk_size:
                        pass

        except SyntaxError:
            return []
