import random


def create_lst(n):
    result = []
    for _ in range(n):
        num = random.randint(1 * n, 10 * n)
        result.append(num)

    return result


def selection_sort(lst):
    result = lst[:]

    for i in range(len(lst) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(lst)):
            if result[cur_min_idx] > result[j]:
                cur_min_idx = j
        result[i], result[cur_min_idx] = result[cur_min_idx], result[i]

    return result


def bubble_sort(lst):
    result = lst[:]

    for i in range(len(lst)):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def insertion_sort(lst):
    result = lst[:]

    for i in range(len(result)):
        j = i
        while result[j - 1] > result[j] and j > 0:
            result[j - 1], result[j] = result[j], result[j - 1]
            j = j - 1

    return result


print(insertion_sort(create_lst(5)))
