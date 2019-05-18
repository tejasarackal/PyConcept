from time import sleep
from decorators import dec


@dec.timer
def add1(x, y):
    return x + y


class Adder:
    @dec.timer
    def __call__(self, x, y):
        return x + y


add2 = Adder()


@dec.timer
def heavy_compute():
    rv = []
    for i in range(101):
        sleep(.1)
        rv.append(i)
    return rv


class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 100:
            raise StopIteration()
        sleep(.1)
        return rv


def compute():  # easier to read generator
    for i in range(101):
        sleep(.1)
        yield i


class Api:
    def first(self, x, y):
        return add1(x, y)

    def second(self, x, y):
        return add2(x, y)

    def last(self):
        return compute()

    def __call__(self, x, y):
        yield self.first(x, y)
        yield self.second(x, y)
        for value in self.last():
            yield value

if __name__ == '__main__':
    a = Api()
    for i in a(10, 20):
        print(i)
