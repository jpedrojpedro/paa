import math


def altura_piramide(d, x):
    i = 2
    while i <= len(d.values()):
        if d[i] < x:
            return math.log(i, 2)
        i *= 2
    return math.log(i/2, 2)


if __name__ == '__main__':
    entrada = {1: 500, 2: 300, 3: 200, 4: 150, 5: 125, 6: 100, 7: 50}
    print(entrada)
    valor = 50
    print(altura_piramide(entrada, valor))
