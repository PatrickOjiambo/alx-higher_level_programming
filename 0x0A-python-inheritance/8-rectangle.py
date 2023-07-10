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
        Args:
            name: just the name
            value: value of the name
        """
        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Class rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height =height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
