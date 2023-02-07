#!/usr/bin/python3
"""This module returns an object (Python data structure) rep by json str """
import json


def from_json_string(my_str):
    """This function returns obj rep by json"""
    return json.loads(my_str)
