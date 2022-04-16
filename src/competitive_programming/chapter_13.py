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
        first_xs = get_sorted_xs(first)
        second_xs = get_sorted_xs(second)
        return one_dimensional_intersect(first_xs, second_xs)
    if get_point_side(first, second.begin) == get_point_side(first, second.end):
        return False
    if get_point_side(second, first.begin) == get_point_side(second, first.end):
        return False
    return True


def one_dimensional_intersect(first: list[float], second: list[float]) -> bool:
    return second[0] <= first[0] <= second[1] or first[0] <= second[0] <= \
           first[1]


def get_sorted_xs(line: Line) -> list[float]:
    return sorted([line.begin.x, line.end.x])


def are_collinear(first, second):
    return get_point_side(first, second.begin) == 'center' and get_point_side(first,
                                                                              second.end) == 'center'
