# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele. 

var = input('Digite algo: ')
print(f'O tipo primitivo da variável é {type(var)}')
print(f'Só tem espaços? {var.isspace()}')
print(f'É alfanumérico? {var.isalnum()}')
print(f'É um número? {var.isnumeric()}')
print(f'É decimal? {var.isdecimal()}')
print(f'É alfabético? {var.isalpha()}')
print(f'Está só em minúsculo? {var.islower()}')
print(f'Está só em maiúsculo? {var.isupper()}')

