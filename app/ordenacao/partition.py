# import sys
# sys.path.append('/nethome/a/jpinheiro/Workspace/paa')
import app.utils.list as lst


def partition_not_in_order(A):
    p = 0
    r = len(A) - 1
    x = A[r]
    menores = []
    maiores = []
    j = p
    while j < r:
        if A[j] <= x:
            menores.append(A[j])
        else:
            maiores.append(A[j])
        j += 1
    final = menores + [x] + maiores
    return final, len(menores)


if __name__ == '__main__':
    entrada = lst.generate_list(20)
    print(entrada)
    print(partition_not_in_order(entrada))
    exit(0)

