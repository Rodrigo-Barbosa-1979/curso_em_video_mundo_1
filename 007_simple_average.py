'''
Challenge: Create a program that reads a student's two grades, calculates and
displays their average.
Author: Rodrigo Barbosa
Date: January 18, 2024
'''
from utils import header, line

print(header('Operadores Aritméticos', '='))

name = input('Digite por gentileza o nome do aluno: ')

try:

    first_note = float(input('Digite por gentileza a primeira nota: '))
    second_note = float(input('Digite por gentileza a segunda nota: '))

    average = (first_note + second_note) / 2

    print(
        f'Com as notas {first_note} e {second_note} o aluno {name} atingiu '
        f'a média: {average}'
    )

except:    
    print(f'{format("lightred")}O valor informado não preenche o requisito solicitado!{format("reset")}')

print(line('='))
