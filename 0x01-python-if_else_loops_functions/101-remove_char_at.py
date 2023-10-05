#!/usr/bin/python3
def remove_char_at(str, n):
    str_cp = ""
    c = 0
    for i in str:
        if c != n:
            str_cp += str[c]
        c += 1
    return str_cp
