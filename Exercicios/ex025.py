# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. 

n = str(input('Digite um nome:  ')).lower()
var = 'silva' in n 
print(f'O nome digitado tem "SILVA"? {var}')

