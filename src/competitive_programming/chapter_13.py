from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __mul__(self, other: Point) -> float:
        return self.x * other.y - other.x * self.y

    def __sub__(self, other: Point) -> Point:
        return Point(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass(frozen=True)
class Line:
    begin: Point
    end: Point


def get_point_side(line: Line, point: Point) -> str:
    first = line.end - line.begin
    second = point - line.end
    cross_product = first * second
    if cross_product > 0:
        return 'left'
    elif cross_product < 0:
        return 'right'
    return 'center'


def segments_intersect(first: Line, second: Line) -> bool:
    # TODO: improve code
    if are_collinear(first, second):
        first_xs = sorted([first.begin.x, first.end.x])
        second_xs = sorted([second.begin.x, second.end.x])
        return second_xs[0] <= first_xs[0] <= second_xs[1] or first_xs[0] <= second_xs[0] <= \
               first_xs[1]
    if get_point_side(first, second.begin) == get_point_side(first, second.end):
        return False
    if get_point_side(second, first.begin) == get_point_side(second, first.end):
        return False
    return True


def are_collinear(first, second):
    return get_point_side(first, second.begin) == 'center' and get_point_side(first,
                                                                              second.end) == 'center'
