# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram 
# a maioridade e quantas já são maiores.

from datetime import date 
data = date.today().year
totalmaior = 0
totalmenor = 0
for x in range(1, 8):
    ano = int(input(f'Digite o {x}º ano de nascimento:  '))
    idade = data - ano
    if idade < 21:
        totalmenor += 1
    elif idade >= 21:
        totalmaior += 1 
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade e\n'
        f'{totalmenor} pessoas menores de idade.')

