from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Line:
    a: Point
    b: Point


def get_point_side(line: Line, point: Point) -> str:
    return None
