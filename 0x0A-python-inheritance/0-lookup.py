#!/usr/bin/python3 
"""Module  0-lookup.
Returns a list of available attributes and methods of an object."""

def lookup(obj):
    """Returns that list of attributes and objects

    Args:
    - obj: object to look into
    """
    return dir(obj)

