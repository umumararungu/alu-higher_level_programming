#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


def text_indentation(text):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    suffix = [".", "?", ":"]

    result = text.endswith(".")

    if result == True:
        print(text, "\n", "\n")

    else:
        print("")
