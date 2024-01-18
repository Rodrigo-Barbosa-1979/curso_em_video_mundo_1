'''
Challenge: It takes a string and returns its primitive type and some 
information about it. 
Author: Rodrigo Barbosa
Date: January 17, 2024
'''


def check_characteristics(value):
    """
        -> It takes a string and returns its primitive type and some 
        information about it.
        :param value: string referring to the value to be analyzed.
        :return: string with the analysis result.
    """

    response = f"""
        O tipo primitivo do valor "{value}" é: {type(value)} 
        O valor "{value}" contém apenas espaços?: {value.isspace()}
        O valor "{value}" é um número?: {value.isdecimal()} 
        O valor "{value}" é alfabetico?: {value.isalpha()}
        O valor "{value}" é alfanumérico?: {value.isalnum()}
        O valor "{value}" está em letras maiusculas?: {value.isupper()}
        O valor "{value}" está em letras minusculas?: {value.islower()}
        O valor "{value}" está capitalizado?: {value.istitle()}
        """

    return response
