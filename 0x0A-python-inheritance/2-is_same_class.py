#!/usr/bin/python3
"""This module contains a function that checks if types"""


def is_same_class(obj, a_class):
    """This function checks if an object is of a given class"""
    if type(obj) is a_class:
        return True
    else:
        return False
