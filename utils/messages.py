'''
Challenge: Create a function that returns a custom message.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''


def message(name, option):
    """
    -> It receives a name string and an option string and generates a string with the formatted message.
    :param name: Receives a string with the name to be formatted.
    :param option: Recebe uma string com a opção de formatação.
    :return: String com o nome formatado.
    """

    options = {
        'birthday': 'Happy birthday',
        'welcome': 'Welcome',
        'morning': 'Good morning',
        'afternoon': 'Good afternoon',
        'goodnight': 'Goodnight',
    }

    response = ' '
    choice = options.get(option.strip().lower())

    if choice:
        response = f'{choice} {name.strip()}!'

    return response
