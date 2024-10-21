#!/usr/bin/python3
"""
square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing objects
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overide the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} -\
 {self.width}"

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates arguments
        """
        if args and len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
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
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
