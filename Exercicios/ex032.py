# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


from datetime import date

n = int(input('Qual ano você quer analisar? Ou coloque 0 para analisar o ano atual:  '))
if n == 0:
    n = date.today().year
if (n % 4) == 0 and (n % 100) != 0:
    print(f'O ano {n} é bissexto!')
else: 
    print(f'O ano {n} não é bissexto!')

