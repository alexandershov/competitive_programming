import itertools
from dataclasses import dataclass
from typing import Iterator


def get_range_sum(seq: list, first: int, last: int) -> int:
    assert last >= first
    prefix_sums = get_prefix_sums(seq)
    return prefix_sums[last] - prefix_sums[first] + seq[first]


def get_prefix_sums(seq):
    cur_sum = 0
    sums = []
    for item in seq:
        cur_sum += item
        sums.append(cur_sum)
    return sums


def get_range_min(seq: list, first: int, last: int) -> int:
    assert first <= last
    sparse_table = get_sparse_table(seq)
    range_len = last - first + 1
    closest_len = max(size for size in sparse_table if size <= range_len)
    return min(
        sparse_table[closest_len][first],
        sparse_table[closest_len][last - closest_len + 1],
    )


def get_sparse_table(seq: list):
    table = {
        1: dict(enumerate(seq)),
    }
    range_len = 2
    while range_len <= len(seq):
        row = {}
        for i, item in enumerate(seq):
            if i + range_len <= len(seq):
                prev = table[range_len // 2]
                row[i] = min(prev[i], prev[i + range_len // 2])
        table[range_len] = row
        range_len *= 2
    return table


@dataclass(frozen=True)
class FenwickTree:
    values: list

    @staticmethod
    def get_range_length_at(index):
        return (index + 1) & -(index + 1)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, item, value):
        change = value - self._get_seq_value(item)
        for index in _unique(FenwickTree._iter_indexes_to_update(item)):
            if index >= len(self.values):
                return
            self.values[index] += change

    def get_range_sum_till(self, last: int) -> int:
        range_sum = 0
        current = last
        while current >= 0:
            range_sum += self[current]
            current -= self.get_range_length_at(current)
        return range_sum

    @staticmethod
    def _iter_indexes_to_update(start):
        exp = 1
        while True:
            # TODO: is there a way to improve +1 -1 stuff?
            div, mod = divmod(start + 1, exp)
            yield (div + int(bool(mod))) * exp - 1
            exp *= 2

    def _get_seq_value(self, item):
        assert item >= 0
        return self.get_range_sum_till(item) - self.get_range_sum_till(item - 1)

    def __eq__(self, other):
        if not isinstance(other, FenwickTree):
            return False
        return self.values == other.values


def build_fenwick_tree(seq: list) -> FenwickTree:
    # TODO: is there a way with less extra memory
    prefix_sums = get_prefix_sums(seq)
    values = []
    for last in range(0, len(seq)):
        length = FenwickTree.get_range_length_at(last)
        first = last - length + 1
        last_value = prefix_sums[last] - prefix_sums[first] + seq[first]
        values.append(last_value)
    return FenwickTree(values)


def get_fenwick_range_sum(seq: list, first: int, last: int) -> int:
    assert first <= last
    tree = build_fenwick_tree(seq)
    return tree.get_range_sum_till(last) - tree.get_range_sum_till(first - 1)


def _unique(it: Iterator) -> Iterator:
    for key, group in itertools.groupby(it):
        yield key
