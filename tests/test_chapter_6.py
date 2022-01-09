import pytest

from competitive_programming import chapter_6


@pytest.mark.parametrize('coins, amount, expected', [
    # TODO: what if there's no solution?, what if solution is empty?
    pytest.param(
        {100, 99, 6, 1},
        105,
        [99, 6],
        id='it should pick the minimum amount of coins'
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


def try_sorted(opt_seq):
    if opt_seq is None:
        return None
    return sorted(opt_seq)
