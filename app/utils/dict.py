import random


def generate_array_indexed_one(n):
    return {idx + 1: random.randint(-999, 999) for idx in range(n)}


def generate_positive_array_indexed_one(n):
    return {idx + 1: random.randint(1, 999) for idx in range(n)}
