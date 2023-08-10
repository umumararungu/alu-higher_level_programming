#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


from models.base import Base

class Rectangle(Base):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__width

    @width.setter
    def width(self, width):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__width = width

    @property
    def height(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__height = height

    @property
    def x(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__x
    @x.setter
    def x(self, x):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__x = x

    @property
    def y(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__y

    @y.setter
    def set_y(self, y):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__y = y

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
