#!/usr/bin/python3
"""
Module 0-read_file
Deifnes a functions that reads a file
"""


def read_file(filename=""):
    """ function that reads a file and encodes it"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
