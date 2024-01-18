'''
Challenge: 
Author: Rodrigo Barbosa
Date: January 18, 2024
'''

"""
->
:param:
:return:
"""

from utils.messages import message
from utils.lines import line
from utils.formats import format
name = 'Gisele Nunes'
option = 'welcome '

print(f'{format("RED")} {message(name, option)} {format("reset")}')

print(line('='))

print(message('    Gisele Nunes     ', '   welcome   '))

print(line('='))

print(message(name, option))
