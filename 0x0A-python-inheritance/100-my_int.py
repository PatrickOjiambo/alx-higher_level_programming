#!/usr/bin/python3
"""
Just a base class for something.
"""


class MyInt(int):
    """
    Class rebel. Does the opposite
    """
    def __eq__(self, other):
        """
        Does the opposite
        Returns the opposite
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Does the opposite
        Returns the opposite
        """
        return super().__eq__(other)
