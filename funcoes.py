def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


def pesquisa(numero):
    if numero > 0 and numero != 0:
        return "P"
    elif numero < 0:
        return "N"
    if numero == 0:
        return "Z"


a = []
b = []


def bota(num):
    a.append(num)


def coloca(numero):
    b.append(numero)
