from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self) -> float:
        return self.rate * self.amount/(1-(1+self.rate)**(-self.n))

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        rows = []
        amount = self.amount
        a = 'nan'
        principal = 'nan'
        rate_value = 'nan'
        for i in range(self.n+1):
            rows.append(
                {"B": amount, "A": a, "P": principal, "I": rate_value})
            table = pd.DataFrame(rows).rename_axis("t").reset_index()
            a = self.annuity
            rate_value = amount * self.rate
            principal = a - rate_value
            amount = amount - principal
            if save_file:
                table.savefig(save_file)
        return pd.DataFrame(rows).rename_axis("t").reset_index()

    def plot(self, show: bool = False, save_file: Optional[str] = None):
        df = self.get_table()
        df = df.astype('float')
        plot = df.plot.bar(x="t", y=["P", "I"], stacked=True)
        fig = plot.get_figure()
        plt.grid()
        plt.show()
        if show:
            return fig
        if save_file:
            fig.savefig(save_file)
        return fig
