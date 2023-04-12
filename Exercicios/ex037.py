# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão:
    # 1 para binário;
    # 2 para octal;
    # 3 para hexadecimal.


n = int(input('Digite um número inteiro qualquer:  '))
x = int(input('Escolha a base de conversão:\n'
        '1. Binário\n'
        '2. Octal\n'
        '3. Hexadecimal\n'
        '->  '))
if x == 1:
    print(f'O número {n} convertido para Binário é: {bin(n)}')
elif x == 2: 
    print(f'O número {n} convertido para Octal é: {oct(n)}')
elif x == 3:
    print(f'O número {n} convertido para Hexadecimal é: {hex(n)}')
else: 
    print('Opção inválida.')

