# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta. 

from random import randint
from time import sleep 

lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie?  '))
print('-' * 15, end=' ')
print(f'SORTEANDO {quant} JOGOS ', end='')
print('-' * 15)
tot = 1 
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print('-' * 19, end=' ')
print('BOA SORTE ', end='')
print('-' * 19)


'''
lista = []
cont = 0
while True:
    sort = randint(1, 60)
    if sort not in lista:
        lista.append(sort)
        cont += 1
    if cont >= 6:
        break
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-' * 15, end=' ')
print(f'SORTEANDO {jogos} JOGOS ', end='')
print('-' * 15)
lista.sort()
for j in range(0, jogos):
    print(f'Jogo {j+1}: {lista}')
    sleep(0.75)

print('-' * 19, end=' ')
print('BOA SORTE ', end='')
print('-' * 19)
'''