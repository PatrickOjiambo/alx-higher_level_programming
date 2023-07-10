#!/usr/bin/python3
"""
Module containing an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Class contains some geometry class
    """
    def area(self):
        """
        Calculates the area. Maybe it doesn't
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates the value
        """
        if isinstance(value, int):
            raise TypeError("{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")
