import functools
import json
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


def print_terminal(logger, serializer_function=lambda obj: obj.__dict__):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            serial_obj = func(*args, **kwargs)
            try:
                formatted_output = json.dumps(serial_obj, indent=4, default=serializer_function)
                print(formatted_output)
            except TypeError as e:
                logger.error("Type Error encounter with message {}".format(e))
                raise

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

    @staticmethod
    def sensitivity_matching_meta_decorator():
        def decorator(func):
            @functools.wraps(func)
            def wrapper(self, pattern, *args, **kwargs):
                pattern = self._sensitivity_matching(string=pattern)
                return func(self, pattern, *args, **kwargs)

            return wrapper

        return decorator
