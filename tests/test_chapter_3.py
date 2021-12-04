from competitive_programming import chapter_3

import pytest


@pytest.mark.parametrize('n, x, expected', [
    # num_calls = (n^x - 1) / (n - 1)
    (2, 1, 1),
    (2, 2, 3),
    (2, 3, 7),
    (2, 10, 1023),
    (3, 3, 13)
])
def test_recursive_num_calls(n, x, expected):
    actual = len(list(chapter_3.n_ary_function(n, x)))
    assert actual == expected
