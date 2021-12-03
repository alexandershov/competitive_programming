from competitive_programming import chapter_3

import pytest


@pytest.mark.parametrize('function, n, expected', [
    (chapter_3.binary_function, 1, 1),
    (chapter_3.binary_function, 2, 3),
    (chapter_3.binary_function, 3, 7),
    (chapter_3.binary_function, 10, 1023),
])
def test_recursive_num_calls(function, n, expected):
    actual = len(list(function(n)))
    assert actual == expected
