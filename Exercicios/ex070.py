# Crie um porgrama que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar. No final, mostre:
#       -> Qual é o total gasto na compra
#       -> Quantos produtos custam mais de R$1000
#       -> Qual é o nome do produto mais barato

tot = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    tot += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else: 
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]  ')).upper()[0].strip()
    if resp == 'N':
        break
print('-----'*15)
print(f'O total gasto foi de R${tot:.2f}')
print(f'{totmil} produto(s) que custam mais de R$1000,00') 
print(f'O nome do produto mais barato foi {barato} e custa R${menor:.2f}')
