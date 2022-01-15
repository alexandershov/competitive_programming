from __future__ import annotations

import collections
import dataclasses
from typing import Optional, Iterable


def solve_coins_problem(coins: set[int], amount: int) -> list[int]:
    # TODO: make it more elegant
    assert amount >= 0
    for a_coin in coins:
        assert a_coin > 0

    cache = {0: []}  # amount -> solution
    for cur_amount in range(0, amount + 1):
        for a_coin in coins:
            prev_solution = cache.get(cur_amount - a_coin)
            if prev_solution is not None:
                if cur_amount not in cache or len(cache[cur_amount]) > len(prev_solution) + 1:
                    cache[cur_amount] = prev_solution + [a_coin]
    return cache.get(amount)


def solve_coins_count_problem(coins: set[int], amount: int) -> int:
    cache = collections.defaultdict(int, {0: 1})
    for cur_amount in range(1, amount + 1):
        for a_coin in coins:
            prev_count = cache[cur_amount - a_coin]
            cache[cur_amount] += prev_count
    return cache[amount]


@dataclasses.dataclass(frozen=True)
class Item:
    value: object
    max_len: int
    prev: Optional[Item]


def find_longest_increasing_subsequence(seq: list) -> list:
    items = []
    for i, value in enumerate(seq):
        less_than = (
            an_item
            for an_item in items
            if an_item.value < value
        )
        best = _pick_best(less_than)
        items.append(Item(value, best.max_len + 1 if best else 1, best))
    result = []
    best = _pick_best(items)
    while best is not None:
        result.append(best.value)
        best = best.prev
    return list(reversed(result))


def _pick_best(items: Iterable[Item]) -> Optional[Item]:
    return max(items, key=lambda item: item.max_len, default=None)


def find_best_path_in_grid(grid: list[list[int]]) -> int:
    pass
