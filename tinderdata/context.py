"""
Created on 2019.08.30
:author: Felix Soubelet

A callable script to process and get insight on your Tinder data.
All functionality is packed in a class and can be imported.
"""

import time
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Callable


@contextmanager
def timeit(function: Callable) -> Iterator[None]:
    """
    Returns the time elapsed when executing code in the context via `function`.
    Original code from @jaimecp89

    Args:
        function: any callable taking one argument. Was conceived with a lambda in mind.

    Returns:
        The elapsed time as an argument for the provided function.

    Usage:
        with timeit(lambda spanned: logger.debug(f'Did some stuff in {spanned} seconds')):
            some_stuff()
            some_other_stuff()
    """
    start_time = time.time()
    try:
        yield
    finally:
        time_used = time.time() - start_time
        function(time_used)
