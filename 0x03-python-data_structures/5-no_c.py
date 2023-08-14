#!/usr/bin/python3
def no_c(my_string):
    letters = "cC"
    new_string = "".join(
            letter for letter in my_string if letter not in letters)
    return new_string
