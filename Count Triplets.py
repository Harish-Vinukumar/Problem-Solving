from collections import Counter
arr = [1, 2, 2, 4]
r = 2

r2 = Counter()
r3 = Counter()
counter = 0

for x in arr:
    if x in r3:
        counter += r3[x]

    if x in r2:
        r3[x * r] += r2[x]

    r2[x * r] += 1

print(counter)