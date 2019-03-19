import app.utils.list as lst


def insertion_sort(numeros):
    final = []
    for n in numeros:
        reorder(final, n)
    print(final)


def reorder(numeros, n):
    if len(numeros) == 0:
        numeros.append(n)
        return
    i = len(numeros) - 1
    numeros.append(-1)
    while i >= 0 and numeros[i] > n:
        numeros[i + 1] = numeros[i]
        i -= 1
    numeros[i + 1] = n


if __name__ == '__main__':
    entrada = lst.generate_list(10)
    print(entrada)
    insertion_sort(entrada)
    exit(0)
