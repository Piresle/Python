# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o 
# empréstimo será negado. 


casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Quanto você recebe? R$'))
anos = int(input('Em quantos anos você vai pagar?  '))
prest = casa / (anos * 12) 
min = (salario*30) / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos,\n'
        f'a prestação será de R${prest:.2f}')
if prest <= min:
    print('O empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')

