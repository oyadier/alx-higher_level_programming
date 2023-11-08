#!/usr/bin/python3
"""Object save to Json file"""
import json


def load_from_json_file(filename):
    """Write object to json representation

        Args:
            filename (.json): the json file exention
    """
    with open(filename, encoding="utf-8") as to_json:
        sons = json.load(to_json)
    return sons
