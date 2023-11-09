#!/usr/bin/python3
"""Student module with attribute"""



class Student:

    def __init__(self, first_name, last_name, age):
        """Student initializer

            Args:
                first_name (str): the first name of student.
                last_name (st): the last name of student.
                age (int): the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """Convert student obj to json rep"""
        return self.__dict__
