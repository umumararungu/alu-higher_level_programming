#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

def add_integer(a, b=98):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if not isinstance(a, int):
        raise TypeError("a must be an integere")
    if not isinstance(a, float):
        raise TypeError("a must be an integere")
    if not isinstance(b, int):
        raise TypeError("a must be an integere")
    if not isinstance(b, float):
        raise TypeError("a must be an integere")
    return int(a)+int(b)
