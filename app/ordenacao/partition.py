# import sys
# sys.path.append('/nethome/a/jpinheiro/Workspace/paa')
import app.utils.list as lst
import random


def partition_not_in_place(vetor):
    ini = 0
    fim = len(vetor) - 1
    # posicao aleatoria
    pos = random.randint(0, fim)
    # trocando pivo com ultima posicao
    pivo = vetor[pos]
    vetor[pos] = vetor[fim]
    vetor[fim] = pivo
    # inicializando vetores auxiliares
    menores = []
    maiores = []
    while ini <= fim:
        if vetor[ini] <= pivo:
            menores.append(vetor[ini])
        else:
            maiores.append(vetor[ini])
        ini += 1
    novo_vetor = menores + [pivo] + maiores
    return novo_vetor, len(menores)


if __name__ == '__main__':
    entrada = lst.generate_positive_list(7)
    print(entrada)
    vetor, pos = partition_not_in_place(entrada)
    print(vetor)
    print("pivô: {}".format(pos + 1))
