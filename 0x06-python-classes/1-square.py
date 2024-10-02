#!/usr/bin/python3
"""
This module handles basic square operations

It will contain functions and classes to handle calculation of the square area.
"""


class Square:
    """
    This class defines a square
    """
    def __init__(self, size):
        """
        Initializes all the attributes needed

        size : int
            the length of the square
        """
        self.__size = size
