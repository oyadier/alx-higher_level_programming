#!/bin/python3
def multiple_returns(sentence):
    """ multiple_returns - a function that returns a 
        tuple with the length of a string and its first character.
        @sentence: the string to be parse
        Return: a tuple with string lengh and first string char
    """

    lengh= 0
    for i in sentence:
        lengh += 1
    if lengh == 0:
        tup = lengh, None
    else:
        tup = lengh,  sentence[0]
    return tup
