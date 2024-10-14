#!/usr/bin/python3
"""
checking for sub classes
"""
def inherits_from(obj, a_class):
    """
    checks for subclass
    Return: true or false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
