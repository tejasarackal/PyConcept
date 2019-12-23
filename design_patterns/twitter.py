from design_patterns.observer_pattern import Observer, Observable
from collections import defaultdict


class Twitter(Observer, Observable):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._timeline = defaultdict(list)

    @property
    def name(self):
        return self._name

    @property
    def timeline(self):
        ret_ = [f'Timeline for {self._name}']
        for lst in self._timeline.values():
            ret_.extend(lst)
            if len(ret_) > 50:
                break
        return '\n'.join(ret_)

    @property
    def followers(self):
        return f'{self.name!r} followers -> {[person.name for person in self.observers]}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r})'

    def update(self, person, tweet: str):
        print(f'{self.name} notified tweet from {person.name}: {tweet}')
        self._timeline[id(person)].append(f'tweet from {person.name}: {tweet}')

    def remove(self, person):
        del self._timeline[id(person)]

    def follow(self, person):
        person.add_observer(self)
        return self

    def unfollow(self, person):
        person.delete_observer(self)
        return self

    def tweet(self, tweet: str):
        self.notify_observers(tweet)


if __name__ == '__main__':
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    c = Twitter('Cheshire Cat')
    h = Twitter('Mad Hatter')

    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)

    print(f'{a}, {a.followers}')
    print(f'{k}, {k.followers}')
    print(f'{q}, {q.followers}')
    print(f'{c}, {c.followers}')
    print(f'{h}, {h.followers}')
    print('\n')

    print(f'======={q.name!r} tweets====')
    q.tweet('Off with their heads!!!')

    print(f'\n======={a.name!r} tweets====')
    a.tweet('What a strange world we live in')

    print(f'\n======={k.name!r} tweets====')
    k.tweet('Begin from the beginning, and go on till you come to the end: then stop.')

    print(f'\n======={c.name!r} tweets====')
    c.tweet('We are all mad in here.')

    print(f'\n======={h.name!r} tweets====')
    h.tweet('Why is a raven like a writing desk?')

    print(f'\n======={q.name!r} timeline====')
    print(q.timeline)

    print(f'\n======={a.name!r} timeline====')
    print(a.timeline)

    print(f'\n======={k.name!r} timeline====')
    print(k.timeline)

    print(f'\n======={c.name!r} timeline====')
    print(c.timeline)

    print(f'\n======={h.name!r} timeline====')
    print(h.timeline)

    print(f'\n======={h.name!r} timeline====')
    h.unfollow(q)
    print(f'{q}, {q.followers}')
    print(h.timeline)