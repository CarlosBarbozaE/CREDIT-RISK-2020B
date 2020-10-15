import json
from typing import Dict

from .utils import get_current_utc


class Borrower:

    def __init__(self, email: str, age: int, income: float):
        self.created_at = get_current_utc()
        self.updated_at = self.created_at
        self.email = email
        self.age = age
        self.income = income

    def to_json(self) -> Dict:
        # TODO: return a json with the: email, age, income, created_at, and updated_at
        pass

    def save(self, file: str):
        # TODO: save the borrower into the json file!
        pass

    def update(self, file: str):
        # TODO: update the borrower on the json file that match the email of the current borrower.
        pass
