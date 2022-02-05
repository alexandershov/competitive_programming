import pytest

from competitive_programming import chapter_8


@pytest.mark.parametrize('left, right, expected', [
])
def test_get_hamming_distance(left, right, expected):
    assert chapter_8.get_hamming_distance(left, right) == expected
