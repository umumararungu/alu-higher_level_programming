#!/usr/bin/python3
def no_c(my_string):
    replaced = ''
    for i in my_string:
        if i.lower() != 'c':
            replaced += i
    return replaced
