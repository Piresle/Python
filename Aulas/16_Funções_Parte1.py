
# def 

'''
"rotina"
    - criar funções para representar o que é usado frequentemente

-> funções que já vêm com a linguagem Python
    - print()
    - len()
    - input()
    - int()
    - +

-> todas as funções em Python são identificadas por ( ) no final do nome.

-> entre a "def" e o programa principal tem que ter duas linhas vazias 

-> cria comando personalizados

-> parâmetro
    - o que estiver entre () depois da função

'''
from tkinter import N


print('-'*40)
print(f'{"CURSO EM VÍDEO":^40}')
print('-'*40)

print()

def lin():  #função criada para não digitar "print('-'*40)", que é isado frequentemente; coloca-se apenas "lin()"
    print('-'*40)


lin()
print(f'{"CURSO EM VÍDEO":^40}')
lin()

print()

# ----------------------------------------------------------

x = 10
y = 5
som = x + y
print(som)

print()

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa Principal 
soma(2, 5) 
soma(b=4, a=6) #para inverter as posições das variáveis a e b

print()

# ----------------------------------------------------------

def contador(* n): # o * em parâmetro, é usado quando não se sabe quantas variáveis tem
    print(n) #cria uma tupla com os valores
    tam = len(n)
    print(f'Recebi os valores {n} e são {tam} números ao todo.')



contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()

# ----------------------------------------------------------

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

print()

# ----------------------------------------------------------

def somar(* valores): #
    som = 0
    for num in valores:
        som += num
    print(f'Somando os valores {valores} temos {som}')


somar(5, 2)
somar(2, 9, 4)

