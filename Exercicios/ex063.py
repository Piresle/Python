# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma seuqência de Fibonacci. 

print('-----'*10)
print('SEQUÊNCIA DE FIBONACCI')
print('-----'*10)
n = int(input('Quantos termos você quer mostrar?  '))
t1 = 0
t2 = 1
print('-----'*10)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3 
    cont += 1
print(' -> FIM')

# "a sequencia de fibonacci sempre começa com 0 e 1, o terceiro termo é 0+1, o próximo termo é a soma dos 
# dois anteriores..."
