#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ac = ord(c)
        print("{:c}".format(ac - 32 if ac >= 97 and ac <= 122 else ac), end="")
    print("")
