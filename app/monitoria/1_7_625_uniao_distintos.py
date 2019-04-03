from ordenacao.merge_sort import merge_sort
from utils.list import generate_list


def uniao_distintos(s1, s2):
    v1 = merge_sort(s1)
    v2 = merge_sort(s2)
    vf = []
    e = None
    i1 = i2 = 0
    while i1 < len(v1) and i2 < len(v2):
        if v1[i1] <= v2[i2]:
            if e != v1[i1]:
                vf.append(v1[i1])
                e = v1[i1]
            i1 += 1
        else:
            if e != v2[i2]:
                vf.append(v2[i2])
                e = v2[i2]
            i2 += 1
    return vf


if __name__ == '__main__':
    l1 = generate_list(20)
    print(l1)
    l2 = generate_list(20)
    print(l2)
    print(uniao_distintos(l1, l2))
