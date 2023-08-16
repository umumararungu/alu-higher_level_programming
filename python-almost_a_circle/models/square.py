#!/usr/bin/python3
""" Defines a Rectangle class """

class Rectangle:
    """ Represents a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the rectangle with '#' characters """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'width': self.width,
            'height': self.height
        }

if __name__ == "__main__":
    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)
