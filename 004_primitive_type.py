'''
Challenge: Create a program that reads something from the keyboard and 
displays its primitive type and some information about it on the screen.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils import header, line, check_characteristics

print(header('Dissecando uma Variável', '='))

value = input('Digite por gentileza algo a ser analisado: ').strip()

print(check_characteristics(value))

print(line('='))
