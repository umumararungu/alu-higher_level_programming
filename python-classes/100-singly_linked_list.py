#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Node:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass


    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data

    @property
    def next_node(self):
        return self.next_node
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, node) or value != None:
            raise TypeError("next_node must be a node object")
        
class SinglyLinkedList:
    def __init__(self):
        print(" " self.__data + self.__next_node "\n" )

