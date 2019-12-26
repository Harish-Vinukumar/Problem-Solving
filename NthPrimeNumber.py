# A function that returns
# Nth prime Number

def find_number(n):
    prime_numbers = list()
    i = 2
    while len(prime_numbers) != n:
        x = 0

        for j in range(2, i):

            if i % j  == 0:
                x += 1

        if x == 0:
            prime_numbers.append(i)
        i += 1

    return prime_numbers[n-1]

n = 10
print(find_number(n))
