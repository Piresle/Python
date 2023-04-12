# Esceva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    # O primeiro valor é maior;
    # o segundo valor é maior;
    # não existe valor mais, os dois são iguais. 


n1 = int(input('Digite um número:  '))
n2 = int(input('Digite outro número:  '))
if n1 > n2:
    print('O PRIMEIRO número é maior.')
elif n2 > n1:
    print('O SEGUNDO número é maior.')
elif n1 == n2:
    print('Não exite valor maior, os dois são IGUAIS.')


