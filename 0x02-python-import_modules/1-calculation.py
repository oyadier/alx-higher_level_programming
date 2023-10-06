#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def compute(met, sign):
    a = 10
    b = 5
    cal = met(a, b)
    print("{}".format(a), sign,  "{} = {}".format(b, cal))


if __name__ == "__main__":
    compute(add, "+")
    compute(sub, "-")
    compute(mul, "*")
    compute(div, "/")
