#!/usr/bin/python3
"""More on this squares to come later"""


class Square:
    def __init__(self, size=0):

        """
        This is a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
