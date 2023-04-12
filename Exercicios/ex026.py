# Faça um programa que leia uma frase pelo teclado e mostre:
#   Quantas vezes aparece a letra "A".
#   Em que posição ela aparece a primeira vez.
#   Em que posição ela aparece a última vez.

n = str(input('Digite uma frase:  ')).lower().strip()
a = n.count('a')
b = n.find('a')+1
c = n.rfind('a')+1
print(f'A letra "A" aparece {a} vezes na frase digitada.\n'
        f'Aparece a primeira vez na posição {b}\n'
        f'E aparece a última vez na posição {c}.')

