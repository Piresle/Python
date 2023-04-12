# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
    # Equilátero: todos os lados iguais;
    # Isósceles: dois lados iguais;
    # Escaleno: todos os lado diferentes. 

a = float(input('Digite o ângulo do lado a:  '))
b = float(input('Digite o ângulo do lado b:  '))
c = float(input('Digite o ângulo do lado c:  '))
if ((a - b) < c < (a + b)) and ((a-c) < b < (a + c)) and ((b - c) < a < (b + c)):
    if a == b == c:
        print('Os ângulos informados podem formar um triângulo EQUILÁTERO.')
    elif a != b != c != a:
        print('Os ângulos informados podem formar um triângulo ESCALENO.')
    elif a == b or a == c or b == c:
        print('Os ângulos informados podem formar um tiângulo ISÓSCELES.')
else:
    print('Os ângulos informados NÃO podem formar um triângulo!')

