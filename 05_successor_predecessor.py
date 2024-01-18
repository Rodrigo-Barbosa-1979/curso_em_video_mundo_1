'''
Challenge: Create a program that reads an Integer and displays its successor 
and predecessor on the screen.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils.headers import header
from utils.lines import line

print(header('Sucessor e Antecessor', '='))

try:
    value = int(
        input('Digite por gentileza um valor numérico inteiro: ').strip())

    print(f'''
            O sucessor do valor {value:.>5} é: {value + 1}
            O antecessor do valor {value:.>3} é: {value - 1}

{line('=')}
        ''')

except:
    print('O valor informado não preenche o requisito de valor inteiro!')
