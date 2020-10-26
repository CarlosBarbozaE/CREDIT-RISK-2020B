import os
import json

from fintools.utils import timeit
from fintools.settings import get_logger


from .models import SIC, Single
from .settings import (
    INDUSTRY_CRAWLER_OUTPUT_FILE,
    INDUSTRY_CRAWLER_URL
)

logger = get_logger(name=__name__)


class Main:
    DEFAULT_URL = INDUSTRY_CRAWLER_URL
    DEFAULT_OUTPUT_FILE = INDUSTRY_CRAWLER_OUTPUT_FILE

    def _validate_filename(self, filename: str):
        # Validate if path exists
        target_directory = os.path.dirname(filename)
        if not os.path.exists(target_directory):
            raise ValueError(f"Directory {target_directory} does not exits")

    @timeit(logger=logger)
    def download(self, filename: str = DEFAULT_OUTPUT_FILE, url: str = DEFAULT_URL):
        self._validate_filename(filename)
        # Download industries
        sic_industries = SIC.from_url(url=url)
        data = sic_industries.jsonify()
        # Save data into filesystem
        with open(filename, "w") as f:
            f.write(data)

    def _keep_level(self, industry, until):
        children = industry["children"]
        children_level = {child["level"] for child in children}
        children_level = children_level.pop() if children_level else ""
        seen = children_level == until
        if seen:
            return {
                **industry,
                "children": [
                    {
                        **child,
                        "children": []
                    }
                    for child in children
                ]
            }
        else:
            return {
                **industry,
                "children": [
                    self._keep_level(industry=child, until=until)
                    for child in children
                ]
            }

    def show(self, filename: str = DEFAULT_OUTPUT_FILE, until: str = Single.level):
        self._validate_filename(filename)
        # Read the industry data
        with open(filename, "r") as f:
            data = json.loads(f.read())
        # Filter levels
        data = self._keep_level(industry=data, until=until)
        return json.dumps(data, indent=4)
