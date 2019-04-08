def subconjunto(p, t):
    i = j = 1
    s = []
    v = []
    while i <= len(t.values()):
        if t[i] == p[j]:
            v.append(t[i])
            if len(v) == len(p.values()):
                s.append(i - j)
                j = 0
                v = []
            j += 1
        else:
            j = 1
            v = []
        i += 1
    return s


if __name__ == '__main__':
    s1 = {1: 7, 2: 6}
    print(s1.values())
    s2 = {1: 7, 2: 6, 3: 8, 4: 1, 5: 5, 6: 7, 7: 5, 8: 1, 9: 9, 10: 10,
          11: 1, 12: 5, 13: 7}
    print(s2.values())
    print(subconjunto(s1, s2))
