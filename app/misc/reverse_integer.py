from utils.measures import log_time


def reverse(x: int) -> int:
    if x < 0:
        signed = -1
        lnum = list(str(x)[1:])
    else:
        signed = 1
        lnum = list(str(x))
    lnum.reverse()
    rnum = signed * int(''.join(lnum))
    if rnum < -2 ** 31 or 2 ** 31 < rnum:
        return 0
    return rnum


if __name__ == '__main__':
    foo = 12345678
    t, res = log_time(reverse, foo)
    print("Solution: {} | {} s".format(res, t))
