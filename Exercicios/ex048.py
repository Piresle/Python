# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no 
# intervalo de 1 até 500.

soma = 0 # acumulador soma valores
cont = 0 # contador soma 1
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont = cont + 1
        soma = soma + x
print(f'A soma de todos os {cont} valores solicitados é {soma}')


