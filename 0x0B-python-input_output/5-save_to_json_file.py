#!/usr/bin/python3
"""This module saves a json string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """This func saves a jsoj str to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
