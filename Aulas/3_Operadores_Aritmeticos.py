# Operadores Aritméticos 
 
#  + adição
# - subtração
# * multiplicação
# % resto da divisão
# ** potência
# / divisão
# // parte inteira da divisão
# == igual
# = recebe/atribuição

# todo operador precisa de um operando 
#    - operandp: pode ser um número, uma str(menos no caso dos operadores aritméticos) ou variáveis 

# ordem de precedência 
#   - 1º ()
#   - 2º **
#   - 3º *  /  //  % 
#   - 4º +  - 

# EX
n1 = 5 + 4 + 3 
n2 = 5 ** 4
n3 = 5 / 4 
n4 = pow(4,3) # potência 
n5 = 81**(1/2) # raiz quadrada de 81
n6 = 25**(1/2) # raiz quadrada de 25
n7 = 'oi' + 'olá' # "concatenação" 
n8 = 'oi' * 5
n9 = 5 * 4 + (3 - 2) * 1 
print(f'n1 {n1}')
print(f'n2 {n2}')
print(f'n3 {n3}')
print(f'n4 {n4}')
print(f'n5 {n5}')
print(f'n6 {n6}')
print(f'n7 {n7}')
print(f'n8 {n8}')
print(f'n9 {n9}')


var = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer {var:>20}!') # o símbolo > deixa a str alinhada à direita 
#  :20  -> deixa a variável em 20 caracteres
#  < para alinhar à esquerda 
#  :^20  -> deixa a variável alinhada entre os 20 caracteres(pode colocar outros símbolos antes do ^)


n10 = int(input('Digite um número: '))
n11 = int(input('Digite outro número: '))
s = n10 + n11 
m = n10 * n11
sub = n10 - n11
d = n10 / n11
di = n10 // n11
p = n10 ** n11 
div = n10 % n11
print(f'A soma é {s}\n'  # \n  -> quebra de linha 
        f'A multiplicação é {m}\n'
        f'A subtração é {sub}\n'
        f'A divisão inteira é {di}\n'
        f'A divisão é {d:.3f}\n'  # :.3f  -> mostra só 3 casas depois da vírgula
        f'O resto da divisão é {div}\n'
        f'A exponenciação é {p}')
# end=' '  -> para não ter quebra de linha 

