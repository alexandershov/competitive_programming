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
    if n > len(seq) - start:
        return
    for i in range(start, len(seq)):
        for combination in iter_combinations(seq, n - 1, i + 1):
            yield combination | {seq[i]}


def iter_subsets(seq):
    # TODO: prove that result length is 2^n
    for i in range(len(seq) + 1):
        yield from iter_combinations(seq, i)
