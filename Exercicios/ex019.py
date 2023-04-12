# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random  # OU # from random import choice 
aluno1 = str(input('Digite o primeiro nome: '))
aluno2 = str(input('Digite o segundo nome: '))
aluno3 = str(input('Digite o terceiro nome: '))
aluno4 = str(input('Digite o quarto nome:  '))
lista = [aluno1, aluno2, aluno3, aluno4]
sort = random.choice(lista) # choice(lista)
print(f'O aluno sorteado foi {sort}')

