
'''
"Enquanto"
-> estrutura de repetição com teste lógico 
-> sabendo o limite, usa for ou while
-> não sabendo o limite, usa while 
'''

for a in range(1, 10):
    print(a)
print('FIM')

print('-----'*10)

b = 1
while b < 10:
    print(b)
    b += 1
print('FIM')

print('-----'*10)

for c in range(1, 5): #tem limite
    d = int(input('Digite um valor: '))
print('FIM')

print('-----'*10)

while e != 0: #não tem limite, o programa para quando digitar 0 | flag / ponto de parada / condição de parada
    e = int(input('Digite um número:  '))
print('FIM')

print('-----'*10)

f = 'S'
while f == 'S': #O programa para quando digitar "N"
    g = int(input('Digite um valor:  '))
    f = str(input('Quer cntinuar? [S/N] ')).upper()
print('FIM')

print('-----'*10)

h = 1
par = impar = 0
while h != 0:
    h = int(input('Digite um número:  '))
    if h != 0:
        if h % 2 == 0:
            par += 1 
        else:
            impar += 1 
print(f'Você digitou {par} números pares e {impar} números ímpares!')

