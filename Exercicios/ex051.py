# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.

a1 = int(input('a1: '))  # primeiro termo 
r = int(input('r: '))  # razao -> de quantos em quantos números "pular"
dec = a1 + (10 - 1) * r
for c in range(a1, dec+r, r):
    print(f'{c}', end=' -> ')
print('Acabou')

