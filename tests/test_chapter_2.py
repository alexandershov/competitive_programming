import collections
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
    ([], 1, []),
    ([1], 1, [[1]]),
    ([1, 2], 1, [[1], [2]]),
    ([1, 2], 2, [[1, 2]]),
    ([1, 2, 3], 2, [[1, 2], [2, 3], [1, 3]]),
])
def test_combinations(seq, n, expected):
    assert_same_sets(chapter_2.combinations(seq, n), expected)


@pytest.mark.parametrize('seq, expected', [
    ([], [[]]),
    ([1], [[], [1]]),
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]),
])
def test_subsets(subsets_algo, seq, expected):
    assert_same_sets(subsets_algo(seq), expected)


@pytest.fixture(params=[
    chapter_2.naive_subsets,
    chapter_2.rec_subsets,
    chapter_2.rec_efficient_subsets,
    chapter_2.iter_subsets,
    chapter_2.iter_efficient_subsets])
def subsets_algo(request):
    return request.param


def assert_same_sets(actual_sets, expected):
    actual = collections.Counter(actual_sets)
    expected = collections.Counter(map(frozenset, expected))
    assert actual == expected
