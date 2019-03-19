import random


def generate_list(n):
    return [random.randint(1, n) for _ in range(n)]


def generate_sorted_list(n):
    return list(range(n))
