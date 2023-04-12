# Crie um programa que leia o nome de uma pessoa e mostre: 
#  O nome com todas as letras maiúsculas.
#  O nome com todas as letras minúsculas.
#  Quantas letras ao todo (sem considerar os espaços)
#  Quantas letras tem o primeiro nome. 

n = str(input('Digite seu nome completo: '))  # .strip()   -> para remover os espaços 
esp = len(n.replace(" ", ''))
cont = n.find(' ')
print(f'Seu nome em maiúsculas: {n.upper()}\n'
        f'Seu nome em minúsculas: {n.lower()}\n'
        f'Número de letras do seu nome no total: {esp}\n'
        f'Número de letras no primeiro nome: {cont}')

