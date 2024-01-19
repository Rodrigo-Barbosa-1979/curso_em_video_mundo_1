'''
Challenge: Create a program that reads any whole number and displays its 
multiplication table on the screen.
Author: Rodrigo Barbosa
Date: January 18, 2024
'''
from utils import header, line, format

print(header('Tabuada', '='))

try:

    number = int(
        input('Digite por gentileza o número que deseja gerar a tabuada: '))

    print(line('='))

    for i in range(0, 11, 1):
        print(f'{format("blue")}{number:>32}{format("reset")}  x {format("blue")}{i:>2}{format("reset")} = {format("red")}{number * i:>3}{format("reset")}')

except:
    print(f'{format("lightred")}O valor informado não preenche o requisito solicitado!{format("reset")}')

print(line('='))
