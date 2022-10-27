# DO NOT MODIFY THIS FILE

"""
Helper functions for the project

This file contains helper functions for the project. You should not modify
anything in this file. You can use the functions in this file to implement
the functions in readability.py.
"""


def get_string(prompt):
    """
    Read text from standard input and return it as a string
    """
    if type(prompt) != str:
        return TypeError("prompt must be a string")

    try:
        return input(prompt)
    except EOFError:
        return None