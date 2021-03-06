import pytest

from competitive_programming import chapter_8


@pytest.mark.parametrize('left, right, expected', [
    pytest.param(
        '01101',
        '11001',
        2,
        id='it should return number of different bits in strings'
    )
])
def test_get_hamming_distance(left, right, expected):
    assert chapter_8.get_hamming_distance(left, right) == expected


@pytest.mark.parametrize('strings, expected', [
    pytest.param(
        [
            '00111',
            '01101',
            '11110',
        ],
        2,
        id='it should return the minimum Hamming distance between all pairs of strings'
    )
])
def test_get_minimum_hamming_distance(strings, expected):
    assert chapter_8.get_minimum_hamming_distance(strings) == expected


@pytest.mark.parametrize('grid, expected', [
    pytest.param(
        [
            [0, 1, 0, 0, 1],
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
        ],
        2,
        id='it should return the count of subgrids'
    )
])
def test_count_subgrids(grid, expected):
    assert chapter_8.count_subgrids(grid) == expected


@pytest.mark.parametrize('seq, sum_, expected', [
    pytest.param(
        [8, 6, 4, 3, 5], 13,
        [6, 4, 3],
        id='it should find subarray with the given sum'
    ),
    pytest.param(
        [8, 6, 4, 3, 5], 18,
        [8, 6, 4],
        id='it should find subarray when sum is prefix sum'
    ),
    pytest.param(
        [8, 6, 4, 3, 5], 12,
        [4, 3, 5],
        id='it should find subarray when sum is suffix sum'
    ),
    pytest.param(
        [8, 6, 4, 3, 5], 0,
        [],
        id='it should return an empty list when given zero sum'
    ),
    pytest.param(
        [8, 6, 4, 3, 5], 15,
        None,
        id="it should return None when sum can't be found"
    )

])
def test_find_sum(seq, sum_, expected):
    assert chapter_8.find_sum(seq, sum_) == expected


@pytest.mark.parametrize('seq, sum_, expected', [
    pytest.param(
        [8, 6, 4, 3, 5], 10,
        [4, 6],
        id='it should return two elements that together give sum_'
    ),
    pytest.param(
        [8, 6, 4, 3, 5], 15,
        None,
        id='it should None if no two elements together give sum_'
    ),
])
def test_find_2_sum(seq, sum_, expected):
    assert chapter_8.find_2_sum(seq, sum_) == expected


@pytest.mark.parametrize('seq, window_size, expected', [
    pytest.param(
        [8, 9, 10, 11, 12, 3, 8, 9, 4], 3,
        [8, 9, 10, 3, 3, 3, 4],
        id='it should return sliding window minimums'
    ),
    pytest.param(
        [8, 1, 3], 1,
        [8, 1, 3],
        id='it return the original list when window_size == 1'
    ),
    pytest.param(
        [8, 1, 3], 3,
        [1],
        id='it return the list minimum when window_size == len(seq)'
    ),
])
def test_get_sliding_minimums(seq, window_size, expected):
    assert chapter_8.get_sliding_minimums(seq, window_size) == expected
