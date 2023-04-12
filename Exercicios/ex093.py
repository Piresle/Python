# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

ficha = {}
Partidas = list()
ficha['Nome'] = str(input('Nome do Jogador:  ')).capitalize().strip()
tot = int(input(f'Quantas partidas {ficha["Nome"]} jogou?  '))
for c in range(0, tot):
    Partidas.append(int(input(f'    Quantos gols na partida {c+1}?  ')))
ficha['Gols'] = Partidas[:] #a chave Gols recebe uma cópia da lista 'partidas'
ficha['Total de Gols'] = sum(Partidas)

print('-'*40)
print(ficha)

print('-'*40)
for k, v in ficha.items():
    print(f'{k}: {v}')

print('-'*40)
print(f'O jogador {ficha["Nome"]} jogou {len(ficha["Gols"])} partidas') # ou 'tot'
for i, v in enumerate(ficha['Gols']):
    print(f'  => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {ficha["Total de Gols"]} gols')
