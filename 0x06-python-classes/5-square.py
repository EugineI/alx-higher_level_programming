#!/usr/bin/python3
"""
This module handles basic square operations

It will contain functions and classes to handle calculation of the square area.
"""


class Square:
    """
    defines a square
    """
    def __init__(self, size=0):
        """
        initialises the attribute size
        """
        self.__size = size

    @property
    def size(self):
        """
        retrieves the attribute size
        """
        length = self.__size
        return length

    @size.setter
    def size(self, value):
        """
        sets the attribute size to value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return: area of the square
        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """
        prints the square using '#'
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
