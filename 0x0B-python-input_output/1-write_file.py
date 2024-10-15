#!/usr/bin/python3
"""
opens a file and writes on it
"""


def write_file(filename="", text=""):
    """
    Returns: number of bytes written
    """
    with open(filename, "w") as f:
        return f.write(text)
