#!/usr/bin/python3
"""This module contains a funct that append sto a file"""


def append_write(filename="", text=""):
    """This func appends to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
