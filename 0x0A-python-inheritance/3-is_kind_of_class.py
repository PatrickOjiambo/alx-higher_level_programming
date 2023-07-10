#!/usr/bin/python3
"""
Module contains an isinstance function
"""


def is_kind_of_class(obj, a_class):
    """
    Write a function that returns True
    if the object is an instance of, or if 
    the object is an instance of a class that
    inherited from,
    Args:
        obj: an object that is inherited from
        a_class: A class that to verify
    Returns:
            True or false
    """
    return isinstance(obj, a_class)
