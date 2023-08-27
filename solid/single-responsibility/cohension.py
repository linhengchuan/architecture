"""
The responsibility is split up for the different class instead of clustering everything in a single Circle class.
"""
import math


class Circle():
    """
    Measurement of circle
    """
    def calculate_area(radius):
        return math.pi * radius * radius

    def calculate_circumference(radius):
        return math.pi * radius * 2


class CircleUI():
    """
    Rendering of circle
    """
    def draw():
        pass
