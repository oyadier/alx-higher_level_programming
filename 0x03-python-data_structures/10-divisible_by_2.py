#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for x in my_list:
        result.append(not x & 1)
    return result
