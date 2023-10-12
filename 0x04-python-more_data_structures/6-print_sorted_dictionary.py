#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k , v in sorted(a_dictionary.items()):
        print(f"{k}: {v}")


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
