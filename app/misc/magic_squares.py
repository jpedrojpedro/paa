def forming_magic_square(s):
    """
    Forming Magic Squares

    - brute force solution
    - generate all possible matrix 3x3 which values are unique and between [1,9]
    - the possible matrix are 9!
    - filter all possible 3x3 magic square
    - compare magic squares with the input s given and calculate costs
    - return the min cost
    """
    magic_squares = []
    for i1 in range(1, 10):
        for i2 in range(1, 10):
            for i3 in range(1, 10):
                for i4 in range(1, 10):
                    for i5 in range(1, 10):
                        for i6 in range(1, 10):
                            for i7 in range(1, 10):
                                for i8 in range(1, 10):
                                    for i9 in range(1, 10):
                                        uniq = {i1, i2, i3, i4, i5, i6, i7, i8, i9}
                                        if len(uniq) != 9:
                                            continue
                                        aux = [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]]
                                        if is_magic_square(aux):
                                            magic_squares.append(aux)
                                            print(aux)
    cost = []
    for ms in magic_squares:
        aux = 0
        for i in range(3):
            zipped = zip(ms[i], s[i])
            for x, y in zipped:
                aux += abs(x - y)
        cost.append(aux)
    return min(cost)


def is_magic_square(s):
    d1 = s[0][0] + s[1][1] + s[2][2]
    d2 = s[2][0] + s[1][1] + s[0][2]
    if sum(s[0]) == sum(s[1]) and sum(s[1]) == sum(s[2]) and \
       sum(s[2]) == d1 and \
       d1 == sum([s[i][2] for i in range(3)]) and \
       sum([s[i][2] for i in range(3)]) == sum([s[i][1] for i in range(3)]) and \
       sum([s[i][1] for i in range(3)]) == sum([s[i][0] for i in range(3)]) and \
       sum([s[i][0] for i in range(3)]) == d2:
        return True
    return False


if __name__ == '__main__':
    # square_input = """
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # """

    # expected cost: 4
    # square_input = """
    # 4 8 2
    # 4 5 7
    # 6 1 6
    # """

    # expected cost: 1
    square_input = """
    4 9 2
    3 5 7
    8 1 5
    """

    parsed_square = []

    for lst in square_input.strip().split('\n'):
        parsed_square.append([int(num) for num in lst.split()])

    result = forming_magic_square(parsed_square)
    print(result)
