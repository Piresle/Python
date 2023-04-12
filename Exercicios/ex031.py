# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 
# R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. 

d = int(input('Qual é a distância da viagem?  '))
p1 = 0.50
p2 = 0.45
if d <= 200:
    print(f'Para uma viagem de {d}km. O preço da passagem é R${d*p1:.2f}')
else: 
    print(f'Para uma viagem de {d}km. O preço da passagem é R${d*p2:.2f}')

