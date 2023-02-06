#!/usr/bin/python3
"""This module contains the is_kind_of_class_function"""


def is_kind_of_class(obj, a_class):
    """This function checks if obj is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
