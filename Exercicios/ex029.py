# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual é a velocidade do carro? '))
x = 7.00
if v > 80:
    print('Você foi multado!')
    print(f'Valor da multa: R${(v-80)*x}')
else: 
    print('Você não foi multado!')
print('Tenha um bom dia! Dirija com segurança.')

