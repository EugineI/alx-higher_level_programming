#!/usr/bin/python3
"""
This module handles basic square operations

It will contain functions and classes to handle calculation of the square area.
"""


class Square:
    """
    this class defines a square
    """
    def __init__(self, size=0):
        """
        This function initialises the attributes
        size: int
        length of the squares side
        raises:
        TypeError and ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
