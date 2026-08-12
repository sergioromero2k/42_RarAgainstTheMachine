from chunkers.base_chunker import BaseChunker
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
        ...
