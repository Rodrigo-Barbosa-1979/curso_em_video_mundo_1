'''
Challenge: Create a program that reads an Integer and displays its successor 
and predecessor on the screen.
Author: Rodrigo Barbosa
Date: January 17, 2024
'''
from utils import header, line

print(header('Antecessor e Sucessor', '='))

try:
    value = int(
        input('Digite por gentileza um valor numérico inteiro: ').strip())

    print(f'''
            O antecessor do valor {value:.>3} é: {value - 1}
            O sucessor do valor {value:.>5} é: {value + 1}

{line('=')}
        ''')

except:
    print(f'{format("lightred")}O valor informado não preenche o requisito solicitado!{format("reset")}')
