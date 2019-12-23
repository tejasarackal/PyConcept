from design_patterns.template_method import FileAverageCalculator

class GeneratorAdaptor:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def readline(self):
        try:
            return next(self.adaptee)
        except StopIteration:
            return ''

    def close(self):
        pass


class Duck:
    def quack(self):
        print('quack')

    def fly(self):
        print('I am flying!')


class Turkey:
    def gobble(self):
        print('gobble gobble!')

    def fly(self):
        print('I am flying a short distance')


class TurkeyAdaptor:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def quack(self):
        self.adaptee.gobble()

    def fly(self):
        [self.adaptee.fly() for _ in range(5)]


if __name__ == '__main__':
    g = (i*i for i in range(10))
    f = FileAverageCalculator(GeneratorAdaptor(g))
    print(f.average())

    print('\nTurkey Says...')
    turkey = Turkey()
    turkey.gobble()
    turkey.fly()

    print('\nDuck Says...')
    duck = Duck()
    duck.quack() 
    duck.fly()

    print('\nTurkey Adaptor Says...')
    turkey_adaptor = TurkeyAdaptor(turkey)
    turkey_adaptor.quack()
    turkey_adaptor.fly()