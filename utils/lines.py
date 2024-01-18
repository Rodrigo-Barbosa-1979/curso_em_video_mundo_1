"""
Challenge: Create a function that prints a custom line.
Author: Rodrigo Barbosa
Date: January 17, 2024
"""


def line(symbol):
    """
        ->Receives a character and creates a line with 78 characters.
        :param symbol: Character to be used to create the line.
        :return: String com 78 caracteres.
    """
    return (symbol.strip() * 78)
