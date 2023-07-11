#!/usr/bin/python3
"""
Module contains a function
returns the dictionary description with
simple data structure (list, dictionary,
string, integer and boolean) for JSON
serialization of an object:
"""


def class_to_json(obj):
    """
    returns the dictionary description with
    simple data structure (list, dictionary,
    string, integer and boolean) for JSON
    serialization of an object:
    Args:
        obj(object): object to check
    """
    return json.dumps(obj, default=lambda x: x.__dict__)
