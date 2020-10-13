import json
from typing import Dict

from .utils import get_current_utc

DEFAULT_FILENAME = "./borrowers/candidates.json"


class Borrower:

    def __init__(self, email: str, age: int, income: float):
        self.created_at = get_current_utc()
        self.updated_at = self.created_at
        self.email = email
        self.age = age
        self.income = income

    def to_json(self) -> Dict:
        return {
            "email": self.email,
            "age": self.age,
            "income": self.income,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def save(self, file: str = DEFAULT_FILENAME):
        # TODO: save the borrower into the json file!
        with open(file, "r") as f:
            content = f.read()
            jason = json.loads(content)
            jason['candidates'].append(self.to_json())
            with open(file, "w") as f2:
                f2.write(json.dumps(jason, indent=4))

    def update(self, file: str = DEFAULT_FILENAME):
        # TODO: update the borrower on the json file that match the email of the current borrower.
        with open(file) as f:
            jason = json.load(f)
            for i in jason['candidates']:
                if i["email"] == self.email:
                    i["age"] = self.age
                    i["income"] = self.income
                    i["updated_at"] = self.updated_at
                jason["updated_at"] = self.updated_at
                with open("./borrowers/candidates.json", 'w') as f2:
                    f2.write(json.dumps(jason, indent=4))
