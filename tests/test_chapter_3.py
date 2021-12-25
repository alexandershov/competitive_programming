from competitive_programming import chapter_3, chapter_2

import pytest


@pytest.mark.parametrize('n, x, expected', [
    # num_calls = (n^x - 1) / (n - 1)
    (2, 1, 1),
    (2, 2, 3),
    (2, 3, 7),
    (2, 10, 1023),
    (3, 3, 13),
    (4, 3, 21),
])
def test_recursive_num_calls(n, x, expected):
    actual = len(list(chapter_3.n_ary_function(n, x)))
    assert actual == expected


@pytest.mark.parametrize('seq, expected', [
    pytest.param(
        [],
        0,
        id='should return 0 on an empty array'
    ),
    pytest.param(
        [1, 2, 3],
        6,
        id='should return sum of the whole array when array has only positive numbers'
    ),
    pytest.param(
        [-2, -1, -3],
        -1,
        id='should pick the maximum element when array has only negative numbers'
    ),
    pytest.param(
        [-1, 2, 4, -3, 5, 2, -5, 2],
        10,
        id='should work on the test case from the book'
    )
])
def test_get_max_subarray_sum(max_subarray_sum_algo, seq, expected):
    actual = max_subarray_sum_algo(seq)
    assert actual == expected


@pytest.fixture(params=[
    chapter_3.get_max_subarray_sum_cubic,
    chapter_3.get_max_subarray_sum_quadratic,
    chapter_3.get_max_subarray_sum_linear
])
def max_subarray_sum_algo(request):
    return request.param


@pytest.mark.parametrize('size, expected', [
    (1, 0),
    (2, 0),
    (3, 8),
    (4, 44),
    (5, 140),
    (6, 340),
    (7, 700),
    (8, 1288),
])
def test_solve_two_queens_problem(solve_two_queens_problem_algo, size, expected):
    assert solve_two_queens_problem_algo(size) == expected


@pytest.fixture(params=[
    chapter_3.solve_two_queens_problem_brute_force,
])
def solve_two_queens_problem_algo(request):
    return request.param


@pytest.mark.parametrize('column, row, size, expected', [
    pytest.param(
        0, 0, 6, 6,
        id='should return maximum diagonal length'
    ),
    pytest.param(
        5, 5, 6, 1,
        id='should return minimum diagonal length'
    ),
    pytest.param(
        0, 5, 6, 1,
        id='should stop when runs out of rows first'
    ),
    pytest.param(
        5, 0, 6, 1,
        id='should stop when runs out of columns first'
    )
])
def test_get_up_diagonal_length(column, row, size, expected):
    square = chapter_2.Square(column, row, size)
    assert chapter_3.get_up_diagonal_length(square) == expected


@pytest.mark.parametrize('column, row, size, expected', [
    pytest.param(
        0, 5, 6, 6,
        id='should return maximum diagonal length'
    ),
    pytest.param(
        5, 0, 6, 1,
        id='should return minimum diagonal length'
    ),
    pytest.param(
        0, 0, 6, 1,
        id='should stop when runs out of rows first'
    ),
    pytest.param(
        5, 5, 6, 1,
        id='should stop when runs out of columns first'
    )
])
def test_get_down_diagonal_length(column, row, size, expected):
    square = chapter_2.Square(column, row, size)
    assert chapter_3.get_down_diagonal_length(square) == expected
