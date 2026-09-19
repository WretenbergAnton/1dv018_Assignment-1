import random

def create_lst(n):
  result = []

  for _ in range(n):
    num = random.randint(-10 * n, 10 * n)
    result.append(num)

  return result



def threesum_cache(lst, s=0):
  result = []
  for i in range(len(lst) - 1):
    sedda = set()
    for j in range(i + 1, len(lst)):
      needed = s - lst[i] - lst[j]
      if needed in sedda:
        sort_lst = tuple(sorted((lst[i], lst[j], needed)))
        if sort_lst not in result:
          result.append(sort_lst)
      sedda.add(lst[j])

  return result


def loop_lst():
  for i in range(3):
    print(f"--------- list: {i + 1} ---------")
    lst = create_lst(15)
    print(lst)
    print(threesum_cache(lst))
    print()




loop_lst()