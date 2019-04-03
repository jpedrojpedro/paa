from ordenacao.merge_sort import merge_sort
from busca.binary_search import binary_search
from utils.list import generate_list


def verifica_soma(s1, s2, x):
    v1 = merge_sort(s1)
    v2 = merge_sort(s2)
    for e1 in v1:
        e = x - e1
        e2 = binary_search(v2, e)
        if e2 is not None:
            return e1, e2
    return None


if __name__ == '__main__':
    l1 = generate_list(20)
    print(l1)
    l2 = generate_list(25)
    print(l2)
    s = 10
    print(verifica_soma(l1, l2, s))
