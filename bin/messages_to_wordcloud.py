#!/usr/bin/env python3

from typing import Iterable, TypedDict
from collections import Counter
import re
import sys

from wordcloud import WordCloud
import matplotlib.pyplot as plt


COMMON = frozenset({
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for',
    'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by',
    'from', 'they', 'we', 'say', 'or', 'an', 'will', 'my', 'one', 'all',
    'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get',
    'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him',
    'know', 'take', 'into', 'year', 'your', 'good', 'some', 'could', 'them',
    'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over',
    'also', 'back', 'after', 'use', 'two', 'how', 'our', 'first',
    'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day',
    'most', 'us', 'is', 'are', 'was', 'im', 'yeah', 'going', 'more', 'here', 'thats',
    'did', 'doing', 'had', 'your', 'those', 'am', 'been', 'ive', 'said', 'yes', 'too'
})

class Row(TypedDict):
    body: str
    source: str | None


def _clean(text: str):
    v1 = text
    v2 = v1.strip().lower()
    v3 = re.sub(r"\s+", " ", v2)
    v4 = re.sub(r"[^a-z\u0020]+", "", v3)
    v5 = re.sub(r"\s+", " ", v4).strip()
    if v5 == "":
        return None
    return v5


def _split(text: str):
    return text.split(" ")


def _flatten(groups: Iterable[Iterable[str]]):
    return (item for row in groups for item in row)


def _extract_words(rows: list[str]):
    bodys1 = rows
    bodys2 = (_clean(x) for x in bodys1)
    bodys3 = (x for x in bodys2 if x is not None)
    bodys3 = (_split(x) for x in bodys3)
    bodys4 = _flatten(bodys3)
    return bodys4


def _remove_common_words(words: Iterable[str]):
    return (x for x in words if x not in COMMON)


def _show_image(wc: WordCloud):
    # plt.figure(figsize = (20, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def _make_wc(wordmap: dict[str, int]):
    wc = WordCloud(width=800, height=400)
    wc.generate_from_frequencies(wordmap)
    return wc


def _get_frequent(words: Iterable[str]):
    cnt = Counter(words)
    common = dict(cnt.most_common(100))
    return common


def _read_input():
    return sys.stdin.readlines()


def main():
    rows = _read_input()
    words1 = _extract_words(rows)
    words2 = _remove_common_words(words1)
    frequent = _get_frequent(words2)
    wc = _make_wc(frequent)
    _show_image(wc)


if __name__ == "__main__":
    main()

