# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.


a1 = int(input('primeiro termo:  '))
r = int(input('razão:  '))
termo = a1
cont = 1
while cont <= 10:
    print(termo, end='')
    termo += r
    cont += 1
print('FIM')

 