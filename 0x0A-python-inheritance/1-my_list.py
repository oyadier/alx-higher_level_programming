#!/usr/bin/python3
"""Class that inherite List class"""


class MyList(list):
    """Print Sorted list"""

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
