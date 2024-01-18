'''
Challenge: Create a function for text color, background color and bold in the
terminal.
Author: Rodrigo Barbosa
Date: January 16, 2024
'''


def format(opcao):
    """
        ->Receives a string referring to color/bold/background color and 
        returns the corresponding code.
        :param option: String referring to the desired customization 
        (color/bold/background color).
        :return: String referring to the requested formatting code.
    """

    response = '\033[0;0m'

    formats = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'orange': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'lightgrey': '\033[37m',
        'darkgrey': '\033[90m',
        'lightred': '\033[91m',
        'lightgreen': '\033[92m',
        'yellow': '\033[93m',
        'lightblue': '\033[94m',
        'pink': '\033[95m',
        'lightcyan': '\033[96m',

        'reset': '\033[0;0m',
        'bold': '\033[;1m',
        'reverse': '\033[;7m',
    }

    choice = formats.get(opcao.strip().lower())

    if choice:
        response = choice

    return response
