
'''
-> append( )
    -> lista2.append(lista1[:])
        - a lista2 recebe uma cópia da lista1 
        - ex:
            -> lista1 = ['Pedro', 25, 'Maria', 32] #pedro é o elemento 0, 25 é o elemento 1,...
            -> lista2.append(lista1[:]) #[:] significa que a lista 2 recebrá uma cópia de todos os elementos
                                        da lista1
            -> lista2 = ['Pedro', 25], ['Maria', 32]
                - "Pedro" e 25, que antes eram dois elementos, agora são um só elemento (elemento 0 da lista2)
            -> print(lista2[0][0]) #imprime o item 0 do elemento 0 ("Pedro")
            -> print(lista2[1][1]) #imprime o item 1 do elemento 1 (32)
            -> print(lista2[1]) #imprime os itens do elemento 1 ('Maria', 32)
'''

listateste = []
listateste.append('Leticia') #o nome se torna parte da 'listateste' (elemento 0)
listateste.append(23) #o número 23 se torna parte da 'listateste' (elemento 1)
print(f'1.{listateste}')

print('-----'*10)

galera = []
galera.append(listateste) # a lista galera recebe a listateste (ligação entre as duas)
listateste[0] = 'Pedro' #o elemento 0 da listateste passa a valer 'Pedro'
listateste[1] = 26 # o elemento 1 da listateste passa a valer 26
galera.append(listateste)
print(f'2.{galera}')

print('-----'*10)

lista1 = []
lista1.append('Mateus')
lista1.append(20)
lista2 = []
lista2.append(lista1[:]) # a lista2 recebe uma cópia da lista1
lista1[0] = 'Stef'
lista1[1] = 35
lista2.append(lista1[:]) # a lista2 recebe outra cópia, com os novos valores (da lista1) informados 
print(f'3.{lista2}')

print('-----'*10)

teste = [['João', 20], ['Ana', 30], ['Maria', 40]] # o elemento 0 tem dois itens (item 0 e item 1)
print(f'4.{teste}')
print(f'5.{teste[2][1]}') #item 1 do elemento 2 
for p in galera:
    print(f'6. {p[0]} tem {p[1]} anos de idade.')

print('-----'*10)

lista = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome:  ')))
    dado.append(int(input('Idade:  ')))
    lista.append(dado[:]) #se não criar uma cópia dos dados, imprime uma lista vazia
    dado.clear()
print(f'7.{lista}')
# +
totmai = 0
totmin = 0
for p in lista:
    if p[1] > 21:
        print(f'8. {p[0]} é maior de idade.')
        totmai += 1
    else: 
        print(f'9. {p[0]} é menor de idade.')
        totmai += 1
print(f'10. Temos {totmai} maiores de  idade e {totmin} menores de idade.')

