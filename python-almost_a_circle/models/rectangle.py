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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__width

    @width.setter
    def width(self, width):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__height

    @height.setter
    def height(self, height):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__x

    @x.setter
    def x(self, x):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__x = x
        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.__y

    @y.setter
    def y(self, y):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        self.__y = y
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return self.width * self.height

    def display(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return (self.id) (self.x / self.y) - (self.width / self.height))

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)
