# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

x = int(input('Digite um número para ver sua tabuada:  '))
for tab in range(0, 11):
    print(f'{x} x {tab} = {x*tab}')




'''
# p/ imprimir todas as tabuadas de 0 a 10


for tabuada in range(0, 11):
    for y in range(0, 11):
        print(f'{tabuada} x {y} = {tabuada*y}')

'''
