import os


INDUSTRY_CRAWLER_URL = os.environ.get(
    "INDUSTRY_CRAWLER_URL",
    default="https://www.osha.gov/pls/imis/sic_manual.html"
)

INDUSTRY_CRAWLER_OUTPUT_FILE = os.environ.get(
    "INDUSTRY_CRAWLER_OUTPUT_FILE",
    default="./industry-crawler/industries.json"
)
