from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def suma_impar(lista):
    impar = filter(lambda x: x % 2 != 0, lista)
    resultado = reduce(lambda x, y: x + y, impar)
    return resultado


print(suma_impar(lista))
