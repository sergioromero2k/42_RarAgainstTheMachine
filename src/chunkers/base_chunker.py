from abc import ABC, abstractmethod
from src.models import MinimalSource
from typing import List


class BaseChunker(ABC):
    """
    Abstract base class for document chunkers.

    A chunker is responsible for splitting the content of a file into
    smaller chunks while preserving enough information to reconstruct
    their location in the original document.
    """

    def __init__(self, minimum_threshold: int = 100, overlap_size: int = 200):
        self.minimum_threshold = minimum_threshold
        self.overlap_size = overlap_size

    @abstractmethod
    def chunk(
            self,
            content: str,
            file_path: str, max_chunk_size: int) -> List[MinimalSource]:
        pass

    def _save_fragment(
            self,
            fragments: list,
            text: str,
            start_offset: int
    ) -> int:
        """"""
        if not text:
            return start_offset
        end_offset = start_offset + len(text)
        fragments.append({
            'text': text,
            'start': start_offset,
            'end': end_offset
        })
        return end_offset
