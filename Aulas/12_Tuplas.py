
# variável composta (mais de um elemento na mesma variável)
# [ ] -> índice do elemento 
# [x:y] -> mostra os elementos de x até y, mas sem mostrar o y 
# [x:] -> começa no x e vai até o final
# [-x(] -> começa a contar do último elemento
# len( ) -> conta quantos elementos têm na tupla
# for x in y( ) -> faz a repetição até o último elemento de y 
# 'for' pode ser usado para coleções, variaveis compostas, range
# While True -> estrutura de repetição que pode ser interrompida com 'break'
# TUPLAS SÃO IMUTÁVEIS (uma vez definida, fica igual até o final do programa)


lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche) #imprime todos os itens da variavel "lanche"
print(lanche[1]) #imprime apenas o item de índice 1, ou seja, o segundo item
print(lanche[1:3]) #imprime do 1 ao 3, desconsiderando o último
print(lanche[2:]) #imprime do ítem 2, até o final
print(lanche[-1]) #imprime o último elemento
print(lanche[:2]) #imprime do início, até o elemento 2, desconsiderando o último elemento
print(lanche[-2:]) #começa no item -2 e vai até o final
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(lanche[cont])
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche)) #"em ordem" -> imprime os elementos da variavel 'lanche' em ordem (não altera a tupla)

a = (2, 3 ,4)
b = (5, 6, 7, 8)
c = a + b # soma as duas tuplas (junta as duas)
print(c) 
print(len(c)) #conta quantos elementos tem na tupla
print(c.count(5)) #conta quantas vezes o número 5 aparece na tupla
print(c.index(8)) #mostra a posição do elemento 8

pessoa = ('Leticia', 22, 'F') #pode ter mais de um tipo de dados dentro da tupla
print(pessoa) 
del(pessoa) #apaga a variavel da memoria
# a tupla é imutável, menos para ser apagada (não pode deletar um item, só a tupla inteira)

