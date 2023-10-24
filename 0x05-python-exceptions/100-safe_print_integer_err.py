#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as t:
        print("Exception: {}".format(t))
        return False
