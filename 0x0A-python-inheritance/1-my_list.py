#!/usr/bin/python3
"""
This module describe a class inheriting from another.
"""


class MyList(list):
    """
    This class inherits from class list
    """
    def print_sorted(self):
        print(sorted(self))
