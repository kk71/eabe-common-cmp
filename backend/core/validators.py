__all__ = [
    "DotSplitStr",
    "DotSplitInt",
]

from typing import Annotated

from pydantic import BeforeValidator


def dot_split_str_inner(s: str | list[str]):
    if isinstance(s, list):
        s = s[0]
    if not s:
        return []
    return s.split(",")

DotSplitStr = Annotated[list[str], BeforeValidator(dot_split_str_inner)]
DotSplitInt = Annotated[list[int], BeforeValidator(dot_split_str_inner)]
