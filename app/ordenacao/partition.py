# import sys
# sys.path.append('/nethome/a/jpinheiro/Workspace/paa')
import app.utils.list as lst


def partition_not_in_place(vetor):
    ini = 0
    pos = len(vetor) - 1
    pivo = vetor[pos]
    menores = []
    maiores = []
    while ini < pos:
        if vetor[ini] <= pivo:
            menores.append(vetor[ini])
        else:
            maiores.append(vetor[ini])
        ini += 1
    final = menores + [pivo] + maiores
    return final, len(menores)


if __name__ == '__main__':
    entrada = lst.generate_positive_list(7)
    print(entrada)
    vetor, pos = partition_not_in_place(entrada)
    print(vetor)
    print("pivô: {}".format(pos + 1))
