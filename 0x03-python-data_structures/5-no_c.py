#!/usr/bin/python3

def no_c(my_string):
    updt_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            updt_str += i
    return (updt_str)
