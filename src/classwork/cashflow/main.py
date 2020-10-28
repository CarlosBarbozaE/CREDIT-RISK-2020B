import json

from fintools import CashFlow


class Main:

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
        value = CashFlow(amount=amount, n=n).pv(r=rate)
        return json.dumps(value.to_dict(), indent=4)

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
        fv = amount * (1 + rate) ** n
        cf = CashFlow(amount=fv, n=n)
        return json.dumps(cf.to_dict(), indent=4)
