#!/usr/bin/env python3
"""module for task 11"""

from typing import Mapping, Any, Sequence, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """add type annotations """
    if key in dct:
        return dct[key]
    else:
        return default
