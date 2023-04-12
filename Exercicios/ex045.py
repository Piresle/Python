# Crie um programa que faça o computador jogar Jokenpô com você.

'''
1 -> pedra
2 -> papel
3 -> tesoura
'''

from random import randint
from time import sleep
print('-*' * 5, 'JOKENPÔ', '-*' * 5)
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
jog = int(input('Suas opções: \n'
        '[ 1 ] PEDRA\n'
        '[ 2 ] PAPEL\n'
        '[ 3 ] TESOURA\n'
        'Qual é a sua jogada?  '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print(f'Você Jogou {itens[jog]}\n'
        f'Computador jogou {itens[pc]}')
if pc == 0:
        if jog == 0:
                print('EMPATE')   
        elif jog == 1:
                print('JOGADOR VENCE')
        elif jog == 2:
                print('COMPUTADOR VENCE')
elif pc == 1:
        if jog == 0:
                print('COMPUTADOR VENCE')
        elif jog == 1:
                print('EMPATE')
        elif jog == 2:
                print('JOGADOR VENCE')
elif pc == 2:
        if jog == 0:
                print('JOGADOR VENCE')
        elif jog == 1:
                print('COMPUTADOR VENCE')
        elif jog ==2:
                print('EMPATE')

