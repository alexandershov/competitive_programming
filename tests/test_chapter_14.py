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
        'tour', '',
        '',
        id='it should return an empty string if right is empty'
    ),
    pytest.param(
        'tokurz', 'zuvrxzok',
        'urz',
        id='it should not fail into local maximum trap'
    ),
])
def test_find_longest_common_subsequence(left, right, expected):
    assert chapter_14.find_longest_common_subsequence(left, right) == expected


@pytest.mark.parametrize('left, right, expected', [
    pytest.param(
        'test', 'ktes',
        2,
        id='it should return minimum edit distance between two words',
    ),
    pytest.param(
        'test', '',
        4,
        id='it should return length of string if the goal is empty',
    ),
])
def test_find_minimum_edit_distance(left, right, expected):
    assert chapter_14.find_minimum_edit_distance(left, right) == expected
