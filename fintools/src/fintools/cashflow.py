from typing import Dict, Optional


class CashFlow:

    def __init__(self, amount: float, n: int):
        self.amount = amount
        self.n = n

    def pv(self, r: float) -> 'CashFlow':
        present = self.amount/(1+r)**self.n
        return CashFlow(amount=present, n=0)

    def shift(self, n: int, r: float) -> 'CashFlow':
        shift_value = self.amount*(1+r)**(n-self.n)
        return CashFlow(amount=shift_value, n=n)

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':
        if not reverse:
            value = other.amount*(1+r)**(self.n-other.n)
            merge_ = value+self.amount
            return CashFlow(amount=merge_, n=self.n)
        else:
            value = self.amount*(1+r)**(other.n-self.n)
            merge_ = value+other.amount
            return CashFlow(amount=merge_, n=other.n)

    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }
