#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Rectangle:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_intances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        space = ""
        if self.__width == 0 or self.__height == 0:
            return space
        for col in range(self.__height):
            for row in range(self.__width):
                space += str(self.print_symbol)
            space += '\n'
        return space[:-1]

    def __repr__(self):
        new_rectangle = eval(repr(Rectangle))
        return new_rectangle

    def __del__(self):
        print(Rectangle.number_of_instances)
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if rect_1 is not isinstance(Rectangle):
            raise TypeError("react_1 must be an instance of Rectangle")
        elif rect_2 is not isinstance(Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1 == rect_2 or rect_1 > rect_2:
                return rect_1
            else:
                return rect_2
