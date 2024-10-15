#!/usr/bin/python3
"""
append test on a file
"""


def append_write(filename="", text=""):
    """
    Return: number of bytes appended
    """
    with open(filename, "a") as f:
        return f.write(text)
