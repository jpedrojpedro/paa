import app.utils.list as lst


def counting_sort(v):
    maximo = 0
    for i in range(len(v)):
        if maximo < v[i]:
            maximo = v[i]
    maximo += 1
    contador = [0] * maximo
    for i in range(len(v)):
        contador[v[i]] += 1
    final = [0] * len(v)
    k = 0
    for i in range(len(contador)):
        for j in range(contador[i]):
            final[k] = i
            k += 1
    print(final)


if __name__ == '__main__':
    entrada = lst.generate_positive_list(20)
    print(entrada)
    print(counting_sort(entrada))
