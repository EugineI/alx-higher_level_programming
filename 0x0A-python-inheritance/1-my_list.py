#!/usr/bin/python3
"""
This module describe a class inheriting from another.
"""


class MyList(list):
    """
    This class inherits from class list
    """
    def print_sorted(self):
        """
        prints sorted version of list
        """
        print(sorted(self))
