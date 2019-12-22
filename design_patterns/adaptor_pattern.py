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


if __name__ == '__main__':
    g = (i*i for i in range(10))
    f = FileAverageCalculator(GeneratorAdaptor(g))
    print(f.average())