from functools import lru_cache


@lru_cache(maxsize=100000000)
def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num - 1) * num


print(factorial(10))