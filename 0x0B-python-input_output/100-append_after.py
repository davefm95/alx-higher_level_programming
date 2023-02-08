#!/usr/bin/python
"""This is the 100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """This func appends text after specified string"""
    text = []
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line != "":
            text.append(line)
            line = f.readline()
    for i in range(len(text)):
        if search_string in text[i]:
            i += 1
            text.insert(i, new_string)
    with open(filename, "w", encoding='utf-8') as f:
        for st in text:
            f.write(st)
