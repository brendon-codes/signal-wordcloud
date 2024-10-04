#!/usr/bin/env python3

from typing import Literal as Lit

def imshow(obj: object, interpolation: Lit["bilinear"] | None = None) -> None:
    ...

def axis(state: Lit["off"]) -> None:
    ...

def show() -> None:
    ...
