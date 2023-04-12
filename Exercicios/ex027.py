# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

n = str(input('Digite seu nome completo:  ')).strip()
x = n.split()
print(f'O primeiro nome é {x[0]} e o último é {x[len(x)-1]}.')

