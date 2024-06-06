#!/usr/bin/env python3
"""module for task 9"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of a list"""
    return [(i, len(i)) for i in lst]
