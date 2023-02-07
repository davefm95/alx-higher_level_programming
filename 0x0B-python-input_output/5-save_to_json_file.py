#!/usr/bin/python3
"""This module saves a json string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """This func saves a jsoj str to a file"""
    st = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(st)
