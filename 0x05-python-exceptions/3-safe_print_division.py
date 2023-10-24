#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sums = a / b
    except ZeroDivisionError:
        sums = None
    finally:
        print("Inside result: {}".format(sums))
        return sums
