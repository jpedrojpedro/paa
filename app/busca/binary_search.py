import app.utils.list as lst


def binary_search(vetor, elemento, inicio=0):
    meio = len(vetor) // 2
    if meio == 0:
        return None
    if vetor[meio] == elemento:
        return inicio + meio
    if vetor[meio] < elemento:
        return binary_search(vetor[meio + 1:], elemento, inicio + meio + 1)
    else:
        return binary_search(vetor[:meio], elemento, inicio)


if __name__ == '__main__':
    entrada = lst.generate_sorted_list(10)
    print(entrada)
    print("Posição: {}".format(binary_search(entrada, 5)))
    exit(0)
