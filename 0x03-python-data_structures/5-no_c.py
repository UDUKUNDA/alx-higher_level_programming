#!/usr/bin/python3

def no_c(my_string):
    y=[i for i in my_string if i != 'c' and i != 'C']
    return ("".join(y))
