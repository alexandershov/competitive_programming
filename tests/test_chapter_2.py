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


@pytest.mark.parametrize('seq, expected', [
])
def test_subsets(seq, expected):
    actual = chapter_2.iter_subsets(seq)
    assert_same_subsets(actual, expected)


def assert_same_subsets(actual, expected):
    return normalized_subsets(actual) == normalized_subsets(expected)


def normalized_subsets(subsets):
    return sorted(
        sorted(subset)
        for subset in subsets
    )
