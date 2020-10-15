import json
from fintools.utils import flatten_dict
from fintools.settings import get_logger

logger = get_logger(name="__main__")


class Main:

    @staticmethod
    def show(file: str) -> str:
        logger.info("Calling the show method.")
        # TODO: read file and show content
        with open(file, "r") as f:
            content = f.read()
        return content

    @staticmethod
    def flatten(file: str):
        with open(file, "r") as f:
            content = f.read()
            jason = json.loads(content)
            out = flatten_dict(jason)
            out = json.dumps(out, indent=4)
        return out
