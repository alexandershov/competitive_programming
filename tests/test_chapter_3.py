from competitive_programming import chapter_3

import pytest


@pytest.mark.parametrize('function, n, expected', [
])
def test_recursive_num_calls(function, n, expected):
    actual = len(list(function(n)))
    assert actual == expected
