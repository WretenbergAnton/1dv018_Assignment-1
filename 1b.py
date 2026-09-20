import random

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


print(threesum_brute(create_lst(15)))