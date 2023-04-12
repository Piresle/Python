# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo. 

# a < b + c and b < a + c and c < a + b
a = float(input('Digite o ângulo do lado a:  '))
b = float(input('Digite o ângulo do lado b:  '))
c = float(input('Digite o ângulo do lado c:  '))
if ((a - b) < c < (a + b)) and ((a-c) < b < (a + c)) and ((b - c) < a < (b + c)):
    print('Os ângulos informados podem formar um triângulo!')
else:
    print('Os ângulos informados NÃO podem formar um triângulo!')

