#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for item in range(x):
        try:
            print("{}".format(my_list[item]), end="")
        except Exception:
            print("")
            return item
    print("")
    return item + 1
