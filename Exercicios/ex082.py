# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares 
# digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número:  ')))
    esc = str(input('Quer continuar? [S/N]  ')).upper()
    if esc == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print('-----'*10)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
