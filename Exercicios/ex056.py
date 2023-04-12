# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#       - A média de idade do grupo;
#       - Qual é o nome do homem mais velho;
#       - Quantas mulheres têm menos de 20 anos.

id = 0
media = 0
maiorhomem = 0 
nomevelho = 0
totmulher = 0
for p in range(1, 5):
    print(f'---------- {p}º PESSOA ----------')
    nome = str(input('Nome:  ')).strip()
    idade = int(input('Idade:  '))
    sexo = str(input('Sexo [F/M] ')).upper().strip()
    id += idade 
    if p == 1 and sexo == 'M':
        maiorhomem = idade 
        nomevelho = nome 
    if sexo == 'M' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome 
    if sexo == 'F' and idade < 20:
        totmulher += 1
media = id / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maiorhomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher} mulher(es) com mais de 20 anos.')

