def aumentar(preco, taxa):
    porcent = preco + ((preco * taxa) / 100)
    return porcent


def diminuir(preco, taxa):
    porcent = preco - ((preco * taxa) / 100)
    return porcent


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2 

