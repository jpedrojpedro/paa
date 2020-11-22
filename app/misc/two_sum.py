import random
from utils.measures import log_time


def two_sum_1(nums, target):
    # brute force solution
    for i, v1 in enumerate(nums):
        for j, v2 in enumerate(nums):
            if v1 + v2 == target:
                return [i, j]
    return []


def two_sum_2(nums, target):
    # optimized solution
    idx_nums = {num: [] for num in nums}
    for idx, num in enumerate(nums):
        idx_nums[num].append(idx)
    sn = sorted(nums)
    i = 0
    j = len(sn) - 1
    while i != j:
        aux = sn[i] + sn[j]
        if aux == target:
            pos_i = idx_nums[sn[i]][0]
            idx_nums[sn[i]].remove(pos_i)
            pos_j = idx_nums[sn[j]][0]
            idx_nums[sn[j]].remove(pos_j)
            return [pos_i, pos_j]
        if aux > target:
            j -= 1
        else:
            i += 1
    return []


if __name__ == '__main__':
    questions = [
        {'numbers': [2, 7, 11, 15], 'target': 9},
        {'numbers': [3, 2, 4, 6], 'target': 6},
        {'numbers': [random.randint(1, 100) for i in range(100)], 'target': 32},
        {'numbers': [random.randint(1, 1_000_000) for i in range(1_000_000)], 'target': 640},
    ]
    for q in questions:
        print("Input size: {}".format(len(q['numbers'])))
        t, res = log_time(two_sum_2, q['numbers'], q['target'])
        print("Optimized solution: {} | {} s".format(res, t))
        t, res = log_time(two_sum_1, q['numbers'], q['target'])
        print("Brute Force solution: {} | {} s".format(res, t))
