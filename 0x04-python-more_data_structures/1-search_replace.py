#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = my_list[:]
    for i in range(len(cp)):
        if cp[i] == search:
            cp[i] = replace
    return cp
