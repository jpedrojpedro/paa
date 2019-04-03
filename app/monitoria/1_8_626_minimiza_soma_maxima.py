from ordenacao.merge_sort import merge_sort
from utils.list import generate_list


def minimiza_soma_maxima(s):
    v = merge_sort(s)
    ve = []
    vd = []
    for i, e in enumerate(v):
        if i % 2 != 0:
            ve.append(e)
        else:
            vd.append(e)
    sum_e = sum(ve)
    sum_d = sum(vd)
    print("Tamanho: {} vs {} | Soma: {} vs {}".format(len(ve), len(vd), sum_e, sum_d))
    return max(sum_e, sum_d)


if __name__ == '__main__':
    l1 = generate_list(40)
    print(l1)
    print(minimiza_soma_maxima(l1))
