#!/usr/bin/python3
"""
converts json string to python object
"""
import json


def from_json_string(my_str):
    """
    Return: string
    """
    return json.loads(my_str)
