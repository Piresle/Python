# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador 
# PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
pc = randint(0, 10)
vit = 0
while True:
    jog = int(input('Digite um valor:  '))
    pi = str(input('Par ou ímpar? [P/I]  ')).upper()[0].strip()
    total = jog + pc
    if pi == 'P':
        if total % 2 == 0:
            print(f'Você jogou {jog} e o computador jogou {pc}. Total de {total}. Deu par!')
            print(f'Você venceu!')
            vit += 1
        else: 
            print(f'Você jogou {jog} e o computador jogou {pc}. Total de {total}. Deu ímpar!')
            print('Você perdeu!')
            break
    elif pi == 'I':
        if total % 2 != 0:
            print(f'Você jogou {jog} e o computador jogou {pc}. Total de {total}. Deu ímpar!')
            print(f'Você venceu!')
            vit += 1
        else: 
            print(f'Você jogou {jog} e o computador jogou {pc}. Total de {total}. Deu par!')
            print('Você perdeu!')
            break
    print('Vamos jogar novamente... ')
print(f'Você venceu {vit} vez(es)')
