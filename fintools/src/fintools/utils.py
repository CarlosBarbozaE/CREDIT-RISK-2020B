import functools
import time
from difflib import SequenceMatcher


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            out = func(*args, **kwargs)
            logger.warning("Execution time %s" % (time.time() - start))
            return out
        return wrapper
    return decorator


def method_caching(func):
    simple_cache = {}

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        hashable_key = frozenset(args).union(frozenset(kwargs.items()))
        key = hash(hashable_key)
        if key in simple_cache:
            return simple_cache[key]
        simple_cache[key] = func(self, *args, **kwargs)
        return wrapper(self, *args, **kwargs)
    return wrapper


def flatten_dict(self):
    out = {}

    def flatten_d(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten_d(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten_d(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x
    flatten_d(self)
    return out


class StringWrapper:
    """
    This is the string wrapper.
    """

    def __init__(self, value: str, case_sensitive: bool = False):
        self._value = value
        self.case_sensitive = case_sensitive

    def _sensitivity_matching(self, string: str) -> str:
        return string if self.case_sensitive else string.lower()

    @property
    def value(self) -> str:
        return self._sensitivity_matching(string=self._value)

    def contains(self, pattern: str, reverse: bool = False):
        pattern = self._sensitivity_matching(string=pattern)
        return (pattern in self.value) if not reverse else (self.value in pattern)

    def similarity_ratio(self, pattern: str) -> float:
        pattern = self._sensitivity_matching(string=pattern)
        return SequenceMatcher(None, self.value, pattern).ratio()

    def similar_enough(self, pattern: str, threshold: float) -> bool:
        pattern = self._sensitivity_matching(string=pattern)
        return self.similarity_ratio(pattern) > threshold

    def boolean_search(self, pattern: str, exact: bool, threshold: float, reverse: bool = False):
        pattern = self._sensitivity_matching(string=pattern)
        return self.contains(pattern, reverse=reverse) if exact \
            else self.similar_enough(pattern, threshold=threshold)
