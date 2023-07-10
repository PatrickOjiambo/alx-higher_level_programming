#!/usr/bin/python3
"""
Module containing an empty class BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Contains the Square class
    """
    def __init__(self, size):
        """
        Contains the square construcor
        """
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size ** 2
