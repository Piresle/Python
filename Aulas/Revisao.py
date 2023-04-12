'''- (X*Y)/100   -> porcentagem (X=o valor / Y=a porcentagem de X)
- ( b - c ) < a < b + c  and  ( a - c ) < b < a + c  and  ( a - b ) < c < a + b   -> triângulo
	- a < b + c  and  b < a + c  and  c < a + b 
- peso / altura ** 2  -> imc
- an = a1 + (n-1)*r  -> PA '''

# Porcentagem
n1 = int(input('valor: '))
n2 = int(input('Porcentagem: '))
porcent = (n1*n2)/100
print(porcent)

# PA
a1 = float(input('a1: '))
n = float(input('n: '))
r = float(input('r: '))
an = a1 + (n-1) * r 
print('an = {} '.format(an))

# triângulo 
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
tri = (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b 
print(tri)

# operadores aritméticos 
# multiplicação * 
# adição + e subtração -
# divisão /   %   //

# Operadores lógicos 
# and -> retorna true se ambas as afirmações forem verdadeiras
# or -> retorna true se uma das afirmações for verdadeira
# not -> retorna falso se o resultado for verdadeiro 

# operadores relacionais
# > maior que
# < menor que 
# == igual a
# >= maior ou igual
# <= menor ou igual 
# = atribuição

def dobrar(x):
    return 2 * x

def triplicar(x):
    triplo = 3 * x
    return triplo

n1 = float(input('Digite um número: '))
dobro = dobrar(n1)
print(f'O dobro é: {dobro}')
print('O triplo é: {}'.format(triplicar(n1)))

# Formatação de str
# são str com a letra f no início e { } para realizar a interpolação de expressões 
nome = 'stringg'
print(f'O nome é: {nome}!') # o print vai retornar como: O nome é stringg!
# Pode ser usado com funções

# Acessando dicionários
dicionario = dict({'nome': 'Leticia', 'ocupacao': 'faculdade'})
print(f"{dicionario['nome']} está na {dicionario['ocupacao']}")

# str multilinha
site1 = 'youtube'
site2 = 'instagram'
site3 = 'facebook'
print(
    f"Primeiro site: {site1}\n" # \n -> quebra de linha
    f"Segundo site: {site2}\n"
    f"Terceiro site: {site3}"
)

