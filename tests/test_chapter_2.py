import math

import pytest
from competitive_programming import chapter_2


@pytest.mark.parametrize('n, modulo', [
    (5, 121),
    (5, 7),
    (900, 23422342),
    (1001, 23422342),
])
def test_factorial_modulo(n, modulo):
    expected = math.factorial(n) % modulo
    assert chapter_2.factorial_modulo(n, modulo) == expected


@pytest.mark.parametrize('seq, n, expected', [
    ([], 0, [[]]),
    ([1], 1, [[1]]),
    ([1, 2], 1, [[1], [2]]),
    ([1, 2], 2, [[1, 2]]),
    ([1, 2, 3], 2, [[1, 2], [2, 3], [1, 3]]),
])
def test_iter_combinations(seq, n, expected):
    actual = set(chapter_2.iter_combinations(seq, n))
    expected = set(map(frozenset, expected))
    assert actual == expected


@pytest.mark.parametrize('seq, expected', [
    ([], [[]]),
    ([1], [[], [1]]),
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]),
])
def test_iter_subsets(seq, expected):
    actual = set(chapter_2.iter_subsets(seq))
    expected = set(map(frozenset, expected))
    assert actual == expected
