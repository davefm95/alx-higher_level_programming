#!/usr/bin/python3
"""This module contains class base"""


class Base:
    """This is the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """This functiom inits base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
