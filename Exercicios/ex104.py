# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Você precisa digitar um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
