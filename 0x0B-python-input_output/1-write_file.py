#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """This func writes to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
