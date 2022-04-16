import pytest

from competitive_programming import chapter_13
from competitive_programming.chapter_13 import Point
from competitive_programming.chapter_13 import Line


@pytest.mark.parametrize('line, point, expected', [
    pytest.param(
        Line(Point(1, 1), Point(3, 3)), Point(2, 3),
        'left',
        id='it should return "left" when point is located on the left side of the line'
    ),
    pytest.param(
        Line(Point(3, 3), Point(1, 1)), Point(2, 3),
        'right',
        id='it should return "right" when point is located on the right side of the line'
    ),
    pytest.param(
        Line(Point(1, 1), Point(3, 3)), Point(2, 2),
        'center',
        id='it should return "center" when point is located on the line'
    )
])
def test_get_point_side(line, point, expected):
    assert chapter_13.get_point_side(line, point) == expected


@pytest.mark.parametrize('first, second, expected', [
    pytest.param(
        Line(Point(1, 1), Point(3, 3)),
        Line(Point(3, 1), Point(1, 3)),
        True,
        id='it should return True when two line segments intersect'
    ),
    pytest.param(
        Line(Point(1, 1), Point(3, 3)),
        Line(Point(5, 3), Point(3, 5)),
        False,
        id='it should return False when two line segments intersect'
    ),
    pytest.param(
        Line(Point(1, 1), Point(3, 3)),
        Line(Point(2, 2), Point(3, 1)),
        True,
        id='it should return True when two segments have one common point'
    )
])
def test_segments_intersect(first, second, expected):
    assert chapter_13.segments_intersect(first, second) is expected
