''' 
Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar 
    [3] maior
    [4] novos números
    [5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. 
'''

v1 = int(input('Digite um valor:  '))
v2 = int(input('Digite outro valor:  '))
escolha = int(input('''Escolha uma opção:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa '''))
if escolha == 1:
    print(f'A soma entre {v1} e {v2} é {v1 + v2}')
elif escolha == 2:
    print(f'A multiplicação entre {v1} e {v2} é {v1 * v2}')
elif escolha == 3:
    if v1 > v2:
        print(f'O número {v1} é maior que o número {v2}')
    elif v2 > v1:
        print(f'O número {v2} é maior que o número {v1}')
    elif v1 == v2:
        print('Os números informados são iguais!')
elif escolha == 5:
    print('FIM')
while escolha == 4:
    v1 = int(input('Digite um valor:  '))
    v2 = int(input('Digite outro valor:  '))
    escolha = int(input('''Escolha uma opção:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa '''))
    if escolha == 1:
        print(f'A soma entre {v1} e {v2} é {v1 + v2}')
    elif escolha == 2:
        print(f'A multiplicação entre {v1} e {v2} é {v1 * v2}')
    elif escolha == 3:
        if v1 > v2:
            print(f'O número {v1} é maior que o número {v2}')
        elif v2 > v1:
            print(f'O número {v2} é maior que o número {v1}')
        elif v1 == v2:
            print('Os números informados são iguais!')
    elif escolha == 5:
        print('FIM')

