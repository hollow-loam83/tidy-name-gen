"""Random name generation built on top of the formatter.

The generator normalizes its name pools once, at load time, rather than on
every call - the pools are small and reused, so there's no reason to redo
the same string work for every generated name.
"""

import random

from .data import FIRST_NAMES, LAST_NAMES
from .formatter import normalize_name


class RandomNameGenerator:
    def __init__(self, first_names=None, last_names=None, seed=None):
        raw_first = first_names if first_names is not None else FIRST_NAMES
        raw_last = last_names if last_names is not None else LAST_NAMES
        self._first = [normalize_name(name) for name in raw_first]
        self._last = [normalize_name(name) for name in raw_last]
        if not self._first or not self._last:
            raise ValueError("first_names and last_names must be non-empty")
        self._rng = random.Random(seed)

    def first_name(self):
        return self._rng.choice(self._first)

    def last_name(self):
        return self._rng.choice(self._last)

    def full_name(self):
        return f"{self.first_name()} {self.last_name()}"

    def many(self, count):
        return [self.full_name() for _ in range(count)]
