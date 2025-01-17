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

    def to_json(self):
        """
        converts class obj to json
        """
        return self.__dict__
