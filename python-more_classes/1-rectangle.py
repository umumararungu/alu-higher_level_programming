#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Rectangle:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass


    def __init__(self, width=0, heiht=0):
        self.__width = width
        self.__height = height


    @property
    def width(self):
        self.__width = width
        return width

    @property.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")

    @property
    def height(self):
        self.__height = height
        return height

    @property.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
