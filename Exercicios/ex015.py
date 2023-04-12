# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por 
# km rodado.

km = int(input('Quantos km rodados: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
d = 60
kmr = 0.15
print(f'O carro foi alugado por {dias} dias e o valor a pagar é R${dias*d}')
print(f'Foram percorridos {km}km e o valor ficou em R${km*kmr}')
print(f'O valor total a pagar é R${(dias*d)+(km*kmr)}')

