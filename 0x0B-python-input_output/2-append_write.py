#!/usr/bin/python3
"""
Module 2-append_write
Contains a function that appends a string
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
