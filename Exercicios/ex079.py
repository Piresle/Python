# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
# únicos digitados, em ordem crescente.

lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar.')
    esc = str(input('Quer continuar? [S/N]  ')).upper()
    if esc == 'N':
        break
print('-----'*10)
lista.sort()
print(f'Os valores únicos digitados foram: {lista}')
