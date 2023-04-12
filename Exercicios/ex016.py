# Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira. 

import math 
n = float(input('Digite um número real:  '))
print(f'A porção inteira do número {n} é {math.trunc(n)}')

# OU
# n = float(input('Digite um número real:  '))
# print(f'A porção inteira do número {n} é {int(n)}')

