from chunkers.base_chunker import BaseChunker
from typing import List
from src.models import MinimalSource
import re

class MarkdownChunker(BaseChunker):

    patron_head = re.compile(r'^[]{0,3}#{1,6}\s+')
    def chunk(
            self,
            content: str,
            file_path: str, max_chunk_size: int) -> List[MinimalSource]:

        lines = content.splitlines(keepends=True)

        sections = []
        current_heading = ""
        section_lines = []

        current_global_pos = 0
        section_global_start = 0

        for line in lines:
            stripped_line = line.strip()
            
