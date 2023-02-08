#!/usr/bin/python3
"""This module returns a list of lists rep pascal triangle"""


def pascal_triangle(n):
    """Return lists of list pascal triangle"""
    pt = []
    for i in range(n):
        if i == 0:
            pt.append([1])
        else:
            row = pt[i - 1] + [0]
            temp = row[:]
            for num in range(1, len(row)):
                row[num] = temp[num - 1] + temp[num]
            pt.append(row)
    return pt
