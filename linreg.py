import random
import time
import matplotlib.pyplot as plt


def create_lst(n):
    result = []

    for i in range(n):
        num = random.randint(-10 * n, 10 * n)
        result.append(num)

    return result


def threesum_brute(lst, s=0):
    result = []

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            for y in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[y] == s:
                    unique = tuple(sorted((lst[i], lst[j], lst[y])))
                    if unique not in result:
                        result.append(unique)

    return result


def threesum_cache(lst, s=0):
    result = set()

    for i in range(len(lst) - 1):
        seen = set()
        for j in range(i + 1, len(lst)):
            need = s - lst[i] - lst[j]
            if need in seen:
                sort = tuple(sorted((lst[i], lst[j], need)))
                result.add(sort)
            seen.add(lst[j])

    return sorted(result)


def loop_lst():
    for i in range(3):
        lst = create_lst(15)
        print()
        print(lst)
        print()
        print(f"List {i + 1}: Brute force")
        print(threesum_brute(lst))
        print()
        print(f"List {i + 1}: Caching")
        print(threesum_cache(lst))
        print()
        print("--------------------------")


def mat_tid(br, ca):
    lst = create_lst(br)
    start_br = time.perf_counter()
    threesum_brute(lst)
    stop_br = time.perf_counter()

    time_br = stop_br - start_br

    lst = create_lst(ca)
    start_ca = time.perf_counter()
    threesum_cache(lst)
    stop_ca = time.perf_counter()

    time_ca = stop_ca - start_ca

    return time_br, time_ca


def experiment_function():
    lst_brute = range(300, 1001, 50)
    lst_cache = range(1800, 12301, 750)

    time_brute = []
    time_cache = []

    for i in range(len(lst_brute)):
        time_br, time_ca = mat_tid(lst_brute[i], lst_cache[i])
        time_brute.append(time_br)
        time_cache.append(time_ca)

    return list(lst_brute), time_brute, list(lst_cache), time_cache


def run_three_times():
    x_brute = []
    y_brute = []
    x_cache = []
    y_cache = []

    for _ in range(3):
        x_br, y_br, x_ca, y_ca = experiment_function()
        x_brute.append(x_br)
        y_brute.append(y_br)
        x_cache.append(x_ca)
        y_cache.append(y_ca)

    return x_brute, y_brute, x_cache, y_cache


def plot_figure_1(x_brute, y_brute, x_cache, y_cache):

    plt.figure()
    for i in range(3):
        plt.plot(x_brute[i], y_brute[i], label=f"Körning {i + 1}")

    plt.title("Figure 1: Brute force")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()

    plt.figure()
    for i in range(3):
        plt.plot(x_cache[i], y_cache[i], label=f"Körning {i + 1}")

    plt.title("Figure 1: Caching")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()


def plt_figure_1a(x_brute, y_brute, x_cache, y_cache):

    new_y_brute = []
    new_y_cache = []
    for i in range(len(x_brute[0])):
        sum_of_y_brute = y_brute[0][i] + y_brute[1][i] + y_brute[2][i]
        sum_of_y_cache = y_cache[0][i] + y_cache[1][i] + y_cache[2][i]
        new_y_brute.append(sum_of_y_brute / 3)
        new_y_cache.append(sum_of_y_cache / 3)

    plt.figure()
    plt.plot(x_brute[0], new_y_brute, label="Medel värde av tre körningar")
    plt.title("Figure 1a: Medevärdet av brute force")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()

    plt.figure()
    plt.plot(x_cache[0], new_y_cache, label="Medel värde av tre körningar")
    plt.title("Figure 1a: Medevärdet av caching")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()

    return new_y_brute, new_y_cache


x_brute, y_brute, x_cache, y_cache = run_three_times()
plot_figure_1(x_brute, y_brute, x_cache, y_cache)
plt_figure_1a(x_brute, y_brute, x_cache, y_cache)
plt.show()
