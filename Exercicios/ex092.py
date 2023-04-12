# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em 
# um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

ficha = {}
ficha['Nome'] = str(input('Nome:  ')).capitalize().strip()
ano = int(input('Ano de nascimento:  '))
ficha['Idade'] = datetime.now().year - ano
ficha['CTPS'] = int(input('Carteira de Trabalho (0 não tem):  '))
if ficha['CTPS'] != 0:
    ficha['Ano de Contratação'] = int(input('Ano de Contratação:  '))
    ficha['Salário'] = float(input('Salário:  R$'))
    ficha['Aposentadoria'] = ficha['Idade'] + ((ficha['Ano de Contratação'] + 35) - datetime.now().year)
print('-'*40)
for k, v in ficha.items():
    print(f'{k}: {v}')
