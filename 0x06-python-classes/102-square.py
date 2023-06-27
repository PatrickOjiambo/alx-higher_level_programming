#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        size (int or float): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int or float): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of this square is equal to the area of another square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if the area of this square is not equal to the area of another square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if the area of this square is greater than the area of another square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if this square's area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of this square is greater than or equal to the area of another square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if this square's area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Checks if the area of this square is less than the area of another square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if this square's area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of this square is less than or equal to the area of another square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if this square's area is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
