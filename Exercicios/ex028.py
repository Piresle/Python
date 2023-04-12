# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint
from time import sleep

print('***'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('***'*20)
x = randint(0,5) 
sleep(3)
n = int(input('Em qual número eu pensei?  '))
print('***'*20)
if n == x:
    print('Você acertou!')
else:
    print(f'Você errou! Eu pensei no número {x} e não no número {n}.')

