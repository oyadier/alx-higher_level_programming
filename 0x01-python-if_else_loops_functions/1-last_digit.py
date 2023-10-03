#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# First convert the number to string then get the las digit using
# the negative value slicing
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit}\
 and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit}\
 and is 0")
else:
    print(f"Last digit of {number} is {last_digit}\
 and is less than 6 and not 0")
