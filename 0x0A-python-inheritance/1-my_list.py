#!/usr/bin/python3
"""This moduoe contains a class that inherits from the liat object
"""


class MyList(list):
    def print_sorted(self):
        """This function prints the sprted list"""
        print("{}".format(sorted(self)))
