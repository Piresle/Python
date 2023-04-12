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
