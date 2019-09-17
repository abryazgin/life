import random
from hashlib import sha224


class Board(list):
    @staticmethod
    def generate(w, h):
        return Board(
            [random.randint(0, 1) for _ in range(w)]
            for _ in range(h)
        )

    def __repr__(self):
        symbol_map = {
            -1: '+',
            1: '@',
            0: '-',
        }
        cell = '\n'.join(
            (' '.join([symbol_map[el] for el in self[h]]) + ' ') * 3 for h in range(len(self))
        )
        return '\n'.join([cell] * 3) + '\n\n'

    def __bool__(self):
        return any(any(row) for row in self)

    def __hash__(self):
        return int(''.join([''.join([str(e) for e in row if e in [0,1]]) for row in self]), 2) % 10**40

