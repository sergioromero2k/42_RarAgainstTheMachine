from chunkers.base_chunker import BaseChunker
from typing import List
from src.models import MinimalSource
import re


class MarkdownChunker(BaseChunker):
    """"""

    def __init__(self, minimum_threshold: int = 100):
        self.minimum_threshold = minimum_threshold
        self.heading_pattern = re.compile(r'^[ ]{0,3}#{1,6}\s+', re.MULTILINE)

    patron_head = re.compile(r'^[]{0,3}#{1,6}\s+')

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

    def _split_long_text(self, text: str, base_start: int, max_chunk_size: int) -> List[dict]:
        """"""
        fragments = []
        parts = re.split(r'(\.)', text)
        sentences_info = []
        temp_current_sentence = ""

        for part in parts:
            temp_current_sentence += part
            if part == '.':
                sentences_info.append(temp_current_sentence)
                temp_current_sentence = ""

        if temp_current_sentence:
            sentences_info.append(temp_current_sentence)

        temp_chunk = ""
        chunk_start_offset = base_start

        for sentence in sentences_info:
            if len(sentence) > max_chunk_size:
                if temp_chunk:
                    chunk_start_offset = self._save_fragment(
                        fragments, temp_chunk, chunk_start_offset)
                    temp_chunk = ""

                words = re.split(r'(\s+)', sentence)
                emergency_chunk = ""

                for word in words:
                    if len(emergency_chunk) + len(word) <= max_chunk_size:
                        emergency_chunk += word
                    else:
                        if emergency_chunk:
                            chunk_start_offset = self._save_fragment(
                                fragments, emergency_chunk, chunk_start_offset)
                            emergency_chunk = word

                if emergency_chunk:
                    chunk_start_offset = self._save_fragment(
                        fragments, emergency_chunk, chunk_start_offset)
            else:
                if len(temp_chunk) + len(sentence) <= max_chunk_size:
                    temp_chunk += sentence
                else:
                    if temp_chunk:
                        chunk_start_offset = self._save_fragment(
                            fragments, temp_chunk, chunk_start_offset)
                    temp_chunk = sentence
        if temp_chunk:
            chunk_start_offset = self._save_fragment(
                fragments, temp_chunk, chunk_start_offset)

        return fragments

    def chunk(
            self,
            content: str,
            file_path: str, max_chunk_size: int) -> List[MinimalSource]:

        sections = []
        matches = list(self.heading_pattern.finditer(content))

        if not matches:
            sections.append(
                {
                    'text': content,
                    'start': 0,
                    'end': len(content)
                }
            )
        else:
            if matches[0].start() > 0:
                sections.append({
                    'text': content[:matches[0].start()],
                    'start': 0,
                    'end': matches[0].start()
                })
