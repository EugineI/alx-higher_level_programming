#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

try:
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)
    my_rectangle.width = -6
    my_rectangle.height = 4
    print(my_rectangle.__dict__)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
