#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_ = set(my_list)
    sum_ = 0
    for num in set_:
        sum_ += num
    return sum_
