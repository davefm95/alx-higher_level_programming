#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    if len(argv) == 1:
        print("{:d}".format(add))
    elif len(argv) == 2:
        print("{:d}".format(int(argv[1])))
    else:
        for i in range(1, len(argv)):
            add += int(argv[i])
            if i == len(argv) - 1:
                print("{:d}".format(add))
