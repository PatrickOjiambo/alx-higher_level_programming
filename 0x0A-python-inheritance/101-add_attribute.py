#!/usr/bin/python3
"""
Just a base class for something.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    This function sets the attribute name 
    and all that not so pleasing stuff
    """
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
