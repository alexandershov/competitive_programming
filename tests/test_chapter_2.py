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


@pytest.mark.parametrize('seq, expected', [
    ([], [[]]),
    ([1], [[1]]),
    ([1, 2], [[1, 2], [2, 1]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
])
def test_permutations(permutations_algo, seq, expected):
    actual = list(permutations_algo(seq))
    assert sorted(actual) == sorted(expected)


@pytest.fixture(params=[
    chapter_2.naive_subsets,
    chapter_2.rec_subsets,
    chapter_2.rec_efficient_subsets,
    chapter_2.iter_subsets,
    chapter_2.iter_efficient_subsets])
def subsets_algo(request):
    return request.param


@pytest.fixture(params=[
    chapter_2.rec_permutations,
    chapter_2.iter_permutations,
])
def permutations_algo(request):
    return request.param


def assert_same_sets(actual_sets, expected):
    actual = collections.Counter(actual_sets)
    expected = collections.Counter(map(frozenset, expected))
    assert actual == expected


@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
])
def test_solve_queen_problem(n, expected):
    actual = len(list(chapter_2.solve_queen_problem(n)))
    assert actual == expected


@pytest.mark.parametrize('column, row, expected', [
    (0, 0, 0),
    (1, 0, 1),
    (2, 0, 2),
    (0, 1, 1),
    (1, 1, 2),
    (2, 1, 3),
    (0, 2, 2),
    (1, 2, 3),
    (2, 2, 4),
])
def test_get_down_diagonal(column, row, expected):
    actual = chapter_2.get_down_diagonal(column, row)
    assert actual == expected


@pytest.mark.parametrize('column, row, expected', [
    (0, 0, 2),
    (1, 0, 3),
    (2, 0, 4),
    (0, 1, 1),
    (1, 1, 2),
    (2, 1, 3),
    (0, 2, 0),
    (1, 2, 1),
    (2, 2, 2),
])
def test_get_up_diagonal(column, row, expected):
    actual = chapter_2.get_up_diagonal(column, row, 3)
    assert actual == expected


@pytest.mark.parametrize('number, expected', [
    (0, '0'),
    (1, '1'),
    (2, '10'),
    (4, '100'),
    (15, '1111'),
])
def test_binary(number, expected):
    assert chapter_2.binary(number) == expected
