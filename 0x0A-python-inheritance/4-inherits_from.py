#!/usr/bin/python3
"""Thsis the 4-inherits module"""


def inherits_from(obj, a_class):
    """This func checks if ob is a subclass of a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
