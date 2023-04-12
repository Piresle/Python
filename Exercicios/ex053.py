# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase/palavra:  ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inv = junto[::-1]
print(f'O inverso de {junto} é {inv}')
if inv == junto:
    print('A frase/palavra digitada É palíndromo!')
else:
    print('A frase/palavra digitada NÃO é palíndromo')

