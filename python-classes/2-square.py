#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass

    def __init__(self, size=0):
        self._Square__size = size
        if size < 0:
            try:
                print(size)
            except ValueError as e:
                print(f"size must be >= 0")
            
