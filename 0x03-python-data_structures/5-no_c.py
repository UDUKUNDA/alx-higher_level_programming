#!/usr/bin/python3

def no_c(my_string):
    empstr = ""
    for j in my_string:
        if j != 'c' and j != 'C':
            new_string += j
            return new_string
