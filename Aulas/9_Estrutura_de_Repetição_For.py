
# Laço for

'''
'laço com variável de controle'
'laço de repetição / iteração'

# for "variável" in range(n1,n2):  -> vai de n1 até n2 e depois continua o programa 
# range -> 'intervalo'
# for "variável" in range(n1,n2,n3): 
        n1 -> início
        n2 -> fim
        n3 -> passo  
'''

print('oi')
print('oi')
print('oi')

print('-----' * 10)

for a in range(1,6): # vai imprimir 5x (se colocar de 0 a 6, imprime 6x)
    print('olá')
    print('tchau')
print('fim')

print('-----' * 10)

for b in range(0,6):
    print(b) # vai imprimir os números de 0 a 5 (ignora o último número)

print('-----' * 10)

for c in range(6,0,-1): # o -1 faz imprimir de trás p frente
    print(c)
print('fim')

print('-----' * 10)

for d in range(0,7,2): # imprime de 0 a 7, pulando de 2 em 2
    print(d)

print('-----' * 10)

e = int(input('Digite um número: '))
for f in range(0, e): # vai imprimir de 0 até o número escolhido em 'e'
    print(f)
print('fim')

print('-----' * 10)

g = int(input('Início:  '))
h = int(input('Fim:  '))
i = int(input('Passo:  '))
for j in range(g, h, i): # começa em g, vai até h, pulando de i em i
    print(j)
print('fim')

print('-----' * 10)

for k in range(0, 3):
    l = int(input('Digite um valor:  ')) # vai imprimir l 3x
print('fim')

print('-----' * 10)

m = 0
for n in range(0, 4):
    o = int(input('Digite um valor:  '))
    m += o  # o mesmo que m = m + o |   # a variável m vai 'acumular'/somar os números digitados
print(f'O somatório de todos os valores foi {m}') 

