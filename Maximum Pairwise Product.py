input_1 = int(input())
input_2 = input()
input_2 = [int(x) for x in input_2.split()]

if len(input_2) != input_1:
    print("Enter the specified length of numbers")
    input_2 = input()
    input_2 = [int(x) for x in input_2.split()]

input_3 = list()
for x in input_2:
    for y in input_2:
        if x != y:
            input_3.append(x*y)

print(max(input_3))
