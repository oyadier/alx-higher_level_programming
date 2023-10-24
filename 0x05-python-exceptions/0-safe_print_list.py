#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    _len = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            _len += 1
    except IndexError:
        pass
    print();
    return _len
