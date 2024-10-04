#!/usr/bin/env python3

from typing import Callable

class WordCloud:
    def __init__(self, width: int | None = None, height: int | None = None, background_color: str | None = None, max_words: int | None = None, normalize_plurals: bool = False) -> None: ...

    def generate_from_frequencies(self, frequencies: dict[str, int]) -> None: ...

    def recolor(self, color_func: Callable[[], str] | None = None, random_state: int | None = None) -> None: ...
