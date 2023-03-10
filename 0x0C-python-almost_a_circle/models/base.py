#!/usr/bin/python3
"""This module contains class base"""
import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This functiom inits base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string of argument"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json string to file"""
        if list_objs is None:
            st = "[]"
        else:
            ld = []
            for obj in list_objs:
                ld.append(obj.to_dictionary())
            st = cls.to_json_string(ld)
        name = cls.__name__
        name += ".json"
        with open(name, "w", encoding="utf-8") as f:
            f.write(st)

    @staticmethod
    def from_json_string(json_string):
        """returns objevt"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an Instance"""
        if cls.__name__ == "Rectangle":
            self = cls(1, 1)
        else:
            self = cls(1)
        self.update(**dictionary)
        return self

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
