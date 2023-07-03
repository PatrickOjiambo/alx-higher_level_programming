#!/usr/bin/python3
"""
This file contains the rectangle file.
This file contains the rectangle file.
This file contains the rectangle file.
"""


class Rectangle:
    """
    This is the rectangle class with getters, setters
    and all that stuff
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
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rect.
        """
        return (self.__height)

    @property()
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rect.
        """
        return (self.__width)

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        """
        Setter method for the width attribute.

        Args:
            value (tuple): The position of the rect.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
=======
>>>>>>> 7248a612c45060fbc46e4cd92cbf11087e9aa41f
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """
        Setter method for the width attribute.

        Args:
            value (tuple): The position of the rect.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
=======
>>>>>>> 7248a612c45060fbc46e4cd92cbf11087e9aa41f
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
