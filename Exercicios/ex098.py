# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
#   - De 1 até 10, de 1 em 1
#   - De 10 até 0, de 2 em 2
#   - Uma contagem personalizada.

from time import sleep


def lin():
    print('-'*40)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    lin()
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input(f'{"Início:  ":<10}'))
fim = int(input(f'{"Fim:  ":<10}'))
passo = int(input(f'{"Passo:  ":<10}'))
contador(inicio, fim, passo)
