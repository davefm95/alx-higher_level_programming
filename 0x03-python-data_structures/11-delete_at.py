#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    if idx <= 0:
        return my_list
    my_list[idx:(idx + 1)] = []
    return my_list
