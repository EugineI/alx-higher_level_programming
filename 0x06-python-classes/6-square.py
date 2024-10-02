#!/usr/bin/python3
"""
This module handles basic square operations
It will contain functions and classes to handle calculation of the square area.
"""


class Square:
    """
    Defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialises attributes size and position
        position: turple
        size: int
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        retrieves size
        """
        length = self.__size
        return length

    @size.setter
    def size(self, value):
        """
        sets size to value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        retrieves position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets position to value
        """
        if not isinstance(value, tuple) or len(value) != 2 or not \
                all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return: area of the square
        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """
        prints square
        """
        if self.__size == 0:
            print("")
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
