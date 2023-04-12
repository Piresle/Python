'''
# INTERACTIVE HELP
    - help()
    - _doc_
        ex: para ver informações da função input()
            - print(input._doc_)

# DOCSTRINGS
    - str de documentação
    - funções criadas
    - começa exatamente depois do cmd def
    - aspas duplas 3x na linha de baixo do def para "explicar" os parâmetros 

# PARÂMETROS OPCIONAIS
    - colocar um parâmetro paradão para o caso de não ter entrada de dados desse parâmetro

# VARIÁVEIS
    - Global: funciona em todo o programa
    - Local: funciona só dentro da função 

# ESCOPO GLOBAL
    - quando a variável faz parte do programa principal

# ESCOPO LOCAL 
    - quando a variável faz parte apenas de uma função

# ESCOPO DE IMPORTAÇÃO 
    - 

# 'global'
    - para utilizar uma variável global 

# RETORNAR VALORES
    - return
    - "personalizar" a resposta
'''


from re import S
from tkinter import W


help(print)

print()
print('-'*60, '1')
print()
 

def contador(i, f, p):
    """
    -> faz contagem e mostra na tela.
    :param i: início da contagem;
    :param f: fim da contagem;
    :param p: passo da contagem;
    :return: sem retorno 
    """
    c = i
    while c <= 7:
        print(f'{c}', end='..')
        c += p 
    print('FIM!')


help(contador) # vai imprimir o que está entre as aspas duplas


print()
print('-'*60, '2')
print()

def somar(a=0, b=0, c=0): #o valor 0 será utilizado caso nenhum valor seja digitado(se não for digitado nenhum valor para a,o valor de a será 0)
    s = a + b + c
    print(f'A soma é {s}')


somar(3, 4, 5)
somar(8, 4)
help(somar)


print()
print('-'*60, '3')
print()


def teste():
    x = 8 #variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2 # variáve global
print(f'No programa principal, n vale {n}')


print()
print('-'*60, '4')
print()


def teste2(b):
    a = 8 #variável A local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5  #variável A global
teste2(a)
print(f'A fora vale {a}')
#  print(f'B fora vale {b}')  -> b só funciona dentro da função
#  print(f'C fora vale {c}')  -> c só funciona dentro da função


print()
print('-'*60, '5')
print()


def teste3(x):
    global W #utiliza a variável w global; o w local deixa de valer 5 e passa a valer 8
    w = 8
    x += 4
    y = 2
    print(f'W dentro vale {w}')
    print(f'X dentro vale {x}')
    print(f'y dentro vale {y}')


w = 5
teste3(w)
print(f'W fora vale {w}')


print()
print('-'*60, '6')
print()


def somar2(a=0, b=0, c=0):
    s = a + b + c 
    return s


r1 = somar2(3, 4, 5)
r2 = somar2(1, 7)
r3 = somar2(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')


print()
print('-'*60, '7')
print()


def fatorial(num = 1):
    f = 1 #variável local
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número:  '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
print(f'Os resultados são {f1}, {f2} e {f3}')


print()
print('-'*60, '8')
print()


def par(n = 0):
    if n % 2 == 0:
        return True
    else: 
        return False


num = int(input('Digite um número:  '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')

