'''
Challenge: Create a function that prints a custom header.
Author: Rodrigo Barbosa
Date: January 16, 2024
'''
from utils.lines import line


def header(text, symbol):
    """
        ->Receives a String to be displayed as text and a character to be used 
        in separation lines.
        :param text: String referring to the text to be displayed.
        :param symbol: Character to be used to create separation lines.
        :return: String referring to the header.
    """
    symbol = symbol.strip()

    return f'{line(symbol)}\n{text.strip():^78}\n{line(symbol)}'
