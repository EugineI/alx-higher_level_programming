#!/usr/bin/python3
"""
Rectangle class that inherits fro  Base
"""
from models.base import Base
import json


class Rectangle(Base):
    """
    class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        gets width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        retrieves width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        retrieves height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        gets x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        gets y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        displays area with #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """overide the __str__ method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
 {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        updates arguments
        """
        if args and len(args) > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        to dictionary
        """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
