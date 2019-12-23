from oop.financial_history import FinancialHistory, new_decimal


class DeductibleHistory(FinancialHistory):

    def __init__(self, initial_balance=0.0):
        super().__init__(initial_balance)
        self._deductions = new_decimal(0.0)

    def __repr__(self):
        return f'{super().__repr__()}, Deductions: {self._deductions}'

    @property
    def deductions(self):
        return self._deductions

    def spend(self, amount, category, deducting=0.0):
        """ Record transactions with partial deductions """
        super().spend(category=category, amount=amount)
        if deducting:
            self._deductions += new_decimal(deducting)

    def spend_deductible(self, category, amount):
        """ Record transactions with full deductions """
        self.spend(amount=amount, category=category, deducting=amount)


if __name__ == '__main__':
    d = DeductibleHistory(1000)
    print(d)

    d.spend(amount=600, category='book', deducting=150)
    print(d)

    d.spend_deductible(category='charity', amount=250)
    print(d)

    print(d.deductions)