#!/usr/bin/python3
"""
This file contains the rectangle file.
"""


class Rectangle:
    """
    This is the rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        This is the init function.
        Args: width, height
        """
        self.__width = width
        self.__height = height

    @property()
    def height(self):
        """get the height of the rectangle."""
        return (self.__height)

    @property()
    def width(self):
        """get the width of the rectangle."""
        return (self.__width)

    @height.setter
    def height(self, value):
        """Changes the value  of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """Changes the value  of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
