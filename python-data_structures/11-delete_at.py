#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
   if idx < 0 or idx > len(my_list):
      return my_list
   else:
       space = ""
       my_list[idx] = space
       return my_list
