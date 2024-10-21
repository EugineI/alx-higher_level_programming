#!/usr/bin/python3
"""
creates the base class
"""
import json
import os

class Base():
    """
    base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        converts dictionary to json
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        json to file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as f:
            f.write(json_string)

    def from_json_string(json_string):
        """
        json to dictionary
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load from a file
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_string = f.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
