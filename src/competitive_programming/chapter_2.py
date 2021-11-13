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

