# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
#       -> Quantas pessoas têm mais de 18 anos
#       -> Quantos homens foram cadastrados
#       -> Quantas mulheres têm menos de 20 anos

tot18 = homens = menos20 = 0
sexo = 0

while True:
    idade = int(input('Idade:  '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]:  ')).upper()[0].strip()
    if idade >= 18:  
        tot18 += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        menos20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {menos20}')
