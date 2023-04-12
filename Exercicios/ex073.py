# Crie um tupla preenchida com os 20 colocados da tabela do campeonato brasileiro de futebol, na ordem
# de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time Corinthians.

colocados = ('Palmeiras', 'Santos', 'Vasco', 'Grêmio', #limite de 80 caracteres por código/linha
'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro', 
'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 
'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 
'Portuguesa', 'Atlético Paranaense', 'Vitória')
print('-----'*10)
print(f'Lista de times: {colocados}')
print('-----'*10)
print(f'Os cinco primeiros colocados são: {colocados[0:5]}')
print('-----'*10)
print(f'Os últimos quatro colocados são: {colocados[-4:]}')
print('-----'*10)
print(f'Times em ordem afabética: {sorted(colocados)}')
print('-----'*10)
while True:
    esc = str(input('Informe o time para saber a sua posição: ')).strip().capitalize()
    print(f'O time {esc} está na posição {colocados.index(esc)+1}') # Aspas duplas
    cont = str(input('Quer continuar? [S/N]  ')).upper()
    if cont == 'N':
        break
