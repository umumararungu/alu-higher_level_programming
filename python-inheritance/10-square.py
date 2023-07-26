#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

Square = __import__('10-square').Square

class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        return f"[Square] {self.__size}"
