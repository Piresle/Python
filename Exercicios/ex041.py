# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
# mostre sua categoria, de acordo com a idade:
    # Até 9 anos: MIRIM
    # Até 14 anos: INFANTIL
    # Até 19 anos: JUNIOR
    # Até 20 anos: SÊNIOR
    # Acima: MASTER


from datetime import date
ano = int(input('Digite seu ano de nascimento:  '))
data = date.today().year
idade = data - ano 
if idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print ('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')

