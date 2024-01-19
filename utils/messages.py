'''
Challenge: Create a function that returns a custom message.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils import format


def message(name, option):
    """
    -> It receives a name string and an option string and generates a string with the formatted message.
    :param name: Receives a string with the name to be formatted.
    :param option: Recebe uma string com a opção de formatação.
    :return: String com o nome formatado.
    """

    options = {
        'birthday': 'Feliz aniversário',
        'welcome': 'Bem vindo',
        'morning': 'Bom dia',
        'afternoon': 'Boa tarde',
        'goodnight': 'Boa noite',
    }

    response = ' '
    choice = options.get(option.strip().lower())

    if choice:
        response = f'{choice} {format("cyan")} {name.strip()}{format("reset")}!'

    return response
