#!/usr/bin/python3
"""
checking for instances of a class
"""
def is_same_class(obj, a_class):
    """
    checks if object is instance of a class
    Return: true or false
    """
    return type(obj) is a_class
