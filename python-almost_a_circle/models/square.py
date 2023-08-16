#!/usr/bin/python3
""" Defines a Square class that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a Square, a special case of Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()
