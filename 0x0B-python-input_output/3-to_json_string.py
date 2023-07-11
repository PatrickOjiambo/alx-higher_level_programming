#!/usr/bin/python3
"""
Module contains a function that returns the
json representation of a string
"""


import json


def to_json_string(my_obj):
    """
    returns the json representation of a string
    Args:
        my_obj(object):Object to be transformed
    """
    return json.dumps(my_obj)
