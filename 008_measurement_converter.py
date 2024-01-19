'''
Challenge: Create a program that reads a value in meters and displays it 
converted into centimeters and millimeters.
Author: Rodrigo Barbosa
Date: January 18, 2024
'''
from utils import header, line, format

print(header('Conversor de Medidas', '='))

try:

    value = float(
        input('Digite por gentileza quantos metros deseja converter: '))

    kilometer = value / 1000
    hectometer = value / 100
    decameter = value / 10
    decimeter = value * 10
    centimeters = value * 100
    millimeters = value * 1000

    print(f'''
    {format('red')}{value:.0f}{format("reset")} metros convertidos em quilômetros representa {format("green")}{kilometer:>5}{format("reset")} {"quilômetros":>12}.
    {format('red')}{value:.0f}{format("reset")} metros convertidos em hectômetros representa {format("green")}{hectometer:>5}{format("reset")} {"hectômetros":>12}.
    {format('red')}{value:.0f}{format("reset")} metros convertidos em decâmetros representa {format("green")}{decameter:>6}{format("reset")} {"decâmetros":>12}
    {format('red')}{value:.0f}{format("reset")} metros convertidos em decímetros representa {format("green")}{decimeter:>6.0f}{format("reset")} {"decímetros":>12}.
    {format('red')}{value:.0f}{format("reset")} metros convertidos em centímetros representa {format("green")}{centimeters:>5.0f}{format("reset")} {"centimetros":>12}
    {format('red')}{value:.0f}{format("reset")} metros convertidos em milímetros representa {format("green")}{millimeters:>6.0f}{format("reset")} {"milímetros":>12}.
    ''')

except:
    print(f'{format("lightred")}O valor informado não preenche o requisito solicitado!{format("reset")}')

print(line('='))
