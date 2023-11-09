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

    def to_json(self, attrs=None):
        """Convert student obj to json rep

            Args:
                attrs (attributes): all posible data type
            Return:
                all posible data type
        """
        json_dict = {}
        diction = self.__dict__
        if not attrs:
            return diction

        for key in attrs:
            if key in diction:
                value = diction[key]
                if isinstance(value, (list, str, dict, int, bool)):
                    json_dict[key] = value

        return json_dict
