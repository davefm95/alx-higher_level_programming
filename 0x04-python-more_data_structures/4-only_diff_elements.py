#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_set = set(filter(lambda st: st not in set_1, set_2))
    d_set = set(filter(lambda st: st not in set_2, set_1))
    return c_set | d_set
