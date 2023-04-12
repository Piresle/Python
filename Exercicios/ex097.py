# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
# adaptável. 


def escreva():
    cont = len(frase) + 4
    print('~'*cont)
    print(f'  {frase}')
    print('~'*cont)


frase = str(input('Digite uma frase/palavra:  '))
escreva()
