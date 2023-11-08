#!/usr/bin/python3
"""Object save to Json file"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to json representation

        Args:
            my_obj (object): python object ie list.
            filename (.json): the json file exention
    """
    with open(filename, "w", encoding="utf-8") as to_json:
        json.dump(my_obj, to_json)
