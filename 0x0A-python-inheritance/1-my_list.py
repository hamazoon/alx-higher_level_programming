#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
