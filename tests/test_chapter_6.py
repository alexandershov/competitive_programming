import pytest

from competitive_programming import chapter_6


@pytest.mark.parametrize('coins, amount, expected', [
    pytest.param(
        {100, 99, 6, 1},
        105,
        [99, 6],
        id='it should pick the minimum amount of coins'
    ),
    pytest.param(
        {100, 99, 6, 1},
        0,
        [],
        id='it should return empty list if amount is zero'
    ),
    pytest.param(
        {100, 99, 6},
        10,
        None,
        id="it should return None if there's no solution"
    )
])
def test_solve_coins_problem(coins, amount, expected):
    assert try_sorted(chapter_6.solve_coins_problem(coins, amount)) == try_sorted(expected)


@pytest.mark.parametrize('coins, amount, expected', [
    pytest.param(
        {1, 3, 4},
        5,
        6,
        id='it should count the number of ways to construct an amount'
    )
])
def test_solve_coins_count_problem(coins, amount, expected):
    assert chapter_6.solve_coins_count_problem(coins, amount) == expected


def try_sorted(opt_seq):
    if opt_seq is None:
        return None
    return sorted(opt_seq)


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [],
        [],
        id='it should return an empty list if input is empty'
    ),
    pytest.param(
        [10, 9, 8],
        [10],
        id='it should return one element if input is in reversed order'
    ),
    pytest.param(
        [8, 9, 10],
        [8, 9, 10],
        id='it should return the input unchanged is input is sorted'
    ),
    pytest.param(
        [6, 2, 5, 1, 7, 4, 8, 3],
        [2, 5, 7, 8],
        id='it should work on the example from the book',
    ),
])
def test_find_longest_increasing_subsequence(seq, expected):
    assert chapter_6.find_longest_increasing_subsequence(seq) == expected


@pytest.mark.parametrize('grid, expected', [
    pytest.param(
        [
            [8]
        ],
        8,
        id='it should return the only element when given a singleton grid'
    ),
    pytest.param(
        [
            [3, 7, 9, 2, 7],
            [9, 8, 3, 5, 5],
            [1, 7, 9, 8, 5],
            [3, 8, 6, 4, 10],
            [6, 3, 9, 7, 8],
        ],
        67,
        id='it should find the path with the maximum cost'
    )
])
def test_find_best_path_in_grid(grid, expected):
    assert chapter_6.find_best_path_in_grid(grid) == expected


@pytest.mark.parametrize('weights, expected', [
    pytest.param(
        [1, 3, 3, 5],
        {0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12},
        id='it should return all possible sums'
    )
])
def test_knapsack_sums(weights, expected):
    assert chapter_6.find_knapsack_sums(weights) == expected


@pytest.mark.parametrize('max_weight, weights, expected', [
    pytest.param(
        12,
        [2, 3, 4, 5, 9],
        2,
        id='it should return minimum number of rides'
    ),
    pytest.param(
        12,
        [],
        0,
        id="it should zero if there's no people",
    ),
])
def test_get_min_num_rides(max_weight, weights, expected):
    assert chapter_6.get_min_num_rides(max_weight, weights) == expected
