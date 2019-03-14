import math


def binary_search(vetor, elemento, tamanho, inicio=None, fim=None):
    inicio = inicio or 0
    fim = fim or tamanho - 1
    pivo = math.floor((fim - inicio + 1)/2.0) + inicio
    if vetor[pivo] == elemento:
        return pivo
    if vetor[pivo] >= elemento:
        return binary_search(vetor, elemento, tamanho, inicio, pivo - 1)
    else:
        return binary_search(vetor, elemento, tamanho, pivo + 1, fim)


if __name__ == '__main__':
    entrada = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("Posição: {}".format(binary_search(entrada, 2, len(entrada))))
    exit(0)
