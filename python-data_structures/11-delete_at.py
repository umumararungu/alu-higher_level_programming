#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        index = ((my_list[idx]) - 1)
        remove = my_list.remove(index)
        return my_list
