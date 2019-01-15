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
    # entrada = [5, 2, 4, 6, 1, 3]
    entrada = [10, 8, 12, 55, 7, 2, 100, 52, 17, 18, 21]
    insertion_sort(entrada)
    exit(0)
