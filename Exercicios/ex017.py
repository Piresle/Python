# Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo, calcule 
# e mostre o comprimento de hipotenusa.

co = float(input('Digite o comprimento do cateto oposto:  '))
ca = float(input('Digite o comprimento do cateto adjacente:  '))
hip = (co**2) + (ca**2)
print(f'O comprimento da hipotenusa é {hip**(1/2):.1f}')


# (hip**2) = (cat**2) + (cat**2)

# OU
# import math
# co = float(input('Digite o comprimento do cateto oposto:  '))
# ca = float(input('Digite o comprimento do cateto adjacente:  '))
# hip = math.htpot(co, ca)
# print(f'A hipotenusa vai medir {hip:.1f})

