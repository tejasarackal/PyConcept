from library import Base

# enforce constraint
assert hasattr(Base, 'foo'), "The foo method is broken!"


class Derived(Base):
    def bar(self):
        return 'bar'

    def bar2(self):
        return 'bar2'


u = Derived()
print(u.foo2())