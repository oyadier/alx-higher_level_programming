#!/usr/bin/python3
"""Handle error status code"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            pass
    except Exception as err
        print('Error code: ', err.code)
