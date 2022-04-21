import pytest

from competitive_programming import chapter_14


@pytest.mark.parametrize('left, right, expected', [
])
def test_find_longest_common_subsequence(left, right, expected):
    assert chapter_14.find_longest_common_subsequence(left, right) == expected
