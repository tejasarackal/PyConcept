class BaseMeta(type):
    def __new__(mcs, name, bases, body):
        if name != 'Base' and 'bar2' not in body:
            raise TypeError('Bad User Class')
        return super().__new__(mcs, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return 'foo'

    def foo2(self):
        return 'foo2'

    def __init_subclass__(cls, *a, **kw):
        super().__init_subclass__(*a, **kw)
        print('__init_subclass__', a, kw)

