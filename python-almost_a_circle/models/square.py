#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, size, x=0, y=0, id=None):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,self.x,self.y,self.width
        )

    def __str__(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
    


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()