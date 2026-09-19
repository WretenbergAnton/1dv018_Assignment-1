import random

def create_lst(n):
  result = []

  for _ in range(n):
    num = random.randint(-10 * n, 10 * n)
    result.append(num)

  return result


print(create_lst(15))