# Faça um programa que leia o sexo de uma pessoa, mas só aceite se for 'M' ou 'F'. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto. 

sexo = str(input('Informe o sexo [F/M] ')).upper()
while sexo != 'M' != 'F':
    sexo = str(input('Valor inválido. Digite novamente:  ')).upper()
print(f'Sexo {sexo} registrado!')

