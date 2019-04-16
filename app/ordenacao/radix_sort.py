import app.utils.list as lst
from app.ordenacao.counting_sort import counting_sort


# TODO: implementar até o final
def radix_sort(v):
    maximo = 0
    for i in range(len(v)):
        if maximo < v[i]:
            maximo = v[i]
    t = []
    b = 1
    while maximo//b > 0:
        b *= 10
    while maximo//b > 0:
        b *= 10
        vetor_b = [v[i]//b for i in range(len(v))]
        t.append(counting_sort(vetor_b))
    return t


if __name__ == '__main__':
    entrada = lst.generate_positive_list(20)
    print(entrada)
    print(radix_sort(entrada))
