# uso dos parênteses

# tipos de variáveis
# int -> números inteiros
# float -> números decimais; números reais; ..ponto flutuante
# str -> texto / '' -> str vazia
# bool -> True / False (a primeira letra sempre maiúscula)
# variáveis são objetos
#    - todo objeto tem características e realiza funcionalidades 
# quando tem () na frente, é um método


n1 = input('Digite um número: ') # o tipo da variável tem que ser especificado 
print(type(n1))
#
n2 = int(input('Digite um valor: ')) # tipo da variável: int
n3 = int(input('Digite outro valor: ')) # tipo da variável: int
s = n2 + n3
print(f'A soma é: {s}')
print(f'A soma entre {n2} e {n3} vale {s}')

# float
n4 = float(input('Digite um número: ')) 
print(n4) # mesmo que o número digitado for um inteiro, aparece como float 

#
n5 = input('Digite algo: ')
print(n5.isnumeric()) # diz se a variável n5 é um número
# .isalpha() -> diz se a variável é alfabética
# .isalnum() -> diz se a variável é alfanumérica
# .is -> várias possibilidades 