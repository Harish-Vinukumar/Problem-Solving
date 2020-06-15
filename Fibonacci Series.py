from functools import lru_cache

@lru_cache(maxsize=10000)
def fibonacci_series(num):
    if num <= 1:
        return num
    else:
        return fibonacci_series(num - 1) + fibonacci_series(num - 2)


num = int(input())
print([fibonacci_series(i) for i in range(num)])