import math

import pytest
from competitive_programming import chapter_2


@pytest.mark.parametrize('n, modulo', [
    (5, 121),
    (5, 7),
    (2000, 23422342),
])
def test_factorial_modulo(n, modulo):
    expected = math.factorial(n) % modulo
    assert chapter_2.factorial_modulo(n, modulo) == expected
