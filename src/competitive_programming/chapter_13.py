from __future__ import annotations

import math
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

    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


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
        return (
                one_dimensional_intersect(first, second, get_dimension=get_x) and
                one_dimensional_intersect(first, second, get_dimension=get_y))
    if get_point_side(first, second.begin) == get_point_side(first, second.end):
        return False
    if get_point_side(second, first.begin) == get_point_side(second, first.end):
        return False
    return True


def one_dimensional_intersect(first: Line, second: Line, get_dimension) -> bool:
    first_values = get_sorted_dimension(first, get_dimension)
    second_values = get_sorted_dimension(second, get_dimension)
    if second_values[0] <= first_values[0] <= second_values[1]:
        return True
    if first_values[0] <= second_values[0] <= first_values[1]:
        return True
    return False


def get_sorted_dimension(line: Line, get_dimension) -> list[float]:
    return sorted(map(get_dimension, [line.begin, line.end]))


def are_collinear(first, second):
    begin_side = get_point_side(first, second.begin)
    end_side = get_point_side(first, second.end)
    return begin_side == 'center' and end_side == 'center'


def get_distance_to_line(point: Point, line: Line) -> float:
    cross_product = (point - line.begin) * (line.end - line.begin)
    return abs(cross_product) / (line.end - line.begin).magnitude()


def get_x(point: Point) -> float:
    return point.x


def get_y(point: Point) -> float:
    return point.y
