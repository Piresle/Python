# Desenvolva um porgrama que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
# digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for n in range(1, 7):
    x = int(input(f'Digite o {n}º número:  '))
    if x % 2 == 0:
        soma += x
        cont += 1
print(f'Você informou {cont} números PARES e a soma de todos eles foi {soma}.')


