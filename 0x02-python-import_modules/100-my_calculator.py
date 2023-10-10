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
            case "-":
                print("{} - {} = {}".format(first, second, sub(first, second)))
            case "*":
                print("{} * {} = {}".format(first, second, mul(first, second)))
            case "/":
                print("{} / {} = {}".format(first, second, div(first, second)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
