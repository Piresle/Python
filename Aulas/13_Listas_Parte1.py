

'''
-> MUTÁVEIS
-> entre [ ]
-> vários itens
_________________________________________________________________________________________________________
    - CMD
-> .append() -> adiciona itens no final da lista
-> .insert( índice , item ) -> coloca-se entre () o índice do item a ser adicionado, depois o item
-> del lista[índice] -> para deletar um item da lista 
-> lista.pop() -> a função pop normalmente deleta o último item da lista, mas pode deletar um específico
                    colocando o índice do item entre os ( )
-> lista.remove(item) -> revome o item entre ( ) da lista
    +) if item in lista:
            lista.remove(item)
-> lista.sort() -> colocar todos os valores da lista em ordem 
-> lista.sort(reverse=True) -> deica os valores na ordem reversa
-> len(lista) -> informa o tamanho da lista (quantos elementos ela possui)
__________________________________________________________________________________________________________
- criar listas com range
    -> lista = list(range(0, 1))
''' 

num = [2, 5 ,9, 1]
print('1.',num)

num[2] = 3 #o número 3 será adicionado no índice 2 (ocupando o espaço do outro elemento)
print('2.',num)

num.append(7) # adiciona o número 7 no final da lista
print('3.',num)

num.sort() # valores em ordem
print('4.',num)

num.sort(reverse=True) # ordena os elementos na ordem reversa 
print('5.',num)

num.insert(2, 0) # adiciona o valor 0 na posição 2
print('6.',num)

num.pop() # elimina o último elemento ou o elemento que estiver entre ( )
print('7.',num)

num.remove(2) # remove a primeira ocorrencia do valor determinado entre ( )
print('8.',num)
#OU
if 2 in num:
    num.remove(2)
else:
    print('Não achei o número 2')

print(f'Essa lista tem {len(num)} elementos')

print('-----'*10)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...')

for c, v in enumerate(valores): 
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('-----'*10)

lista = []
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: '))) #os números digitados ferão parte da lsita
for c, v in enumerate(lista): 
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('-----'*10)

a = [2, 3, 4, 7]
b = a # as duas são iguais; estão ligadas; o que muda em uma, muda na outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:] # b recebe todos os itens de a, mas não se liga a ela; b recebe uma "cópia" de a
print(b)

