class Tigger:

    def __str__(self):
        return 'I am the only one!'

    @staticmethod
    def roar():
        return 'Grr!'


class _Tigger:

    def __str__(self):
        return 'I am the only one!'

    @staticmethod
    def roar():
        return 'Grr!'


_instance = None


def Tigger():
    global _instance
    if _instance is None:
        _instance = _Tigger()
    return _instance


if __name__ == '__main__':
    a = Tigger()
    b = Tigger()

    print(f'ID(a): {id(a)}')
    print(f'ID(a): {id(b)}')
    print(f'are they the same object? : { a is b }') # Tigger is not a singleton

