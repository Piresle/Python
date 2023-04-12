# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#   -> Quantos números foram digitados.
#   -> A lista de valores ordenada de forma decrescente.
#   -> Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    esc = str(input('Quer continuar? [S/N]  ')).upper()
    if esc == 'N':
        break
print('-----'*10)
print(f'Você digitou {len(lista)} elementos.')
print('-----'*10)
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente de valores é {lista}')
print('-----'*10)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else: 
    print('O valor 5 não faz parte da lista!')
