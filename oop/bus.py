class HauntedBus:
    passengers = list() # Bad Practice

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


class HauntedBusV2:

    def __init__(self, passengers=[]): # Bad Practice mutable defaults
        self.passengers = passengers

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers # Bad Practice referring to same object

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


class Bus:
    """ Correct implementation of a Bus """
    def __init__(self, passengers):
        self.passengers = list(passengers) if passengers else list()

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


if __name__ == '__main__':
    h1 = HauntedBus()
    h1.pick('Alice')
    h1.pick('Bob')

    print(f'{h1.__class__}: Bus 1 Passengers {h1.passengers}')

    h2 = HauntedBus()
    print(f'{h2.__class__}: Bus 2 Passengers {h2.passengers}')

    h3 = HauntedBusV2()
    h3.pick('Alice')
    h3.pick('Bob')

    print(f'{h3.__class__}: Bus 3 Passengers {h3.passengers}')

    h4 = HauntedBusV2()
    print(f'{h4.__class__}: Bus 4 Passengers {h4.passengers}')

    hockeyclub = ['Alice', 'Bob', 'Cathy', 'Dick', 'Ed', 'Fiona']
    h5 = TwilightBus(passengers=hockeyclub)

    h5.drop('Bob')
    h5.drop('Cathy')

    print(f'{h5.__class__}: Bus 5 Passengers {h5.passengers}')
    print(f'{h5.__class__}: hockey club {hockeyclub}')

    hockeyclub = ['Alice', 'Bob', 'Cathy', 'Dick', 'Ed', 'Fiona']
    h6 = Bus(hockeyclub)

    h6.drop('Bob')
    h6.drop('Cathy')

    print(f'{h6.__class__}: Bus 6 Passengers {h6.passengers}')
    print(f'{h6.__class__}: hockey club {hockeyclub}')
