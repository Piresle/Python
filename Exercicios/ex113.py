# Reescreva a função leiaint( ) que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiafloat( ) com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n



n1 = leiaint('Digite um número inteiro:  ')
n2 = leiafloat('Digite um número real:  ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
