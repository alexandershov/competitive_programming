from competitive_programming import chapter_9

import pytest


@pytest.mark.parametrize('seq, first, last, expected', [
    pytest.param(
        [8, 10, 12, 6, 7], 1, 3,
        28,
        id='it should return sum of elements in the range [first; last]'
    ),
    pytest.param(
        [8, 10, 12, 6, 7], 1, 1,
        10,
        id='it should return seq[first] when first==last'
    ),
])
def test_get_range_sum(seq, first, last, expected):
    assert chapter_9.get_range_sum(seq, first, last) == expected


@pytest.mark.parametrize('seq, first, last, expected', [
    pytest.param(
        [8, 10, 12, 6, 7], 1, 3,
        6,
        id='it should return the minimum value in range'
    )
])
def test_get_range_min(seq, first, last, expected):
    assert chapter_9.get_range_min(seq, first, last) == expected
