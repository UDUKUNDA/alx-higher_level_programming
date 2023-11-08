#!/usr/bin/python3
"""Defines a text reading function."""


def read_file(filename=""):
    """Print the contents of a text file to stdout."""
    with open(filename, encoding="utf-8") as y:
        print(y.read(), end="")