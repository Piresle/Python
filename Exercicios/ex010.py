# Crie um porgrama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# US$1,00 = R$3,27

n = float(input('Digite o valor em R$: '))
d = n / 3.27
print(f'Com R${n:.2f}, você pode comprar US${d:.2f}')

