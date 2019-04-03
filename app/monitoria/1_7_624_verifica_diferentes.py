from ordenacao.merge_sort import merge_sort
from utils.list import generate_list


def verifica_diferentes(s1, s2):
    v1 = merge_sort(s1)
    v2 = merge_sort(s2)
    i1 = i2 = 0
    while i1 < len(v1) and i2 < len(v2):
        if v1[i1] == v2[i2]:
            return False
        if v1[i1] > v2[i2]:
            i1 += 1
        else:
            i2 += 1
    return True


if __name__ == '__main__':
    l1 = generate_list(10)
    # l1 = [1, 2, 3, 4, 5, 6]
    print(l1)
    l2 = generate_list(10)
    # l2 = [7, 8, 9, 10, 11, 12]
    print(l2)
    print(verifica_diferentes(l1, l2))
