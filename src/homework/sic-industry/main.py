import os
import json
from typing import Dict

from fintools.settings import get_logger
from fintools.utils import StringWrapper, timeit, print_terminal

from .settings import (
    INDUSTRY_SEARCH_DEFAULT_FILENAME,
    INDUSTRY_SEARCH_DEFAULT_THRESHOLD
)

logger = get_logger(name=__name__)


class Main:
    threshold = INDUSTRY_SEARCH_DEFAULT_THRESHOLD

    def _recursive_search(self, node, string_wrapper, exact):
        title = node["title"]
        children = node["children"]
        new_children = []
        for child in children:
            is_child_valid = self._recursive_search(child, string_wrapper, exact)
            if is_child_valid:
                new_children.append(child)
        node["children"] = new_children
        search = len(new_children) or string_wrapper.boolean_search(title, exact=exact,
                                                                    threshold=0.5, reverse=True)
        return search

    @timeit(logger=logger)
    @print_terminal(logger)
    def search(self, title: str, exact: bool = False, file: str = INDUSTRY_SEARCH_DEFAULT_FILENAME) -> list:
        with open(file, 'r') as f:
            jason = json.load(f)
            target_title = StringWrapper(value=title)
            children = jason["children"]
            new_children = []
            for child in children:
                if self._recursive_search(child, target_title, exact=exact):
                    new_children.append(child)
            return new_children
