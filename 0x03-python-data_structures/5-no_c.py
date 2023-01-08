#!/usr/bin/python3
def no_c(my_string):
    lst = [letter for letter in my_string]
    for i in lst:
        if ord(i) == ord('c') or ord(i) == ord('C'):
            lst.remove(i)
    new_str = "".join(lst)
    return new_str
