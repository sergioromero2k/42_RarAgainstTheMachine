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
    @abstractmethod
    def chunk(
            self,
            content: str,
            file_path: str, max_chunk_size: int) -> List[MinimalSource]:
        pass
