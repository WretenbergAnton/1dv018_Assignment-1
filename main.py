import time
import random
import matplotlib.pyplot as plt

def random_lst(n):
  result = []
  for _ in range(n):
    num = random.randint(n * -10, n * 10)
    result.append(num)

  return result


def sum_three(lst, s=0):
  result = []
  for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
      for y in range(j + 1, len(lst)):
        if lst[i] + lst[j] + lst[y] == s:
          sort = tuple(sorted((lst[i], lst[j], lst[y])))
          if sort not in result:
            result.append(sort)
  
  return result

def mat_tid(n):
  lst = random_lst(n)
  start = time.perf_counter()
  sum_three(lst)
  stop = time.perf_counter()
  return stop - start


storlekar = list(range(300, 1001, 50))
tider = []
for n in storlekar:
  tider.append(mat_tid())
print(storlekar)
print(tider)

def kor_experiment():
  storlekar = list(range(300, 1001, 50))
  tider = []
  for n in storlekar:
    tider.append(mat_tid(n))
  return storlekar, tider



x, y1 = kor_experiment()
x, y2 = kor_experiment()
x, y3 = kor_experiment()
medel = []
for i in range(len(y1)):
  medel.append((y1[i] + y2[i] + y3[i]) / 3)
plt.plot(x, medel, label="medel av 3 körningar")

plt.xlabel("n")
plt.ylabel("tid (s)")
plt.legend()
plt.show()


