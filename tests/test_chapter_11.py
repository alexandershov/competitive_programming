import pytest

from competitive_programming import chapter_11


@pytest.mark.parametrize('number, expected', [
    pytest.param(0, False, id='it should return False for 0'),
    pytest.param(1, False, id='it should return False for 1'),
    pytest.param(2, True, id='it should return True for 2'),
    pytest.param(3, True, id='it should return True for 3'),
    pytest.param(4, False, id='it should return False for 4'),
    pytest.param(47, True, id='it should return True for 47'),
    pytest.param(16, False, id='it should return False for 16'),
    pytest.param(234234811, True, id='it should return True for 234234811'),
    pytest.param(23497 * 23581, False, id='it should return True for 23497 * 23581'),
])
def test_is_prime(number, expected):
    assert chapter_11.is_prime(number) is expected


@pytest.mark.parametrize('number, expected', [
    pytest.param(2, [2], id='it should the number itself for any prime number'),
    pytest.param(12, [2, 2, 3], id='it should return prime factorization for composite number'),
    pytest.param(23497, [23497], id='it should return the number itself for any prime number'),
    pytest.param(23497 * 23581, [23497, 23581],
                 id='it should return prime factorization for large composite number'),
])
def test_factorize(number, expected):
    assert_same_items(chapter_11.factorize(number), expected)


def assert_same_items(actual, expected):
    assert sorted(actual) == sorted(expected)


@pytest.mark.parametrize('length, expected', [
    pytest.param(
        0,
        [],
        id='it should return empty list when length is 0'
    ),
    pytest.param(
        14,
        [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        id='it should return Eratosthenes sieve of the given length'
    )
])
def test_eratosthenes_sieve(length, expected):
    assert chapter_11.build_eratosthenes_sieve(length) == expected


@pytest.mark.parametrize('x, y, expected', [
    pytest.param(
        200, 150,
        50,
        id='it should return the greatest common divisor of two numbers'
    ),
    pytest.param(
        11, 37,
        1,
        id='it should return 1 if both numbers are unequal primes'
    ),
    pytest.param(
        11, 11,
        11,
        id='it should return the number if both numbers are the same'
    )
])
def test_gcd(x, y, expected):
    assert chapter_11.gcd(x, y) == expected
