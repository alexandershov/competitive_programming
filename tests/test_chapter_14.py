import pytest

from competitive_programming import chapter_14


@pytest.mark.parametrize('left, right, expected', [
    pytest.param(
        'tour', 'opera',
        'or',
        id='it should return longest common subsequence'
    ),
    pytest.param(
        '', 'opera',
        '',
        id='it should return an empty string if left is empty'
    ),
    pytest.param(
        'tokurz', 'zuvrxzok',
        'urz',
        id='it should not fail into local maximum trap'
    ),
])
def test_find_longest_common_subsequence(left, right, expected):
    assert chapter_14.find_longest_common_subsequence(left, right) == expected
