# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número de 0 a 9999:  '))
num = str(n)
lista = list(num)
print(f'O número digitado foi: {n}\n'
        f'Unidade: {lista[3]}\n'
        f'Dezena: {lista[2]}\n'
        f'Centena: {lista[1]}\n'
        f'Milhar: {lista[0]}')

