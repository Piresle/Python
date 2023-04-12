# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

n = str(input('Digite o nome da cidade:  ')).lower().strip()
var = (n[:5] == 'santo')
print(f'O nome digitado começa com a palavra "SANTO"? {var}')

