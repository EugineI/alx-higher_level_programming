#!/usr/bin/python3
"""
This module defines a rectangle with width and height
"""


class Rectangle:
    """
    This is a rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        this function initialises the rectangle with:
        width and height
        """
        self._width = width
        self._height = height

    @property
    def height(self):
        """
        retrieves the attribute height
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        This method sets the height to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    @property
    def width(self):
        """
        Retrieves the width attribute
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def area(self):
        """
        This method culculates the area of the rectangle
        """
        return self._width * self._height

    def perimeter(self):
        """
        This method culculates the perimeter of the rectangle
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        rectangle = []
        for _ in range(self._height):
            rectangle.append('#' * self._width)
        return "\n".join(rectangle)
