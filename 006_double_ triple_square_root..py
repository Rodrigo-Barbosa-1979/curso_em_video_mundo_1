'''
Challenge: Create an algorithm that reads a number and shows its double, 
triple and square root.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from math import sqrt
from utils import header, line

print(header('Dobro, Triplo, Raiz Quadrada', '='))

try:

    value = int(input('Digite por gentileza um número inteiro: ').strip())

    print(f"""
    O doblo do valor {value:.>12} é: {value * 2:>4}
    O triplo do valor {value:.>11} é: {value * 3:>4}
    A raiz quadrada do valor {value:.>4} é: {sqrt(value):>4}

{line('=')}
""")


except:
    print(f'{format("lightred")}O valor informado não preenche o requisito solicitado!{format("reset")}')
