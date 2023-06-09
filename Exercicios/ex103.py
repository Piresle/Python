# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha 
# sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print('-'*40)
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jog = str(input('Nome do jogador:  ')).capitalize().strip()
gol = str(input('Quantos gols o jogador marcou?  '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    ficha(gols=gol)
else:
    ficha(jog, gol)
