
'''
-> invés de índices numéricos (como nas listas), usa-se índices "literais"/palavras
-> estruturas de dados semelhantes às tuplas e listas, mas que permite personalizar os índices 

-> { }
    - dicionários ficam sempre entre chaves { }
-> dict()

ex:
dados = dict()    #OU dados = {}
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) 
    - nome é o 'índice' da variável 'Pedro' 
    - vai imprimir 'Pedro'

-> dicionários não aceitam 'append'
    - ex: dados['sexo'] = 'M' 

-> remover elementos 
    - del
        -ex: del dados['idade'] 

-> valor: .values()
    - vai mostrar os elementos do dicionários, não os índices 
    - ex: print(dados.values()) 
        - vai imprimir 'Pedro', 25, 'M'
-> chave: .keys()
    - são os índices 
    - ex: print(dados.keys())
-> item: .items()
    - imprime tanto os valores quanto as chaves

-> semelhança com 'enumerate()' em for
filme = {'título': Star Wars, 'ano': 1977, 'diretor': George Lucas'}
    - for k, v in filme.items():
        - print(f'O {k} é {v}')
            - imprime 'O título é Star Wars
                       O ano é 1977
                       O diretor é George Lucas'

-> pode-se juntar listas, tuplas e dicionários
ex: 
locadora = [['título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'],
            ['título': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'],
            ['título': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski']]
 -> a lista locadora tem o item 0, 1 e 2.
    - o item 0 é o dicionário de Star Wars;
    - o item 1 é o dicionário de Avengers...
print(locadora[0]['ano'])
    - 1977
print(locadora[2]['título'])
    - Matrix

-> .copy()
    - para copiar um conteúdo 
'''

pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(f'1. {pessoas}')
print(f'2. {pessoas["Idade"]}')
print(f'3. O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(f'4. {pessoas.values()}')
print(f'5. {pessoas.keys()}')
print(f'6. {pessoas.items()}')
for k in pessoas.keys():
    print(f'7. {k}')
for k in pessoas.values():
    print(f'8. {k}')
for k, v in pessoas.items():  # semelhante ao '.enumerate()'
    print(f'9. {k} = {v}')
del pessoas['Sexo']
print(f'10. {pessoas}')
pessoas['Nome'] = 'Leandro'  # a variável 'Leandro' fica no lugar da variável 'Gustavo'
pessoas['peso'] = 70.5 # adiciona a chave 'peso' com valor 70.5 ao dicionário 'pessoas' 
print(f'11. {pessoas}')

print()
print('-' * 60)
print()

# criar um dicionário dentro de uma lista
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(f'1. {estado1}')
print(f'2. {estado2}')
print(f'3. {brasil}')
print(f'4. {brasil[0]}')
print(f'5. {brasil[1]}')
#print(f'6. {brasil[1]['Sigla']}')

print()
print('-' * 60)
print()

estados = dict()
br = list()
for c in range(0, 3):
    estados['UFs'] = str(input('Unidade Federativa:  ')).capitalize().strip()
    estados['Siglas'] = str(input('Sigla do estado:  '))
    br.append(estados.copy())
for e in br:
    for k, v in e.items():
        print(f' O campo {k} tem valor {v}')
for x in br:
    for y in e.values():
        print(y)

