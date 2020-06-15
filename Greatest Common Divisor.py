from functools import lru_cache


@lru_cache(maxsize=10000)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


print(gcd (38547624, 14578968))