#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area():
        return sel.width * self.height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
