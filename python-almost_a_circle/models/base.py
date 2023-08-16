#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import json


class Base:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    #getter method
    def get_width(self):
        return self.get__width
    #setter method
    def set_width(self, width):
        self.__width = width

    #getter method
    def get_height(self):
        return self.get__height
    #setter method
    def set_height(self, height):
        self.__height = height

    #getter method
    def get_x(self):
        return self.get__x
    #setter method
    def set_x(self, x):
        self.__x = x

    #getter method
    def get_y(self):
        return self.get__y
    #setter method
    def set_y(self, y):
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
