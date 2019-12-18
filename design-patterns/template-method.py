from abc import ABC, abstractmethod


class AverageCalculator(ABC):

    def average(self):
        total, items = 0, 0
        try:
            while self.has_next():
                total += self.next_item()
                items += 1
            if items == 0:
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


class FileAverageCalculator(AverageCalculator):

    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ""

    def next_item(self):
        next_ = float(self.last_line)
        self.last_line = self.file.readline()
        return next_

    def dispose(self):
        self.file.close()


class MemoryAverageCalculator(AverageCalculator):

    def __init__(self, list_: list()):
        self.list = iter(list_)

    def has_next(self):
        return self.list.__length_hint__() > 0

    def next_item(self):
        return next(self.list)

    #def average(self):
    #    if len(self.list) == 0:
    #        raise RuntimeError("No items found for calculating average")
    #    try:
    #        return sum(self.list) / len(self.list)
    #    finally:
    #        self.dispose()


if __name__ == '__main__':
    with open('numbers.txt') as file:
        f = FileAverageCalculator(file)
        print(f"Average for numbers in file is {f.average()}")

    m = MemoryAverageCalculator([1,2,3,4,5,6,7])
    print(f"Average of numbers in a list memory is {m.average()}")
