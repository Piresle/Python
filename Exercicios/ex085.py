# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em
# ordem crescente. 

lista = []
par = []
impar = []
for v in range(1, 8):
    lista.append(int(input(f'Digite o {v}º valor:  ')))
print('-----'*10)
for a, b in enumerate(lista):
    if b % 2 == 0:
        par.append(b)
    else:
        impar.append(b)
impar.sort()
par.sort()
print(f'Todos os valores: {lista}')
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')

# OU 

'''
listan = [[], []]
valor = 0 
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor:  '))
    if valor % 2 == 0:
            listan[0].append(valor)
    else:
        listan[1].append(valor)
listan[0].sort()
listan[1].sort()
print(f'Todos os valores: {lista})
print(f'Os valores pares digitados foram: {listan[0]})
print(f'Os valores ímpares digitados foram: {listan[1]})

'''