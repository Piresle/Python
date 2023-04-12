# Crie um porgama onde quatro jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
# resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
# o maior número.

import enum
from random import randint
from time import sleep
from operator import itemgetter
'''
randint(1, 6)
print(f'{"VALORES SORTEADOS":^25}')
print('-'*25)
for c in range(0, 4):
    print(f'Jogador {c+1} tirou {randint(1, 6)} no dado.')
print('-'*25)
print()
print(f'{"RANKING DOS JOGADORES":^25}')
print('-'*25)
'''

# __________________________________________________ #

jogo = {'jogador 1': randint(1, 6), 
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6), 
        'jogador 4': randint(1, 6)}
print(f'{"VALORES SORTEADOS":^25}')
print('-'*25)
ranking = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.75)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING DOS JOGADORES":^25}')
print('-'*25)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.75)
