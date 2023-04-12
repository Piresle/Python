# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for x in range(1, 51):
    print('.', end='')
    if x % 2 == 0:
        print(x, end=' ')
print('Acabou!')

# OU
'''
for x in range(2, 51, 2):
    print(x, end=' ')
print('Acabou')
'''