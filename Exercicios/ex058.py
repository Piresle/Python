# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de o a 10. Só que agora o 
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
palpites = 0 
pc = randint(0,10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('-----'*10)
escolha = 0
while escolha != pc:
    if escolha > pc:
        print('MENOS... Tente mais uma vez.')
    elif escolha < pc:
        print('MAIS... Tente mais uma vez.')
    palpites += 1
    print(f'Você errou! Tente novamente.')
    escolha = int(input('Em qual número eu pensei?  '))
    if escolha == pc:
        print(f'Você acertou! Eu pensei no número {pc}.')
        print(f'Foram necessários {palpites} palpites para vencer!')

