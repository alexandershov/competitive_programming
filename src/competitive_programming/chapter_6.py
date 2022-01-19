from __future__ import annotations

import collections
from dataclasses import dataclass, replace
from typing import Optional, Iterable

from competitive_programming import chapter_2


@dataclass(frozen=True)
class Square:
    x: int
    y: int

    def up(self) -> Square:
        return replace(self, y=self.y - 1)

    def down(self) -> Square:
        return replace(self, y=self.y + 1)

    def left(self) -> Square:
        return replace(self, x=self.x - 1)

    def right(self) -> Square:
        return replace(self, x=self.x + 1)


def solve_coins_problem(coins: set[int], amount: int) -> list[int]:
    assert amount >= 0
    assert_all_positive(coins)

    cache = {0: []}  # amount -> solution
    for cur_amount in range(0, amount + 1):
        for a_coin in coins:
            prev_solution = cache.get(cur_amount - a_coin)
            if prev_solution is None:
                continue
            new_solution = prev_solution + [a_coin]
            cache.setdefault(cur_amount, new_solution)
            cache[cur_amount] = min(cache[cur_amount], new_solution, key=len)
    return cache.get(amount)


def assert_all_positive(coins):
    for a_coin in coins:
        assert a_coin > 0


def solve_coins_count_problem(coins: set[int], amount: int) -> int:
    cache = collections.defaultdict(int, {0: 1})
    for cur_amount in range(1, amount + 1):
        for a_coin in coins:
            prev_count = cache[cur_amount - a_coin]
            cache[cur_amount] += prev_count
    return cache[amount]


@dataclass(frozen=True)
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
    indexes = frozenset(range(len(weights)))
    cache = {frozenset(): 0}
    return get_min_num_rides_rec(max_weight, weights, indexes, cache)


def get_min_num_rides_rec(max_weight: int, weights: list[int], indexes: frozenset[int],
                          cache: dict) -> int:
    if indexes in cache:
        return cache[indexes]
    num_rides = float('inf')
    for riders in chapter_2.rec_efficient_subsets(list(indexes)):
        if not riders:
            continue
        riders_weight = sum(weights[i] for i in riders)
        if riders_weight > max_weight:
            continue
        left_behind = indexes - riders
        num_rides = min(1 + get_min_num_rides_rec(max_weight, weights, left_behind, cache),
                        num_rides)
    cache[indexes] = num_rides
    return num_rides


def count_tilings_brute_force(width: int, height: int) -> int:
    return sum(
        1 for _ in iter_tilings(width, height, index=0, free=get_free_squares(width, height)))


def get_free_squares(width: int, height: int) -> set[Square]:
    free = set()
    for x in range(width):
        for y in range(height):
            free.add(Square(x, y))
    return free


def iter_tilings(width: int, height: int, index: int, free: set[Square]):
    if index == width * height:
        if not free:
            yield 'solution'
        return

    y, x = divmod(index, width)
    square = Square(x, y)
    if square not in free:
        yield from iter_tilings(width, height, index + 1, free)
        return

    for tile in get_tiles(square, width, height):
        if tile[1] not in free:
            continue
        free.remove(tile[0])
        free.remove(tile[1])
        yield from iter_tilings(width, height, index + 1, free)
        free.update(tile)


def get_tiles(square: Square, width: int, height: int) -> set[tuple[Square, Square]]:
    assert _is_inside(square, width, height)
    neighbours = [square.up(), square.down(), square.left(), square.right()]
    tiles = set()
    for candidate in neighbours:
        if _is_inside(candidate, width, height):
            tiles.add((square, candidate))
    return tiles


def _is_inside(square: Square, width: int, height: int) -> bool:
    return (0 <= square.x < width) and (0 <= square.y < height)


def generate_row_tilings(width: int, alphabet: str, tiling=None):
    if tiling is None:
        tiling = []
    if len(tiling) == width:
        yield ''.join(tiling)
        return
    for symbol in alphabet:
        tiling.append(symbol)
        yield from generate_row_tilings(width, alphabet, tiling)
        tiling.pop()


def count_tilings_dynamic_programming(width: int, height: int) -> int:
    # TODO: make it more elegant
    sentinel = ' ' * width
    counts = {  # k -> {last_row -> count}
        -1: {sentinel: 1},
        height: {sentinel: 1}
    }
    for k in range(height):
        cur_counts = collections.defaultdict(int)
        for row in generate_row_tilings(width, '<>^v'):
            if not has_valid_tiling(row, k, height):
                continue
            prev = counts[k - 1]
            for last_row, count in prev.items():
                if rows_match(last_row, row):
                    cur_counts[row] += count
        counts[k] = dict(cur_counts)
    return sum(counts[height - 1].values())


def rows_match(up: str, down: str) -> bool:
    for up_part, down_part in zip(up, down, strict=True):
        if up_part == '^' and down_part != 'v':
            return False
        if down_part == 'v' and up_part != '^':
            return False
    return True


def has_valid_tiling(row: str, k: int, height: int) -> bool:
    forbidden = set()
    if k == 0:
        forbidden.add('v')
    if k == height - 1:
        forbidden.add('^')

    for i, tile_part in enumerate(row):
        if tile_part in forbidden:
            return False
        if tile_part == '>':
            if i == 0:
                return False
            if row[i - 1] != '<':
                return False
        if tile_part == '<':
            if i == len(row) - 1:
                return False
            if row[i + 1] != '>':
                return False
    return True
