#!/usr/bin/python3
"""
Module contains an isinstance function
"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True
    if the object is an instance of, or if
    the object is an instance of a class that
    inherited from or not(directly or indirectly),
    Args:
        obj: an object that is inherited from
        a_class: A class that to verify
    Returns:
            True or false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
