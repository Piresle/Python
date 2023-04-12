def aumentar(preco=0, taxa=0, formato=False):
    porcent = preco + ((preco * taxa) / 100)
    return porcent if format == False else moeda(porcent)


def diminuir(preco=0, taxa=0, formato=False):
    porcent = preco - ((preco * taxa) / 100)
    return porcent if formato is False else moeda(porcent)


def dobro(preco=0, formato=False):
    porcent = preco * 2
    return porcent if not formato else moeda(porcent)



def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0):
    return f'R${preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{moeda(dobro(preco))}')
    print(f'Metade do preço: \t{moeda(metade(preco))}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
