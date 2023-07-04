#!/usr/bin/python3
"""
Prints something with locked class
"""


class LockedClass:
    """
    This class contains some stuff
    that does somethin
    """

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("Cannot create new instance attributes")
        self.__dict__[name] = value
