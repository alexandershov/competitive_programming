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


def find_best_path_in_grid(grid: list[list[int]], cache=None, destination=None) -> int:
    if destination is None:
        destination = len(grid[0]) - 1, len(grid) - 1
        cache = {(0, 0): grid[0][0]}
    if cache.get(destination) is not None:
        return cache[destination]

    x, y = destination
    cost = grid[y][x]
    best = max(
        find_best_path_in_grid(grid, cache, source)
        for source in get_sources(destination)
    )
    cache[destination] = best + cost
    return cache[destination]


def get_sources(destination):
    x, y = destination
    candidates = [(x - 1, y), (x, y - 1)]
    return [a_candidate for a_candidate in candidates if is_valid(a_candidate)]


def is_valid(square):
    x, y = square
    return x >= 0 and y >= 0


def find_knapsack_sums(weights: list[int]) -> set[int]:
    sums = {0: {frozenset()}}
    for a_sum in range(sum(weights) + 1):
        for i, weight in enumerate(weights):
            prev_sum = a_sum - weight
            if prev_sum in sums:
                for items in sums[prev_sum]:
                    if i not in items:
                        sums.setdefault(a_sum, set()).add(items | {i})
    return set(sums)


def get_min_num_rides(max_weight: int, weights: list[int]) -> int:
    pass
