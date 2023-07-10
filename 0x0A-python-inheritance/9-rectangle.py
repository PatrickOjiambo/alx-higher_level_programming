#!/usr/bin/python3
"""
Module containing an empty class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area():
        """
        Just return the area of the square
        """
        return self.__width * self.__height
    def __str__(self):
        """
        Print the name of this thing.
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.width, self.height)
