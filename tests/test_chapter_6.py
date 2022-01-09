import pytest

from competitive_programming import chapter_6


@pytest.mark.parametrize('coins, amount, expected', [
])
def test_solve_coins_problem(coins, amount, expected):
    assert sorted(chapter_6.solve_coins_problem(coins, amount)) == sorted(expected)
