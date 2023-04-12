'''

-> Foco: dividir um programa grande

-> Foco: aumentar a legibilidade

-> Foco: facilitar a manutenção

--> criar uma "biblioteca"
1º nome do módulo 
2º nome da função

-> Vantagens 
    - Organização do código
    - Facilita na manutenção
    - Ocultação de código detalhado 
    - Reutilização em outros projetos

-> Pacotes (biblioteca)
    - pasta que contém módulos 
    - "separar o código por assuntos"
    - utilizados para programas extremamente grandes
    - __ nome __.py 
        - cada pasta do pacote tem que ter um arquivo __nome__.py

# divide o código em mais de um arquivo e depois usa o comando "import" em um dos arquivos, para importar
as funções do outro. 

'''


import Mod # funções deste arquivo que foram importadas para outro, com o nome Mod
# OU from Mod import fatorial (não recomendado)

num = int(input('Digite um número:  '))
fat = Mod.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {Mod.dobro(num)}')
print(f'O triplo de {num} é {Mod.triplo(num)}')

