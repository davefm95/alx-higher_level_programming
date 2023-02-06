#!/usr/bin/python3
"""Thsis the 4-inherits module"""


def inherits_from(obj, a_class):
    if issubclass(obj, a_class):
        return True
    else:
        return False
