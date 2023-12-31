#!/usr/bin/python3
# class 'Square' that inherits from 'Rectangle'
# (9-rectangle.py)
"""
    define a class 'Square' inheriting from 'BaseGeometry'
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        representation of 'Square
    """

    def __init__(self, size):
        """
            instantiate private instance field size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
