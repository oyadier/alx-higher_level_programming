#!/usr/bin/python3
import sys


def args(args):
    for i in range(1, args + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc < 1:
        print("{} {}.".format(argc, "arguments"))
    elif argc == 1:
        print("{} {}:".format(argc, "argument"))
        args(argc)
    else:
        print("{} {}:".format(argc, "arguments"))
        args(argc)
