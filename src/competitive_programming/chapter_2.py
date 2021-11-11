import itertools


def factorial_modulo(n: int, m: int) -> int:
    assert n >= 0
    result = 1
    for i in range(1, n + 1):
        result = ((i % m) * (result % m)) % m
    return result


def iter_combinations(seq, n, start=0):
    if n == 0:
        yield frozenset()
        return
    if n > len(seq):
        return
    for i, item in enumerate(itertools.islice(seq, start, len(seq)), start=start):
        for combination in iter_combinations(seq, n - 1, i + 1):
            yield combination | {item}


def iter_subsets(seq):
    for i in range(len(seq) + 1):
        yield from iter_combinations(seq, i)
