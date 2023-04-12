# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
    # À vista dinheiro/cheque: 10% de desconto;
    # À vista no cartão: 5% de desconto;
    # Em até 2x no cartão: Preço normal;
    # 3x ou mais no cartão: 20% de juros.


n = float(input('Preço das compras: R$'))
x = int(input('Escolha a forma de pagamento:\n'
        '[ 1 ] À vista dinheiro/cheque\n'
        '[ 2 ] À vista no cartão\n'
        '[ 3 ] 2x no cartão\n'
        '[ 4 ] 3x ou mais no cartão\n'
        '->  '))
if x == 1: 
    print(f'Você tem 10% de desconto. O valor total a pagar é: R${(n*10)/100}')
elif x == 2:
    print(f'Você tem 5% de desconto. O valor total a pagar é: R${(n*5)/100}')
elif x == 3:
    print(f'Você não tem desconto. Sua compra será parcelada em 2x de R${n/2}')
elif x == 4:
    juros = n + ((n * 20) / 100)
    parcelas = int(input('Quantas parcelas?  '))
    totparc = juros / parcelas
    print(f'Sua compra será parcelada em {parcelas}x, você tem 20% de juros. O valor a pagar é R${totparc:.2f}')
    print(f'Sua compra de R${n} vai custar R${juros:.2f} no final.')
else:
    print('Opção inválida.')

