# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

n = float(input('Digite um valor: R$'))
p = (n*5)/100
print(f'O produto que custava R${n} , está na promoção e seu novo valor é R${(n-p):.2f}')

