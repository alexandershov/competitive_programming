from typing import Optional


def bubble_sort(seq: list) -> None:
    for i in range(len(seq)):
        for j in range(0, len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                swap(seq, j, j + 1)


def merge_sort(seq: list, start: int = 0, end: Optional[int] = None) -> None:
    if end is None:
        end = len(seq)

    if (end - start) <= 1:
        return

    mid = (start + end) // 2
    merge_sort(seq, start, mid)
    merge_sort(seq, mid, end)
    merged = merge(islice(seq, start, mid), islice(seq, mid, end))

    seq[start:end] = merged


def counting_sort(seq: list) -> None:
    if not seq:
        return

    minimum = min(seq)
    maximum = max(seq)

    counts = [0] * (maximum - minimum + 1)

    for item in seq:
        bucket = item - minimum
        counts[bucket] += 1

    index = 0
    for bucket, count in enumerate(counts):
        for _ in range(count):
            item = bucket + minimum
            seq[index] = item
            index += 1


def merge(*iters):
    values_by_it = {}
    for it in iters:
        try_add_next_value(values_by_it, it)

    while values_by_it:
        min_it = min(values_by_it, key=values_by_it.__getitem__)
        yield values_by_it.pop(min_it)

        try_add_next_value(values_by_it, min_it)


def try_add_next_value(values_by_it, it):
    try:
        values_by_it[it] = next(it)
    except StopIteration:
        pass


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


def islice(seq, start, end):
    for i in range(start, end):
        yield seq[i]
