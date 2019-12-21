from collections import namedtuple
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Coordinate:
    latitude: float
    longitude: float

    reference_system: ClassVar[str] = 'WGS84'

    def __str__(self):
        return f'{abs(self.latitude)}°{"NS"[self.latitude < 0]} ' \
               f'{abs(self.longitude)}°{"EW"[self.longitude < 0]}'

    def __repr__(self):
        return f'Coordinate({self.latitude}, {self.longitude})'


if __name__ == '__main__':
    CoordinateNT = namedtuple('Coordinate', 'lat long')
    cle = CoordinateNT(lat=41.5, long=-81.7)
    print(cle)

    latitude, longitude = cle
    print(f'latitude: {latitude}, longitude: {longitude}')

    print(f'Is it equal? : {(latitude, longitude) == cle}')

    cle = Coordinate(lat=41.5, long=-81.7)
    print(cle)
