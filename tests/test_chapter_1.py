import pytest
from competitive_programming import chapter_1


@pytest.mark.parametrize('n, expected', [
    (2, [2, 1]),
    (1, [1]),
    (3, [3, 10, 5, 16, 8, 4, 2, 1]),
])
def test_weird_algorithm(n, expected):
    assert chapter_1.weird_algorithm(n) == expected
