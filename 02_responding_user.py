'''
Challenge: Create a program that reads a person's name and displays a welcome 
message.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils.messages import message

name = input('Digite por gentileza o seu nome completo: ').strip()

print(f'{message(name, "welcome")}')
