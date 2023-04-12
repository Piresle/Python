def aumentar(preco=0, taxa=0):
    porcent = preco + ((preco * taxa) / 100)
    return porcent


def diminuir(preco=0, taxa=0):
    porcent = preco - ((preco * taxa) / 100)
    return porcent


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2 


def moeda(preco=0, moeda=0):
    return f'R${preco:>8.2f}'.replace('.', ',')


