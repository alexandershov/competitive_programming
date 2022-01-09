import pytest

from competitive_programming import chapter_6


@pytest.mark.parametrize('coins, amount, expected', [
    # TODO: what if there's no solution?, what if solution is empty?
    pytest.param(
        {100, 99, 6, 1},
        105,
        [99, 6],
        id='it should pick the minimum amount of coins'
    )
])
def test_solve_coins_problem(coins, amount, expected):
    assert sorted(chapter_6.solve_coins_problem(coins, amount)) == sorted(expected)
