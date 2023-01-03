#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 8 and j == 9:
            break
        if j > i:
            print("{:d}{:d}".format(i, j), end=", ")
print("{:d}".format(89))
