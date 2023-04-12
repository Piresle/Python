# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = l * h 
tin = a / 2
print(f'Sua parede tem a dimensão {l}x{h}, '
        f'sua área é de {a}m², e a quantidade de tinta necessária é {tin}l')

