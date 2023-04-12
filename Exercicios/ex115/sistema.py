# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo 
# de texto simples.
# O sistema só vai ter 2 opções:
    # cadastrar uma nova pessoa
    # listar todas as pessoas cadastradas


from lib.interface import *
from time import sleep
from lib.arquivo import *


arq = 'cursoemvideo.txt'

if not arqExis(arq):
    criarArq(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1:
        lerarq(arq)
    elif resp == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome:  ')).strip().capitalize()
        idade = int(input('Idade:  '))
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
    else:
        print('\033[33mERRO! Digite uma opção válida!\033[m') 
    sleep(2)
