def fast_power(a, b):
    if b == 1:
        print("{} - {}".format(a, b))
        return a
    else:
        c = a * a
        print("{} - {}".format(c, b // 2))
        ans = fast_power(c, b // 2)
    if b % 2 != 0:
        print("{} - {}".format(a, b))
        return a * ans
    else:
        print("{} - {}".format(a, b))
        return ans


if __name__ == 'main':
    print("Bla bla bla bla")
    print("Valor: {}".format(fast_power(2, 4)))
    exit(0)
