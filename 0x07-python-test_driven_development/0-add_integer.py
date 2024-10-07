#!/usr/bin/python3
"""
This module adds two integers
"""
def add_integer(a, b=98):
    """
    this function takes two integers
    returns the sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
