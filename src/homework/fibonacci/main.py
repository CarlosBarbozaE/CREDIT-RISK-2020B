from typing import List

from fintools.settings import get_logger
from fintools.utils import timeit
from fintools.utils import method_caching

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    @method_caching
    def element(self, position: int) -> int:
        if position == 0:
            return 0
        if position == 1:
            return 1
        return self.element(position=position - 1) + self.element(position=position - 2)

    @timeit(logger=logger)
    def sequence(self, length: int) -> List[int]:
        fibonacci_list = []
        for i in range(length):
            fibonacci_list.append(self.element(i)) 

        fibonacci_list = list(map(lambda x: round(x), fibonacci_list))
        return fibonacci_list
