#!/usr/bin/python3

def is_same_class(obj, a_class):
    if isinstance(obj.__repr__(), a_class):
        return True
    else:
        return False
