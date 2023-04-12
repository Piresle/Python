# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
# que estão na tupla.

from random import randint
pc = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os números gerados foram: {pc}')
print(f'O menor número é {min(pc)} e o maior é {max(pc)}.')

