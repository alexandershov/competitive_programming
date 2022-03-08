import pytest

from competitive_programming import chapter_11


@pytest.mark.parametrize('number, expected', [
])
def test_is_prime(number, expected):
    assert chapter_11.is_prime(number) is expected
