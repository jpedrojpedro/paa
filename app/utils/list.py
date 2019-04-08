import random


def generate_list(n):
    return [random.randint(-999, 999) for _ in range(n)]


def generate_positive_list(n):
    return [random.randint(1, 999) for _ in range(n)]


def generate_sorted_list(n):
    return list(range(n))
