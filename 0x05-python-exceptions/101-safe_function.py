#!/usr/bin/python3
import ctypes
import sys


def safe_function(fct, *args):
    """
        a function that executes a function safely.
        I imported the ctypes header file because of the use of
        C pointers in the function parameters
    """
    result = 0
    try:
        result = fct(args[0], args[1])
    except Exception as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        result = None
    return result
