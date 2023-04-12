# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

ficha = {}
Partidas = list()
time = list()

while True:
    ficha.clear()
    ficha['Nome'] = str(input('Nome do Jogador:  ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {ficha["Nome"]} jogou?  '))
    Partidas.clear()
    for c in range(0, tot):
        Partidas.append(int(input(f'    Quantos gols na partida {c+1}?  ')))
    ficha['Gols'] = Partidas[:] #a chave Gols recebe uma cópia da lista 'partidas'
    ficha['Total de Gols'] = sum(Partidas)
    time.append(ficha.copy())
    while True:
        esc = str(input('Quer continuar? [S/N]  ')).upper()[0]
        if esc in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if esc == 'N':
        break
print('-'*40)

print('cod ', end='')
for i in ficha.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
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
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]  '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-'*40)
print('     <<  VOLTE SEMPRE  >> ')
