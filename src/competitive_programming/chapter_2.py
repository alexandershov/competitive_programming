from dataclasses import dataclass


def factorial_modulo(n: int, m: int) -> int:
    assert n >= 0
    result = 1
    for i in range(1, n + 1):
        result = ((i % m) * (result % m)) % m
    return result


def combinations(seq, n, start=0):
    if n == 0:
        yield frozenset()
        return
    if n > len(seq) - start:
        return
    for i in range(start, len(seq)):
        for combination in combinations(seq, n - 1, i + 1):
            yield combination | {seq[i]}


def naive_subsets(seq):
    for i in range(len(seq) + 1):
        yield from combinations(seq, i)


def rec_subsets(seq, start=0):
    if start == len(seq):
        yield frozenset()
        return
    for subset in rec_subsets(seq, start + 1):
        yield subset
        yield subset | {seq[start]}


def rec_efficient_subsets(seq, start=0, output=None):
    if output is None:
        output = []

    if start == len(seq):
        yield frozenset(output)
        return

    yield from rec_efficient_subsets(seq, start + 1, output)

    output.append(seq[start])
    yield from rec_efficient_subsets(seq, start + 1, output)
    output.pop()


def iter_subsets(seq):
    frontier = [(0, [])]

    while frontier:
        level, path = frontier.pop()
        if level == len(seq):
            yield frozenset(path)
            continue
        frontier.append((level + 1, path + [seq[level]]))
        frontier.append((level + 1, path))


def iter_efficient_subsets(seq):
    output = []
    frontier = [(0, False)]
    while frontier:
        level, do_pop = frontier.pop()
        if do_pop:
            output.pop()

        if level == len(seq):
            yield frozenset(output)
            continue

        frontier.append((level + 1, True))
        frontier.append((level + 1, False))
        output.append(seq[level])


def rec_permutations(seq, start=0):
    if start == len(seq):
        yield list(seq)
        return
    for i in range(start, len(seq)):
        swap(seq, start, i)
        yield from rec_permutations(seq, start + 1)
        swap(seq, start, i)


def iter_permutations(seq):
    frontier = [(None, False, 0)]
    while frontier:
        index_to_add, cancel_level, level = frontier.pop()

        if cancel_level:
            swap(seq, level - 1, -1)
            continue

        if index_to_add is not None:
            swap(seq, index_to_add, level - 1)

        if level == len(seq):
            yield list(seq)
        else:
            frontier.append((None, True, level + 1))
            for i in reversed(range(level, len(seq))):
                frontier.append((i, False, level + 1))


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


class Square:
    def __init__(self, column, row, size):
        self.column = column
        self.row = row
        self.down_diagonal = get_down_diagonal(column, row)
        self.up_diagonal = get_up_diagonal(column, row, size)


@dataclass
class QueensState:
    taken_rows: list[int]
    taken_up_diagonals: list[int]
    taken_down_diagonals: list[int]

    @staticmethod
    def initial():
        return QueensState(
            taken_rows=[],
            taken_up_diagonals=[],
            taken_down_diagonals=[]
        )

    def can_take(self, square: Square) -> bool:
        if square.row in self.taken_rows:
            return False
        if square.up_diagonal in self.taken_up_diagonals:
            return False
        if square.down_diagonal in self.taken_down_diagonals:
            return False
        return True

    def take(self, square: Square):
        self.taken_rows.append(square.row)
        self.taken_up_diagonals.append(square.up_diagonal)
        self.taken_down_diagonals.append(square.down_diagonal)

    def pop(self):
        self.taken_rows.pop()
        self.taken_up_diagonals.pop()
        self.taken_down_diagonals.pop()


def solve_queen_problem(size, column=0, state=None):
    if size == 0:
        return

    if state is None:
        state = QueensState.initial()
    if column == size:
        yield 'solution'
        return
    for row in range(size):
        square = Square(column, row, size)
        if not state.can_take(square):
            continue
        state.take(square)
        yield from solve_queen_problem(size, column + 1, state)
        state.pop()


def get_down_diagonal(column, row):
    assert row >= 0
    return column + row


def get_up_diagonal(column, row, size):
    assert 0 <= row <= size - 1
    return column + size - 1 - row
