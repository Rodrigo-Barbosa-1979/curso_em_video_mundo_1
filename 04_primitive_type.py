'''
Challenge: Create a program that reads something from the keyboard and 
displays its primitive type and some information about it on the screen.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils.headers import header
from utils.lines import line
from utils.characteristics import check_characteristics

print(header('Primitive types and their information', '='))

value = input('Digite por gentileza algo a ser analisado: ').strip()

print(check_characteristics(value))

print(line('='))
