import pytest

from competitive_programming import chapter_13


@pytest.mark.parametrize('line, point, expected', [
])
def test_get_point_side(line, point, expected):
    assert chapter_13.get_point_side(line, point) == expected
