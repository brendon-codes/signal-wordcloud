#!/usr/bin/env python3

from typing import Iterable, TypedDict, Any, cast
from collections import Counter
import random
import re
import sys
from optparse import OptionParser

from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Row(TypedDict):
    body: str
    source: str | None


class Opts:
    exclude: str | None


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
    bodys4 = (_split(x) for x in bodys3)
    bodys5 = _flatten(bodys4)
    bodys6 = (x for x in bodys5 if len(x) <= 24 and len(x) > 1)
    return bodys6


def _remove_common_words(words: Iterable[str], common: frozenset[str]):
    return (x for x in words if x not in common)


def _color_func(*args: Any, **kwargs: Any):
    hue = random.randint(0, 360)
    sat = random.randint(80, 100)
    lum = random.randint(0, 40)
    ret = f"hsl({hue}, {sat}%, {lum}%)"
    return ret


def _show_image(wc: WordCloud):
    # plt.figure(figsize = (12, 9))
    plt.imshow(wc.recolor(color_func=_color_func, random_state=3), interpolation="bilinear", aspect="auto")
    plt.axis("off")
    plt.show()


def _make_wc(wordmap: dict[str, int]):
    wc = WordCloud(
        background_color="#FCFCFC",
        width=2400,
        height=1800,
        max_words=len(wordmap),
        normalize_plurals=True
    )
    wc.generate_from_frequencies(wordmap)
    # wc.fit_words(wordmap)
    return wc


def _get_frequent(words: Iterable[str]):
    cnt = Counter(words)
    common1 = dict(cnt.most_common())
    return common1


def _read_input():
    return sys.stdin.readlines()


def _get_opts():
    op = OptionParser()
    op.add_option(
        "-e",
        "--exclude",
        dest="exclude",
        help="Exclude words from this file",
        metavar="FILE",
        default=None
    )
    (options, _) = op.parse_args()
    ret = cast(Opts, options)
    return ret


def _read_excludes(filepath: str | None):
    if filepath is None:
        return frozenset[str]()
    with open(filepath, "r") as f:
        lines = f.readlines()
        words = (x.strip() for x in lines)
    ret = frozenset[str](words)
    return ret


def main():
    opts = _get_opts()
    exc_words = _read_excludes(opts.exclude)
    rows = _read_input()
    words1 = _extract_words(rows)
    words2 = _remove_common_words(words1, exc_words)
    frequent = _get_frequent(words2)
    wc = _make_wc(frequent)
    _show_image(wc)


if __name__ == "__main__":
    main()

