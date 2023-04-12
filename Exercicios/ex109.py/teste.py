# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no 
# desafio 108.

import func

n = float(input('Digite o preço: R$'))
print(f'A metade de {func.moeda(n)} é {func.metade(n, True)}')
print(f'O dobro de {func.moeda(n)} é {func.dobro(n, True)}')
print(f'Aumentando 10%, temos {func.aumentar(n, 10, True)}')
print(f'Reduzindo 13%, temos {func.diminuir(n, 13, True)}')
