'''
Challenge: Create a program that reads a person's name and displays a welcome 
message.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils import message, header, line, format

print(header('Mensagem de boas vindas', '='))

name = input('Digite por gentileza o seu nome completo: ').strip()

print(f'''{line('=')}\n{" ":>25}{message(name, "welcome")}\n{line('=')}''')
