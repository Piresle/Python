# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é maior.

from time import sleep

def maior(* n):
    cont = maior = 0
    print('-'*40)
    print('\nAnalisando os valores passados... ')
    for valor in n:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor 
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor digitado foi {maior}')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(3, 5, 7, 15, 10, 2)
maior(5, 2, 9, 1)
maior(4, 8)
maior(6)
maior()
