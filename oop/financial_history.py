from collections import defaultdict
from decimal import Decimal


def new_decimal(value):
    if isinstance(value, float):
        value = str(value)
    return Decimal(value)


class FinancialHistory:
    """ Keeps a balance sheet of financial records """
    def __init__(self, new_balance=0.0):
        self._balance = new_decimal(new_balance)
        self._expenses = defaultdict(Decimal)
        self._incomes = defaultdict(Decimal)

    def __repr__(self):
        return f'{self.__class__.__name__} balance: {self._balance:.2f}'

    @property
    def balance(self):
        return self._balance

    def spend(self, category: str, amount: float):
        self._expenses[category] += amount
        self._balance -= amount

    def receive(self, category: str, amount: float):
        self._incomes[category] += amount
        self._balance += amount

