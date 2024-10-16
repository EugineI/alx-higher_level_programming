#!/usr/bin/python3
"""
defines a student
"""


class Student():
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initialisation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        converts class obj to json
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in
                    attrs if isinstance(key, str) and hasattr(self, key)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces student attributes with values from a dictionary
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
