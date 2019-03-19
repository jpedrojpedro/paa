def merge(esquerda, direita):
    v = []
    e = d = 0
    while e < len(esquerda) and d < len(direita):
        if esquerda[e] <= direita[d]:
            v.append(esquerda[e])
            e += 1
        else:
            v.append(direita[d])
            d += 1
    v += esquerda[e:]
    v += direita[d:]
    return v


def merge_sort(vetor):
    if len(vetor) == 1:
        return vetor
    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])
    return merge(esquerda, direita)


if __name__ == '__main__':
    entrada = [7, 5, 2, 3, 4, 1, 6]
    print(merge_sort(entrada))
    exit(0)
