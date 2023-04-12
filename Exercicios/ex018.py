# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


import math
ang = int(input('Digite o ângulo:  '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O seno, cosseno e a tangente do ângulo {ang} são:\n'
        f'sen {sen:.2f}\n'
        f'cos {cos:.2f}\n'
        f'tan {tan:.2f}')

# OU
# from math import radians, sin, cos, tan 
# ang = int(input('Digite um ângulo:  '))
# sen = sin(radians(ang))
# ... 