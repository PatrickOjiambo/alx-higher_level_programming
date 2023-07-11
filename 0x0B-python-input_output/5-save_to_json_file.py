#!/usr/bin/python3
"""
Module contains a function  writes an
Object to a text file, using a JSON
representation:
string:
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation:
    Args:
        my_obj(object): Object to be converted to json
        filename(str):name of the file to be written
    """
    with open(filename, 'w') as file:
        content = file.write(json.dumps(my_obj))
