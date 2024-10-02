#!/usr/bin/python3
"""
This module handles basic square operations

It will contain functions and classes to handle calculation of the square area.
"""


class Square:
    """
    This class defines a square and finds its area
    """
    def __init__(self, size=0):
        """
        initialises the attributes
        size: int
        length of the squares side
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        finds area of the square
        Return:
        area of the square
        """
        length = self.__size
        area = length ** 2
        return area
