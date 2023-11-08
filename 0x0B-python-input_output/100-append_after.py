#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    newT = ""
    with open(filename) as r:
        for line in r:
            newT += line
            if search_string in line:
                newT += new_string
    with open(filename, "w") as w:
        w.write(newT)
