#!/usr/bin/python3
"""
Module contains a function
creates an Object from a “JSON file”:
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    Args:
        filename(str):name of the file to be written
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        final_string = json.loads(content)
        return final_string
