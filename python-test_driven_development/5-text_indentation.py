#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


def text_indentation(text):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text.split()
    c = 0
    s = '[?.:]'
    for i in range(len(text)):
        if text[i] in s:
            print("\n", "\n")
    else:
        print(text)
