string = 'AAABBB'

i = 0
counter = 0

for i in range(0, len(string)-1):
    if string[i] == string[i+1]:
        counter += 1
    else:
        continue
print(counter)