from time import time


def timer(func):  # decorator
    def wrapper(*args, **kwags):
        before = time()
        value = func(*args, **kwags)
        after = time()
        print('time elapsed', after - before)
        return value
    return wrapper


@timer
def add(x, y):
    return x + y
# add = timer(add)


@timer
def sub(x, y):
    return x - y
# sub = timer(sub) - Decorator is mere syntax for this


if __name__ == '__main__':
    print('add(10,20) -> ', add(10, 20))
    print('add(10,-20) -> ', add(10, -20))
    print('add("a","b") -> ', add('a', 'b'))
    print('sub(40,20) -> ', sub(40, 20))
    print('sub(50,10) -> ', sub(50, 10))