# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela. 

aluno = {}
aluno['Nome'] = str(input('Nome:  ')).capitalize().strip()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}:  '))
print('-'*16)
print(f'{"NOME":<10}{"MÉDIA":<6}')
print(f'{aluno["Nome"]:<10}{aluno["Media"]:<6}')
print('-'*16)
if aluno['Media'] >= 7:
    print(f'{"APROVADO":^16}')
else: 
    print(f'{"REPROVADO":^16}')
