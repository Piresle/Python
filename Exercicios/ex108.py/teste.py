# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os 
# valores como um valor monetário formatado. 

import Moeda

num = float(input('Digite o valor: R$'))
t = int(input('%: '))

print(f'O dobro de {Moeda.moeda(num)} é {Moeda.dobro(num)}')

print(f'A metade de {Moeda(num)} é {Moeda.metade(num)}')

print(f'Aumentando {t}%, temos {Moeda.aumentar(num)}')
