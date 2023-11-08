#!/bin/usr/python3
"""Json Dic to Python String"""
import json


def from_json_string(my_str):

    """Decode Json string to python str

        Args:
        my_str(dic): json dic

        Return:
    (string): pyton string
    """
    return json.loads(my_str)
