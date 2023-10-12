#!/usr/bin/python3
def best_score(a_dictionary):
    key, big = 0, 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v == 0:
                key = v
            if v > big:
                big = v
                key = k
        return key
