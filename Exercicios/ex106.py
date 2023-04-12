# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário igitar a palavra 'FIM', o programa se encerrará;].
# OBG: use cores.

from time import sleep

c = ('\033[n', # sem cor
    '\033[0;30;41m', # vermelho 
    '\033[0;30;42m', # verde
    '\033[0;30;43m', # amarelo
    '\033[0;30;44m', # azul
    '\033[0;30;45m', # roxo 
    '\033[7;30m') # branco 

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    help(com)
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


cmd = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    cmd = str(input('Função ou biblioteca > '))
    if cmd.upper() == 'FIM':
        break
    else:
        ajuda(cmd)
titulo('ATÉ LOGO!', 1)
