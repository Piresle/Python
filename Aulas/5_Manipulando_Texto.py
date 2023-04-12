
# Manipulando cadeias de texto (str) 

frase = 'Curso em Video Python' # 21 caracteres (0 a 20)

# FATIAMENTO 
# [ ] -> coloca o índice do caractere entre [ ]
print(frase[9])
print(frase[9:13]) # imprime do índice 9 até o índice 12 (exclui o último)
print(frase[9:21]) # imprime até o 20 
print(frase[9:21:2]) # começa no 9, para no 20 e pula de 2 em 2
print(frase[:5]) # indica o final e não o início, ou seja, imprime do primeiro catactere até o 5
print(frase[15:]) # indica o início e não o final, ou seja, imprime até o final
print(frase[9::3]) # começa no 9 e vai até o final (não foi indica o final entre os ::), de 3 em 3
print(frase[::2]) # imprime as str, pulando de 2 em 2

# ANÁLISE
print(len(frase)) # mostra o comprimento da str
print(frase.count('o')) # conta quantas vezes aparece o que está entre ( )
print(frase.count('o', 0, 13)) #conta o caractere entre ( ), de 0 a 13 apenas
print(frase.find('deo')) # mostra em qual índice começou o que está entre ( )
print(frase.find('leticia')) # retorna "-1" pq o valor pedido não existe na str
print('curso' in frase) # retorna True ou False se a palavra "curso" existir na str

# TRANSFORMAÇÃO
print(frase.replace('Python', 'Android')) # substitui a palavra "Python" por "Android"
print(frase.upper()) # Deixa tudo em maiúculo
print(frase.lower()) # Deixa tudo em minúsculo
print(frase.capitalize()) # deixa tudo minúsculo, menos a primeira letra 
print(frase.title()) # analisa quantas palavras tem na variavel e deixa as primeiras letras em maiúsculo
var = '   Aprenda Python    ' 
print(var.strip()) # remove os espaços a mais (antes e depois da frase/palavra (direita e esquerda))
print(var.rstrip()) # remove os espaços a mais (à direita)
print(var.lstrip()) # remove os espaços a mais (à esquerda)

# DIVISÃO 
print(frase.split()) # divide a variável onde tem espaços 

# JUNÇÃO
print('-'.join(frase)) # junta todos os elementos da frase, separando as palavras com " - "


# em Python, tudo é objeto ( tudo pode-se usar .AlgumaCoisa )
# pode usar mais de um em uma só vez 
# ex:      print(frase.split().lower())

# EX
x = 'Curso Python'
div = x.split() 
print(div[0])

