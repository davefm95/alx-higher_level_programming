#!/usr/bin/python3
"""This module defines a Student class"""


class Student:
    """Defines Student class"""
    def __init__(self, first_name, last_name, age):
        """Inits Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict of student class"""
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for at in attrs:
                for key, value in self.__dict__.items():
                    if at == key:
                        dic[key] = value
                        break
            return dic
