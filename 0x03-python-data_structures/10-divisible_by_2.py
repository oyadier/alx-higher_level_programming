#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for x in my_list:
        result.append(not x & 1)
    return result

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

