'''
Challenge: Create a program that reads two numbers and displays the sum 
between them.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils import header

print(header('Somando dois números', '*'))

try:

    first_number = int(input('Digite por gentileza o primeiro numero: ').strip())
    second_number = int(input('Digite por gentileza o segundo numero: ').strip())

    print(
        f'A soma entre os números {first_number} e {second_number} é igual a 
        {first_number + second_number}')

except:    
    print(f'{format("lightred")}O valor informado não preenche o requisito solicitado!{format("reset")}')
