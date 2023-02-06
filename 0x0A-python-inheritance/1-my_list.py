#!/usr/bin/python3
"""This moduoe contains a class that inherits from the liat object
"""


class MyList(list):
    """A Class that inherits from list"""
    def print_sorted(self):
        """This function prints the sprted list"""
        print(sorted(self))
