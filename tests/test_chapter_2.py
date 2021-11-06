from competitive_programming import chapter_2

import pytest


@pytest.mark.parametrize('n, modulo, expected', [
])
def test_factorial_modulo(n, modulo, expected):
    assert chapter_2.factorial_modulo(n, modulo) == expected
