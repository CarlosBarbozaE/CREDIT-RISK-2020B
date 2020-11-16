from typing import Optional

from fintools import Amortization


class Main:

    @staticmethod
    def annuity(amount: float, rate: float, n: int):
        amortization = Amortization(amount, rate, n)
        return amortization.annuity

    @staticmethod
    def table(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        amortization = Amortization(amount, rate, n)
        table = amortization.get_table()
        print(table)
        if save_file:
            table.to_csv(save_file)

    @staticmethod
    def plot(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        amortization = Amortization(amount, rate, n)
        figure = amortization.plot()
        if save_file:
            figure.savefig(save_file)
        return figure
