#!/usr/bin/python3
"""Read text file"""


def read_file(filename=""):
    """Read file and print it to stdo

        Args:
            filename (text): text file

    """
    with open(filename, encoding="utf=8") as f_obj:
        for i in f_obj:
            print(i, end="")
