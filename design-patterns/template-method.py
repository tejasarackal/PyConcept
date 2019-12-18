from abc import ABC, abstractmethod


class AverageCalculator(ABC):

    def average(self):
        total, items = 0, 0
        try:
            while self.has_next():
                total += self.next_item()
                items += 1
            else:
                raise RuntimeError("No items found for calculating average")
            return total/items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next_item(self):
        pass

    def dispose(self):
        pass
