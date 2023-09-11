#!/usr/bin/python3
"""
Module 1-my_list

class MyList that inherits from list
"""


class MyList(list):
    """
    inherits from list

    Functions:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))
