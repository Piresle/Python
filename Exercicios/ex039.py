# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele ainda vai se alistar ao serviço militar;
    # Se é a hora de se alistar;
    # Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 

from datetime import date
ano = int(input('Digite o seu ano de nascimento:  '))
data = date.today().year
idade = data - ano
if idade < 18:
    print(f'Você ainda vai se alistar ao serviço militar. Faltam {18 - idade} anos.')
    print(f'Seu alistamento será em {data - (idade - 18)}')
elif idade == 18:
    print('É hora de se alistar!')
elif idade > 18:
    print(f'Já passou {idade - 18} anos do tempo de alistamento.')
    print(f'Seu alistamento foi em {data - (idade - 18)}')


