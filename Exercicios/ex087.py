# Aprimore o desafio anterior, mostrando no final:
#       -> A soma de todos os valores pares digitados.
#       -> A soma dos valores da terceira coluna.
#       -> O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somacol = spar = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]:  '))
print('-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^4} ]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma de todos os valores pares digitados é: {spar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somacol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O valor valor da segunda linha foi: {maior}')
