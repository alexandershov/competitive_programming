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
    # TODO: rename a & b
    a: Point
    b: Point


def get_point_side(line: Line, point: Point) -> str:
    first = line.b - line.a
    second = point - line.b
    cross_product = first * second
    if cross_product > 0:
        return 'left'
    elif cross_product < 0:
        return 'right'
    return 'center'
