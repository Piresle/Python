# Faça um programa que leia um número qualquer e mostre o seu fatorial. 

import math 
num = int(input('Digite um número para calcular seu factorial:  '))
print(f'O factorial do número {num} é {math.factorial(num)}')

# OU

n = int(input('Digite um número para calcular o seu factorial: '))
c = n
f = 1
print(f'calculando {n}!')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

