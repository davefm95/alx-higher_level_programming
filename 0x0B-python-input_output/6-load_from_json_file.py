#!/usr/bin/python3
"""This module loads an obj from a json file"""
import json


def load_from_json_file(filename):
    """This func loads an obj from a json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
