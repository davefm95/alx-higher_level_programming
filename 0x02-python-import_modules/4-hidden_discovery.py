#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lst = dir(hidden_4)
    for i in range(0, len(lst)):
        if not lst[i].startswith("__"):
            print("{:s}".format(lst[i]))
