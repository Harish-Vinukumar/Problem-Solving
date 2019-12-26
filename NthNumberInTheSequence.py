# A function that returns the
# Nth number in the sequence
# 1,5,3,4,3.5,...

def find_number(n):
    sequence = list()
    x = 1
    y = 5
    sequence.extend([x,y])
    for i in range(2, n):
        z = (x + y) / 2
        sequence.append(z)
        x, y = y, z

    return sequence[n-1]

n = 10
print(find_number(n))