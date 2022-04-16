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
    if are_collinear(first, second):
        return one_dimensional_intersect(get_sorted_xs(first), get_sorted_xs(second))
    if get_point_side(first, second.begin) == get_point_side(first, second.end):
        return False
    if get_point_side(second, first.begin) == get_point_side(second, first.end):
        return False
    return True


def one_dimensional_intersect(first: list[float], second: list[float]) -> bool:
    if second[0] <= first[0] <= second[1]:
        return True
    if first[0] <= second[0] <= first[1]:
        return True
    return False


def get_sorted_xs(line: Line) -> list[float]:
    return sorted([line.begin.x, line.end.x])


def are_collinear(first, second):
    begin_side = get_point_side(first, second.begin)
    end_side = get_point_side(first, second.end)
    return begin_side == 'center' and end_side == 'center'
