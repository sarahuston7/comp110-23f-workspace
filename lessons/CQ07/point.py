"""Pracitce with coordinates."""

from __future__ import annotations

__author__ = "730459812"


class Point:
    """Creates a two dim point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Mutates a coordinate."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new scaled point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point