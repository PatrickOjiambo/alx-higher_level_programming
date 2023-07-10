#!/usr/bin/python3
"""
Module to learn inheritance
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object:
    Args:
        An object
    Returns:
            A list of objects
    """
    return dir(obj)
