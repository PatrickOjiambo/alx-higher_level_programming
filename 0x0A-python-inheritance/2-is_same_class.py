#!/usr/bin/python3
"""
Module contains an isinstance function
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
     an instance of the specified class ; otherwise False.
     Args:
        obj: An object of a class
        a_class: A class to be verified
     Returns:
            True or False
    """
    return type(obj) == a_class
