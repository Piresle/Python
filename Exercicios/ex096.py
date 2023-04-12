# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre
# a área do terreno.

def area(lado, comp):
    a = lado * comp
    print(f'A área do terreno  {lado} x {comp}  é {a}m².')


lado = float(input('Largura:  '))
comp = float(input('Comprimento:  '))
area(lado, comp)
