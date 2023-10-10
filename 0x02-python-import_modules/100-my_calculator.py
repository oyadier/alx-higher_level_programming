#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    if len(sys.argv) == 4:
        first = int(sys.argv[1])
        second = int(sys.argv[3])
        match (sys.argv[2]):
            case "+":
                print("{} + {} = {}".format(first, second, add(first, second)))
                sys.exit("0")
            case "-":
                print("{} - {} = {}".format(first, second, sub(first, second)))
                sys.exit("0")
            case "*":
                print("{} * {} = {}".format(first, second, mul(first, second)))
                sys.exit("0")
            case "/":
                print("{} / {} = {}".format(first, second, div(first, second)))
                sys.exit("0")
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit("1")
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit("1")
