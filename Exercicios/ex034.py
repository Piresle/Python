# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual é o seu salário?  '))
if s > 1250.00:
    x = (s*10)/100
    print(f'Você teve um aumento de 10%! Seu salário agora é R${s+x:.2f}')
elif s <= 1250.00:
    y = (s*15)/100
    print(f'Você teve um aumento de 15%! Seu salário agora é R${s+y:.2f}')

