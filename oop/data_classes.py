from collections import namedtuple
from dataclasses import dataclass, field, fields
from typing import ClassVar, List


@dataclass
class Coordinate:
    latitude: float
    longitude: float

    reference_system: ClassVar[str] = 'WGS84'

    def __str__(self):
        return f'{abs(self.latitude):.1f}°{"NS"[self.latitude < 0]} ' \
               f'{abs(self.longitude):.1f}°{"EW"[self.longitude < 0]}'

    def __repr__(self):
        return f'Coordinate({self.latitude}, {self.longitude})'


@dataclass
class Resource:
    """ Media Resource description"""
    title: str = '<untitled>'
    identifier: str = '0' * 13
    authors: List[str] = field(default_factory=list)
    date: str = ''
    type: str = ''
    category: List[str] = field(default_factory=list)
    language: str = ''
    summary: str = ''

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        repr_ = [f'{cls_name} (']
        for field_ in fields(self):
            value = getattr(self, field_.name)
            repr_.append(f'    {field_.name}: {value!r},')
        repr_.append(f')')
        return '\n'.join(repr_)


if __name__ == '__main__':
    CoordinateNT = namedtuple('Coordinate', 'lat long')
    cle = CoordinateNT(lat=41.5, long=-81.7)
    print(cle)

    latitude, longitude = cle
    print(f'latitude: {latitude}, longitude: {longitude}')

    print(f'Is it equal? : {(latitude, longitude) == cle}')

    cle = Coordinate(latitude=41.5, longitude=-81.7)
    print(cle)

    resource = Resource()
    print(resource)

    harry_potter = Resource(
        title='Harry Potter',
        identifier='9182142123645',
        authors=['J K Rowling'],
        date='2005-11-10',
        type='Fantasy',
        category=['Fiction', 'Series', 'Fantasy', 'Children'],
        language='English',
        summary='Story about a boy with a scar and his adventures in hogwarts school of witchcraft and wizardry'
    )
    print(harry_potter)

