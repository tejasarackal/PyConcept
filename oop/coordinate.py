from oop import geohash


class Coordinate:

    reference_system = 'WGS84'

    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{abs(self.latitude)}°{"NS"[self.latitude < 0]} ' \
               f'{abs(self.longitude)}°{"EW"[self.longitude < 0]}'

    def __repr__(self):
        return f'Coordinate({self.latitude}, {self.longitude})'

    def geohash(self):
        return geohash.encode(latitude=self.latitude, longitude=self.longitude)


if __name__ == '__main__':
    gulf_of_guinea = Coordinate()
    print(repr(gulf_of_guinea))

    greenwich = Coordinate(51.5)
    print(repr(greenwich))

    london = Coordinate(51.5, -0.1)
    print(london)

    print(repr(Coordinate.reference_system))
    cleveland = Coordinate(41.5, -81.7)
    print(repr(cleveland.reference_system))

    print(repr(cleveland.geohash()))