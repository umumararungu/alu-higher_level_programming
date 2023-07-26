#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <=0:
            raise ValueError("<name> must be greater than 0")
