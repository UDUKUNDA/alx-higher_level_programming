#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    n = 0

    for i in unique:
        n += i

    return (n)
