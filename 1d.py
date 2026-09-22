import random
import time
import matplotlib.pyplot as plt
import math


def create_lst(n):
    result = []

    for _ in range(n):
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
        sedda = set()
        for j in range(i + 1, len(lst)):
            needed = s - lst[i] - lst[j]
            if needed in sedda:
                sort_lst = tuple(sorted((lst[i], lst[j], needed)))
                result.add(sort_lst)
            sedda.add(lst[j])

    return sorted(result)


def loop_lst():
    for i in range(3):
        lst = create_lst(15)
        print()
        print(f"list {i + 1}")
        print(lst)
        print()
        print("--------- list using threesum brute ---------")
        print(threesum_brute(lst))
        print()
        print("--------- list using threesum cache ---------")
        print(threesum_cache(lst))
        print()
        print("----------------------------------------------")
        print("----------------------------------------------")


def mat_tid(br, ca):
    lst_brut = create_lst(br)
    lst_cache = create_lst(ca)

    time_start_brut = time.perf_counter()
    threesum_brute(lst_brut)
    time_stop_brut = time.perf_counter()
    time_brut = time_stop_brut - time_start_brut

    time_start_cache = time.perf_counter()
    threesum_cache(lst_cache)
    time_stop_cache = time.perf_counter()
    time_cache = time_stop_cache - time_start_cache

    return time_brut, time_cache


def experiment_function():
    lst_brut = range(300, 1001, 50)
    lst_cache = range(1800, 12301, 750)
    tider_brut = []
    tider_cache = []
    for i in range(15):

        tid_brut, tid_cache = mat_tid(lst_brut[i], lst_cache[i])
        tider_brut.append(tid_brut)
        tider_cache.append(tid_cache)

    return list(lst_brut), tider_brut, list(lst_cache), tider_cache


def plot_figure_1():
    x_brute_list = []
    y_brute_list = []
    x_cache_list = []
    y_cache_list = []
    for _ in range(3):
        x_brute, y_brute, x_cache, y_cache = experiment_function()
        x_brute_list.append(x_brute)
        y_brute_list.append(y_brute)
        x_cache_list.append(x_cache)
        y_cache_list.append(y_cache)

    plt.figure()
    for i in range(3):
        plt.plot(x_brute_list[i], y_brute_list[i], label=f"körning {i + 1}")
    plt.title("Figure 1: brute force")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()

    plt.figure()
    for i in range(3):
        plt.plot(x_cache_list[i], y_cache_list[i], label=f"körning {i + 1}")
    plt.title("Figure 1: caching")
    plt.xlabel('n')
    plt.ylabel('tid (s)')
    plt.legend()

    return x_brute_list, y_brute_list, x_cache_list, y_cache_list


def plot_figure_1a(x_brute_list, y_brute_list, x_cache_list, y_cache_list):
    y_medel_brut = []
    y_medel_cache = []

    for i in range(15):
        summa_brut = y_brute_list[0][i] + \
            y_brute_list[1][i] + y_brute_list[2][i]
        y_medel_brut.append(summa_brut / 3)

        summa_cache = y_cache_list[0][i] + \
            y_cache_list[1][i] + y_cache_list[2][i]
        y_medel_cache.append(summa_cache / 3)

    plt.figure()
    plt.plot(x_brute_list[0], y_medel_brut, label="Average")
    plt.title("Figure 1a: Average")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()

    plt.figure()
    plt.plot(x_cache_list[0], y_medel_cache, label="Average")
    plt.title("Figure 1a: Average")
    plt.xlabel("n")
    plt.ylabel("tid (s)")
    plt.legend()

    return y_medel_brut, y_medel_cache


x_brute_list, y_brute_list, x_cache_list, y_cache_list = plot_figure_1()


def lin_reg(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = 0
    sum_xx = 0

    for i in range(n):
        sum_xx += x[i] * x[i]
        sum_xy += x[i] * y[i]

    k = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    m = (sum_y - k * sum_x) / n
    return m, k


def berakna_k(x, y, name):
    log_x = []
    log_y = []
    for i in range(len(x)):
        log_x.append(math.log(x[i]))
        log_y.append(math.log(y[i]))

    m, k = lin_reg(log_x, log_y)
    print(f"{name}: k = {k}")
    return m, k, log_x, log_y


y_medel_brut, y_medel_cache = plot_figure_1a(
    x_brute_list, y_brute_list, x_cache_list, y_cache_list)


def plot_figure_2b(m, k, log_x, log_y, namn):
    linje_y = []
    for i in range(len(log_x)):
        linje_y.append(m + k * log_x[i])

    plt.figure()
    plt.plot(log_x, log_y, "o", label="mätpunkter")
    plt.plot(log_x, linje_y, label=f"anpassad linje, k = {k:.2f}")
    plt.title(f"Figure 2b: log-log, {namn}")
    plt.xlabel("log(n)")
    plt.ylabel("log(tid)")
    plt.legend()


m_b, k_b, log_x_b, log_y_b = berakna_k(
    x_brute_list[0], y_medel_brut, "brute force")
m_c, k_c, log_x_c, log_y_c = berakna_k(
    x_cache_list[0], y_medel_cache, "caching")

plot_figure_2b(m_b, k_b, log_x_b, log_y_b, "brute force")
plot_figure_2b(m_c, k_c, log_x_c, log_y_c, "caching")
plt.show()
