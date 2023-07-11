#!/usr/bin/python3
"""
Module contains a function  returns an object
(Python data structure) represented by a JSON
string:
"""


import json


def from_json_string(my_str):
    """
     returns an object (Python data structure)
      represented by a JSON string:
    Args:
        my_str(str): String to be converted
    """
    return json.loads(my_str)
