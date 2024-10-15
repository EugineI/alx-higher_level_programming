#!/usr/bin/python3
"""
reads from a file
"""


def read_file(filename=""):
    """
    opens a file to read on it and print its conted on console
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
        f.close()
