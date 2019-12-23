from collections import defaultdict
from decimal import Decimal


def new_decimal(value):
    if isinstance(value, float):
        value = str(value)
    return Decimal(value)


class FinancialHistory:
    """ Keeps a balance sheet of financial records """
    def __init__(self, initial_balance=0.0):
        self._balance = new_decimal(initial_balance)
        self._expenses = defaultdict(Decimal)
        self._incomes = defaultdict(Decimal)

    def __repr__(self):
        return f'{self.__class__.__name__} Balance: {self._balance:.2f}'

    @property
    def balance(self):
        return self._balance

    def spend(self, category: str, amount: float):
        amount = new_decimal(amount)
        self._expenses[category] += amount
        self._balance -= amount

    def receive(self, category: str, amount: float):
        amount = new_decimal(amount)
        self._incomes[category] += amount
        self._balance += amount

    def received_from(self, category: str):
        return self._incomes[category]

    def received_summary(self):
        for category, amount in self._incomes.items():
            if amount > 0:
                print(f'Money Received from {category}: {amount:.2f}')


if __name__ == '__main__':
    f = FinancialHistory(new_balance=100)
    f.spend(category='Shopping', amount=20.22)
    f.spend(category='Travel', amount=20.87)
    f.spend(category='Travel', amount=15.47)

    f.receive(category='Grant', amount=40.50)
    f.receive(category='Salary', amount=250.00)

    print(f)

    category = 'Salary'
    f.received_from(category=category)

    category = 'Investments'
    f.received_from(category=category)

    f.received_summary()

