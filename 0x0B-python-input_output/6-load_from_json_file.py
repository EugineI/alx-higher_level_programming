#!/usr/bin/python3
"""
create an object with json
"""
import json


def load_from_json_file(filename):
    """
    create an object from json file
    """
    with open(filename, "r") as f:
        return json.load(f)
