#!/usr/bin/pythin3
# this 1-element_at.py is the second


def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list):
        return None
    if 0 < idx < len(my_list):
        return my_list[idx]
