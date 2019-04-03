def fast_power(a, b):
    if b == 1:
        return a
    else:
        c = a * a
        ans = fast_power(c, b // 2)
    if b % 2 != 0:
        return a * ans
    else:
        return ans


if __name__ == '__main__':
    print("Valor: {}".format(fast_power(2, 4)))
    exit(0)
