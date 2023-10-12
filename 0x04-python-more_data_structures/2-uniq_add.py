#!/usr/bin/python3
def uniq_add(my_list):
    sum = 0
    new_set = set(my_list)
    for elem in new_set:
        sum += elem
    return sum
