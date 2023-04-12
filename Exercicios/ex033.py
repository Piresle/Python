# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from time import sleep
n1 = int(input('Digite um número:  '))
n2 = int(input('Digite outro número:  '))
n3 = int(input('Digite mais um número:  '))
sleep(2)
print('***'*20)
print(f'Os números digitados foram {n1}, {n2} e {n3}')
print('***'*20)
sleep(2)
if n1 >= n2 and n1 >= n3:
    print(f'O número {n1} é o maior!')
elif n2 >= n1 and n2 >= n3:
    print(f'O número {n2} é o maior!')
elif n3 >= n1 and n3 >= n2: 
    print(f'O número {n3} é o maior!')
print('***'*20)
if n1 <= n2 and n1 <= n3:
    print(f'O número {n1} é o menor!')
elif n2 <= n1 and n2 <= n3:
    print(f'O número {n2} é o menor!')
elif n3 <= n1 and n3 <= n2:
    print(f'O número {n3} é o menor!')

