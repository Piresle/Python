# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. 

'''
palavras = ('Coldplay', 'Swift', 'Sheeran', 'Weeknd', 'Dragons', 'Blink')
for ordem in palavras:
    print(f'\nAs letras vogais na palavra {ordem.upper()} são: ', end='')
    for letra in ordem:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
'''

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. 

palavras = ('Coldplay', 'Foster ', 'Neighbourhood', 'Elephant',
            'Fray', 'Arctic', 'Muse', 'Panic', 'Dragons',
            'Cinema', 'Moon', 'Wallows', 'Yellowcard')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

