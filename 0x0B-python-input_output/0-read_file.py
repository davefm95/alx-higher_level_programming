#!/usr/bin/python3
"""This module reads from a file"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    print(data, end="")
