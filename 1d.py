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
    sedda = set()
    for j in range(i + 1, len(lst)):
      
  return result


def loop_lst():
  for i in range(3):
    print(f"--------- list: {i + 1} ---------")
    lst = create_lst(15)
    print(lst)
    print(threesum_brute(lst))
    print()


loop_lst()