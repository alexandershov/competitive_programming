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
])
def test_count_subgrids(grid, expected):
    assert chapter_8.count_subgrids(grid) == expected
