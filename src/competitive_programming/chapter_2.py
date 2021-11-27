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
    # TODO: prove that it's correct
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
