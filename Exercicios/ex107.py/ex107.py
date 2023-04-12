# Crie um módulo chamado moeda.py que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e
# metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


from Moeda import dobro, metade, aumentar

num = float(input('Digite o valor: R$'))
por = int(input('%: '))

dob = dobro(num)
print(f'O dobro de R${num} é R${dob:.2f}')

met = metade(num)
print(f'A metade de R${num} é R${met:.2f}')

au = aumentar(num, por)
print(f'Aumentando {por}%, temos R${au:.2f}')
