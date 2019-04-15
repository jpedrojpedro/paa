import app.utils.dict as lst


def max_heapify(v, i):
    ult = len(v.keys())
    e = i * 2
    d = i * 2 + 1
    mx = i
    if e <= ult and v[mx] < v[e]:
        mx = e
    if d <= ult and v[mx] < v[d]:
        mx = d
    if mx != i:
        aux = v[i]
        v[i] = v[mx]
        v[mx] = aux
        return max_heapify(v, mx)


def build_max_heap(v):
    ult = len(v.keys())
    i = ult // 2
    while i >= 1:
        max_heapify(v, i)
        i -= 1


if __name__ == '__main__':
    # entrada = {1: 4, 2: 1, 3: 3, 4: 2, 5: 16, 6: 9, 7: 10, 8: 14, 9: 8, 10: 7}
    entrada = lst.generate_positive_array_indexed_one(10)
    print(entrada)
    build_max_heap(entrada)
    print(entrada)
