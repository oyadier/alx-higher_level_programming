#!/usr/bin/python3
"""Class that inherite List class"""


class MyList(list):

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
