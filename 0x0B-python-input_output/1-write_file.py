#!/usr/bin/python3
"""
Module 1-write_file
Defines a functions tha writes a string to a file
"""


def write_file(filename="", text=""):
    """A function that writes a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
