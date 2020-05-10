num1 = 2
num_list = [1, 5, 3, 4, 2]

counter = []
# for i in range(len(num_list)-1):
#     for j in range(i+1, len(num_list)):
#         if abs(num_list[i] - num_list[j]) == num1:
#            counter += 1
print(sum([1 if abs(num_list[i] - num_list[j]) == num1 else 0 for i in range(len(num_list)-1) for j in range(i+1, len(num_list))]))
