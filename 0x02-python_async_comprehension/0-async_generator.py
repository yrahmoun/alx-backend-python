#!/usr/bin/env python3
"""module for task 0"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a sequence of 10 number"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
