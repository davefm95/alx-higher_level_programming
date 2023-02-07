#!/usr/bin/python3
"""This module returns am object dict representation"""


def class_to_json(obj):
    """Returns dict desc woth simple data structure"""
    return obj.__dict__
