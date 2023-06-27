#!/usr/bin/python3
"""
This module defines a Square class that represents a square shape.

Square Class:
    Represents a square defined by its size.

"""


class Square:
    """
    Represents a square shape.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializ with an optional size.

    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of the square
        """
        size = self.__size
        area = size * size
        return area

    @property()
    def size(self):
        """
        Returns the attribute value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
