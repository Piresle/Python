# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre: 
#   -> Quantas pessoas foram cadastradas;
#   -> A média de idade do grupo;
#   -> Uma lista com  todas as mulheres;
#   -> Uma lista com todas as pessoas com idade acima da média.

pessoa = {}
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:  ')).capitalize().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoa['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Idade:  '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        esc = str(input('Quer continuar? [S/N]  ')).upper()[0]
        if esc not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        else: 
            break
    if esc == 'N':
        break
print('-'*40)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('-'*40)
print(f'{"<< ENCERRADO >>":^40}')
