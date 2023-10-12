#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp = my_list[:]
    for i in range(len(cp)):
        if cp[i] == search:
            cp[i] = replace
    return cp


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
