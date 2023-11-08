#!/usr/bin/python3
import json

"""Python objec to String"""


def to_json_string(my_obj):
    """Python Object To Json String

        Args:
            my_obj(object): python object

        Return:
            json : String
    """
    return json.dumps(my_obj)
