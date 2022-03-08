import pytest

from competitive_programming import chapter_11


@pytest.mark.parametrize('number, expected', [
    pytest.param(2, True, id='it should return True for 2'),
    pytest.param(47, True, id='it should return True for 47'),
    pytest.param(16, False, id='it should return False for 16'),
    pytest.param(234234811, True, id='it should return True for 234234811'),
    pytest.param(23497 * 23581, False, id='it should return True for 23497 * 23581'),
])
def test_is_prime(number, expected):
    assert chapter_11.is_prime(number) is expected
