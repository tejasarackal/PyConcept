from sqlite3 import connect
from contextlib import contextmanager

# class contextmanager:
#    def __init__(self, gen):
#        self.gen = gen
#
#    def __call__(self, *args, **kwargs):
#        self.args, self.kwargs = args, kwargs
#        return self
#
#    def __enter__(self):
#        self.gen_inst = self.gen(*self.args, **self.kwargs)
#        next(self.gen_inst)
#
#    def __exit__(self, *args):
#        next(self.gen_inst, None)


@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')
# temptable = contextmanager(temptable) - decorator syntax


with connect('testdb') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points(x, y) values (1, 1)')
        cur.execute('insert into points(x, y) values (1, 2)')
        cur.execute('insert into points(x, y) values (1, 3)')
        cur.execute('insert into points(x, y) values (3, 2)')
        cur.execute('insert into points(x, y) values (4, 1)')
        for rows in cur.execute('select x, y from points'):
            print(rows)

        for rows in cur.execute('select sum(x * y) from points'):
            print(rows)

