#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = set(filter(lambda st: st in set_1, set_2))
    return c_set
