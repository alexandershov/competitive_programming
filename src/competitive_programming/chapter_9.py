from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Iterator, Callable, Optional


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

    @staticmethod
    def build(seq: list) -> FenwickTree:
        prefix_sums = get_prefix_sums(seq)
        for last in reversed(range(0, len(seq))):
            length = FenwickTree.get_range_length_at(last)
            first = last - length + 1
            last_value = prefix_sums[last] - prefix_sums[first] + seq[first]
            prefix_sums[last] = last_value
        return FenwickTree(prefix_sums)

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
        one_based_start = start + 1
        exp = 1
        while True:
            div, mod = divmod(one_based_start, exp)
            yield _zero_based((div + int(bool(mod))) * exp)
            exp *= 2

    def _get_seq_value(self, item):
        assert item >= 0
        return self.get_range_sum_till(item) - self.get_range_sum_till(item - 1)

    def __eq__(self, other):
        if not isinstance(other, FenwickTree):
            return False
        return self.values == other.values


def get_fenwick_range_sum(seq: list, first: int, last: int) -> int:
    assert first <= last
    tree = FenwickTree.build(seq)
    return tree.get_range_sum_till(last) - tree.get_range_sum_till(first - 1)


def _unique(it: Iterator) -> Iterator:
    for key, group in itertools.groupby(it):
        yield key


def _zero_based(index: int) -> int:
    assert index >= 1
    return index - 1


@dataclass(frozen=True)
class Range:
    first: int
    last: int

    def combine_with(self, other: Range) -> Range:
        assert self.last + 1 == other.first
        return Range(self.first, other.last)


@dataclass
class Node:
    value: object
    range: Range
    left: Optional[Node]
    right: Optional[Node]
    parent: Optional[Node]

    @staticmethod
    def build_leaf(value, index) -> Node:
        return Node(
            value=value,
            range=Range(index, index),
            left=None,
            right=None,
            parent=None,
        )


@dataclass(frozen=True)
class SegmentTree:
    root: Optional[Node]
    operation: Callable

    @staticmethod
    def build(seq: list, operation: Callable) -> SegmentTree:
        root = None
        level = SegmentTree._build_initial_level(seq)
        while len(level) > 1:
            level = SegmentTree._build_next_level(level, operation)

        if len(level) == 1:
            root = level[0]
        return SegmentTree(root, operation)

    @staticmethod
    def _build_next_level(level: list[Node], operation: Callable) -> list[Node]:
        next_level = []
        for left, right in _pairs(level):
            next_level.append(SegmentTree.combine(left, right, operation))
        level = next_level
        return level

    @staticmethod
    def _build_initial_level(seq):
        level = [
            Node.build_leaf(value, index)
            for index, value in enumerate(seq)
        ]
        return level

    @staticmethod
    def combine(left: Node, right: Node, operation: Callable) -> Node:
        assert left.range.last + 1 == right.range.first
        parent = Node(
            value=operation(left.value, right.value),
            range=left.range.combine_with(right.range),
            left=left,
            right=right,
            parent=None,
        )
        left.parent = parent
        right.parent = parent
        return parent


def _pairs(seq: list):
    assert not len(seq) % 2
    for i in range(0, len(seq), 2):
        yield seq[i], seq[i + 1]
