# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#       -> Quantas pessoas foram cadastradas.
#       -> Uma listagem com as pessoas mais pesadas.
#       -> Uma listagem com as pessoas mais leves.

princ = []
temp = []
maior = cad = menor = 0
while True:
    temp.append(str(input('Nome:  ')))
    cad += 1
    temp.append(float(input('Peso:  ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    esc = str(input('Quer continuar?  ')).upper()
    if esc == 'N':
        break
print('-----'*10)

print(f'Foram cadastradas {len(princ)} pessoas no total.')
print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor:.1f}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]')