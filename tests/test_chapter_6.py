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
        id='it should return None if there\'s no solution'
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
])
def find_longest_increasing_subsequence(seq, expected):
    assert chapter_6.find_longest_increasing_subsequence(seq) == expected
